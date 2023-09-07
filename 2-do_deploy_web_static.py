#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy """

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['100.25.37.100', '100.25.193.147']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function to distribute archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        # Split archive_path using '/' taking the last elem, e archive filename
        arch_file = archive_path.split("/")[-1]

        # split filename using '.', taking elem 1, which is filename before '.'
        without_exten = arch_file.split(".")[0]

        # set path variable
        path = "/data/web_static/releases/"
        # Upload archive
        put(archive_path, "/tmp/")
        # create dir path on remote servers
        run("sudo mkdir -p {0}{1}/".format(path, without_exten))
        # decompress archive
        run("sudo tar -xzf /tmp/{0} -C {1}{2}/"
            .format(arch_file, path, without_exten))
        # delete archive from webserver
        run("sudo rm /tmp/{}".format(arch_file))
        # Move content of webstatic to target dir
        run("sudo rm -rf {0}{1}/web_static/* {0}{1}/"
            .format(path, without_exten))
        # remove web_static dir
        run("sudo rm -rf {0}{1}/web_static".format(path, without_exten))
        # Delete symbolic link
        run("sudo rm -rf /data/web_static/current")
        # create new symbolic link
        run("sudo ln -s {0}{1}/ /data/web_static/current"
            .format(path, without_exten))

        return True

    except Exception as e:
        return False
