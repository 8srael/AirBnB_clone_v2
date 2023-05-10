#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

import os
from fabric.api import run, env

env.hosts = ['52.91.144.233', '54.208.166.31']


def do_clean(number=0):
    """
    Function that deletes out-of-date archives
    """
    number = int(number)

    if number < 0:
        return
    elif inumber in [0, 1]:
        number = 1
    else:
        number += 1

    path1 = '/data/web_static/releases'
    path2 = '/versions'

    with cd(path):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number))

    with cd(path2):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number))
