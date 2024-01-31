#!/usr/bin/python3
#fab file to pack and deploy

from fabric.api import local, env, run
from datetime import datetime

env.hosts = ['100.26.178.191', '54.146.58.176']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'

def do_pack():
    """pack web static"""
    try:

        local('mkdir -p versions')
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_{}.tgz'.format(timestamp)
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return local('tar -cvzf versions/{} web_static'.format(archive_name))
    except Exception as e:
        return None
def do_deploy():
    """deploys and unpacks"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        webstatic = '/data/web_static/releases/{}'
        release_folder = webstatic.format(archive_filename.split('.')[0])
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        run('sudo mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(release_folder))
        return True
    except Exception as e:
        return False
def deploy():
    """packs and deploys"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

