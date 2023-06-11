#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

import os
from fabric.api import run, env

env.hosts = ['54.167.147.167', '100.25.117.132']


def do_clean(number=0):
    """
    Function that deletes out-of-date archives
    """
    number = int(number)

    if number < 0:
        return
    elif number == 0 or number == 1:
        number_to_keep = 1
    else:
        number_to_keep = number + 1

    path1 = '/data/web_static/releases'
    path2 = '/versions'

    with cd(path):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number_to_keep))

    with cd(path2):
        run("ls -1t | tail -n +{} | xargs rm -rf".format(number_to_keep))
