# Importing modules
import os
import shutil
import re
import json

# Importing manager.py
import pluginmgr.manager as manager

def remove(package):
    for plugin in os.listdir(manager.PLUGINFOLDER):
        if plugin != "repolist.conf" and plugin != "MANIFEST":
            if re.sub(r'[^\w]', '', package) == plugin: # Filters out special characters
                print("Removing plugin...")
                shutil.rmtree(manager.PLUGINFOLDER + "/" + re.sub(r'[^\w]', '', package))

                with open(manager.INSTALLEDPKGS, 'r') as f:
                    installedPackages: dict = json.loads(f.read())

                with open(manager.INSTALLEDPKGS, 'w') as f:
                    for x in installedPackages["packages"]:
                        if x["name"] == package:
                            installedPackages["packages"].remove(x)

                    json.dump(installedPackages, f, indent=4)