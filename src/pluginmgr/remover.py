# Importing modules
import os
import shutil
import re

# Importing manager.py
import pluginmgr.manager as manager

def remove(package):
    for plugin in os.listdir(manager.PLUGINFOLDER):
        if plugin != "repolist.conf" and plugin != "MANIFEST":
            if re.sub(r'[^\w]', '', package) == plugin:
                print("Removing plugin...")
                shutil.rmtree(manager.PLUGINFOLDER + "/" + re.sub(r'[^\w]', '', package))