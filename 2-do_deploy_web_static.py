#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""
from os.path import exists
from fabric.api import env, hosts, sudo, put


env.hosts = ['54.146.76.48', '100.25.192.141']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        archive_fn = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/" + archive_fn.split(".")[0]
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_fn, folder_name))

        # Remove the archive from the web server
        run("sudo rm -rf /tmp/{}".format(archive_fn))

        # Delete the symbolic link /data/web_static/current
        current_link_path = "/data/web_static/current"
        if exists(current_link_path):
            sudo("rm -rf {}".format(current_link_path))

        # Create a new symbolic link to the new version of the code
        sudo("ln -s {} {}".format(folder_name, current_link_path))

        return True

    except Exception:
        return False
