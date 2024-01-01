#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""
import os
from fabric.api import env, hosts, sudo, put


env.hosts = ['54.146.76.48', '100.25.192.141']
def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    
    # upload archive to server
    if put(archive_path, '/tmp/').failed:
        return False
    
    # extract the file name
    name = archive_path.split('/')[-1].split('.')[0]

    path = f"/data/web_static/releases/{name}"

    # create the directory
    if sudo(f'mkdir -p {path}').failed:
        return False

    # uncompress the archive
    if sudo(f"tar -xzf /tmp/{archive_path.split('/')[-1]} -C {path}").failed:
        return False
    
    # delete the archive from the webserver
    if sudo(f"rm /tmp/{archive_path.split('/')[-1]}").failed:
        return False

    # delete the symbolic link
    if sudo("rm /data/web_static/current").failed:
        return False

    # create a symbolic link
    if sudo(f"ln -s {path} /data/web_static/current").failed:
        return False
    return True

