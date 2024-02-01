#!/usr/bin/python3
from fabric.api import run, put, env, sudo
from os.path import exists
from datetime import datetime


env.hosts = ['100.26.178.191', '54.146.58.176']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """deploys archived files to server"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        webstatic = '/data/web_static/releases/{}'
        release_folder = webstatic.format(archive_filename.split('.')[0])
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename,
                                                 release_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        run('sudo mv {}/web_static/* {}'.format(release_folder,
                                                release_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(release_folder))
        return True
    except Exception as e:
        return False
