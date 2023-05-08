#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        tgz_path = "versions/web_static_{}.tgz".format()
        local("tar -cvzf {} web_static".format(tgz_path))
        return tgz_path
    except Exception:
        return None
