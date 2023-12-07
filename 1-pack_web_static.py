#!/usr/bin/python3
"""  Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function
do_pack.
Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions
(your function should create this folder if it doesn’t exist)
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive
has been correctly generated. Otherwise, it should return None
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ This defines a function named do_pack."""

    """ Generates a unique file name for the tarball based
    on the current date and time.
    """
    d = datetime.now()
    fp = f"web_static_{d.year}{d.month}{d.day}{d.hour}{d.minute}{d.second}.tgz"

    """ Checks if the "versions" directory exists. If not, it attempts
    to create it using the local function from Fabric.
    """
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    """ Changes the current working directory to "versions"
    using the cd context manager.
    Creates a tarball (tar -czvf)
    """
    if local(f"tar -cvzf {fp} web_static").failed is True:
            return None
    return fp
