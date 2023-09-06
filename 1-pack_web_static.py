#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack """

from fabric.api import local
from datetime import datetime, date
from time import strftime


def do_pack():
    """ Function to generate .tgz (archive and compress) """
    datestamp = strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        file_name = "tar -czvf versions/web_static_{}.tgz web_static/"
        local(file_name.format(datestamp))

        return file_name.format(datestamp)

    except Exception as exception:
        return None
