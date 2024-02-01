#!/usr/bin/python3
<<<<<<< HEAD
# Fabfile to generate a .tgz archive from the contents of web_static.
=======
# Fabfile to generates a .tgz archive from the contents of web_static.
>>>>>>> 73551a09623cbc28dea49449990f143215404231
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
<<<<<<< HEAD
    """Create a tar gzipped archive of the web_static directory."""
    # Get current UTC time
    dt = datetime.utcnow()
    
    # Define file name with timestamp
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)
    
    # Create 'versions' directory if it doesn't exist
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    
    # Create tar gzipped archive
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    
    return file_name
=======
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
>>>>>>> 73551a09623cbc28dea49449990f143215404231
