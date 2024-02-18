import sys
import requests
import json
import os
from zipfile import ZipFile

import pluginmgr.manager as manager

def getRepo():
    # Reads the hard-coded repolist.conf file
    with open(manager.PLUGINFOLDER+"/repolist.conf") as repolist:
        for x in repolist.readlines(): # For every line in repolist.conf
            if "#" in x: # If it's a comment, do nothing
                pass
            else:
                if "https://" in x: # Otherwise, if it contains https://, returns the repo.
                    return x

def install(package):
    # try:
        if package != " ":                      
            validrepo = getRepo() or "https://github.com/CodyMarkix/PyZ-plugin-repo" # Fallback to this repo
            
            with open(manager.PLUGINFOLDER+"/MANIFEST/mainrepo.json") as manifestfile:
                parsedmanifest = json.load(manifestfile)

            for x in parsedmanifest["plugins"]: # For every package in the mainrepo.json manifest
                if x["name"] == package: # If the package's name matches the user inputted package
                    validzip = x # Declare a variable the package info
                    break
                else:
                    continue
            
            zipparams = {'raw': 'true'}
            zipurl = requests.get(validrepo +"/blob/master/"+ validzip["file"], params=zipparams) # Send a request to the main repo for the zip file the user requested
            
            # If the repository returns 200
            if zipurl.status_code == 200:
                with open(manager.PLUGINFOLDER +"/"+ validzip["file"], "x") as ziptocreate:
                    ziptocreate.close() # Create a zip file
                
                with open(manager.PLUGINFOLDER +"/"+ validzip["file"], "wb") as zipfile: # Download the zip file from the repository
                    zipfile.write(zipurl.content) # And write it to the newly created zip file
                    zipname = zipfile.name
                    zipfile.close()
                
                extractzip = ZipFile(zipname)
                extractzip.extractall(path=manager.PLUGINFOLDER)

                # os.remove(os.path.join(manager.PLUGINFOLDER, validzip["file"]))

                with open(os.path.join(manager.PLUGINFOLDER, "installedpkg.json"), 'r') as installedPkgFile:
                    config = json.loads(installedPkgFile.read())
                    installedPackages: list[dict] = config["packages"]

                with open(os.path.join(manager.PLUGINFOLDER, "installedpkg.json"), 'w') as installedPkgFile:
                    if validzip not in installedPackages:
                        installedPackages.append(validzip)
                    else:
                        for x in installedPackages:
                            if x["name"] == validzip["name"]:
                                x = validzip
                        
                    config.update({"packages": installedPackages})
                    json.dump(config, installedPkgFile, indent=4)

            else:
                print(f"Error! Repository returned code {str(zipurl.status_code)}.") # Else, throw a hissy fit about the repository not returning 200
                sys.exit(0)

        else:
            raise ValueError
            
    # except ValueError:
    #     print("Please include a package to install")
    #     sys.exit(1)