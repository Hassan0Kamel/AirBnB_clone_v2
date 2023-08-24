#!/usr/bin/python3
""" 0x0efore sending
"""
from fabric.api import local, env
from os import path, makedirs, listdir
from datetime import datetime


def do_pack():
    """ Gen AirBnB clone
    rep
    Retr` on failure
    """
    if not path.isdir("./versions"):
        makedirs("./versions")

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(now))

    files = listdir("./versions")
    paths = [path.join("./versions", base_name) for base_name in files]
    if len(paths) == 0:
        return None
    return max(paths, key=path.getctime)
