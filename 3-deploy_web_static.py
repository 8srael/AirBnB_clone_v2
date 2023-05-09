#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py
and 1-pack_web_static.py tasks
that creates and distributes an archive
to the web servers web-01 and web-02
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir, basename

env.hosts = ['52.91.144.233', '54.208.166.31']
env.user = 'ubuntu'
env.ssh_key = '~/.ssh/ssh'


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')

        file_n = basename(archive_path)
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()

    if archive_path is None:
        return False
    return do_deploy(archive_path)
