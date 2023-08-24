#!/usr/bin/python3
""" 0x0Keep it clean!
"""
from fabric.api import env, run, local

env.hosts = ['35.196.49.136', '34.74.70.223']
env.user = 'ubuntu'


def do_clean(number=0):
    """ Deletey `do_pack`
    As
       (str): nmost recent is kept.

    """
    number = eval(number)
    if number == 0:
        number = 1
    # local removal of tgz archives
    pipe = ' '.join(('ls -t versions/ | tail -n +{:d} |'.format(number+1),
                     'sed -e "s/^/versions\//" |',
                     'xargs rm -rf'))
    local(pipe)

    # run on server to remove outdated directories in web_static/releases/
    pipe = ' '.join(('ls -t /data/web_static/releases/ |',
                     'sed -e "/test/d" |',
                     'tail -n +{:d} |'.format(number+1),
                     'sed -e "s/^/\/data\/web_static\/releases\//" |',
                     'xargs rm -rf'))
    run(pipe)
