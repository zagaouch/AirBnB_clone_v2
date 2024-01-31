#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """function to archive contents of web static"""
    try:
        
        local('mkdir -p versions')
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_{}.tgz'.format(timestamp)
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return local('tar -cvzf versions/{} web_static'.format(archive_name))
    except Exception as e:
        return None
