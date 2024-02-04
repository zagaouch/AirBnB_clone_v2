#!/usr/bin/python3
from fabric.api import local, run


def do_pack(number=0):
    """deletes old archives"""
    number = int(number)
    if number < 0:
        return
    try:
        local("cd versions; ls -t | tail -n +{} | xargs -I {{}} rm {{}}"
              .format(1 if number == 0 else number + 1))
        run("cd /data/web_static/releases; ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}"
             .format(1 if number == 0 else number + 1))
    except Exception as e:
        return None
