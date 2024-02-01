#!/usr/bin/python3
# Fabfile for distributing an archive to a web server.
import os.path
from fabric.api import env, put, run

env.hosts = ["54.160.85.72", "35.175.132.106"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        False if the file doesn't exist at archive_path or an error occurs, otherwise True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    
    # Extract file and name from the path
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to the server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    # Remove existing release directory, create new directory, and extract archive
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False

    # Clean up temporary archive file
    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    # Move files from extracted folder to release folder
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    
    # Remove the web_static symbolic link
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False

    # Remove the current symbolic link
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # Create a new symbolic link to the latest release
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False

    return True
