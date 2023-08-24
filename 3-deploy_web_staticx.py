#!/usr/bin/python3
""" 0x03l deployment
"""
from fabric.api import local, env, put, run
from os import path, makedirs
from datetime import datetime

env.hosts = ['34.75.227.236', '54.234.168.105']
env.user = 'ubuntu'


def do_pack():
    """ GeneraAirBnB clone repo
    Retruns:
        (str): fune` on failure
    """
    if not path.isdir("./versions"):
        makedirs("./versions")

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(now))

    if not path.exists('./versions/web_static_{}.tgz'.format(now)):
        return None
    return path.realpath('./versions/web_static_{}.tgz'.format(now))


def do_deploy(archive_path):
    """ Distribu if all operations successful, `False` otherwise
    """
    if not path.exists(archive_path) or archive_path is None:
        return False

    f_name = path.basename(archive_path)
    d_name = f_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(d_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        f_name, d_name))
    run('rm /tmp/{}'.format(f_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(d_name) +
        '/data/web_static/releases/{}/'.format(d_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(d_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        d_name))
    return True


def deploy():
    """ First gf all operations successful, `False` otherwise
    """
    path = do_pack()
    if path is None:
        return False
    return(do_deploy(path))
