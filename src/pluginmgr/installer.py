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
    try:
        if package != " ":                      
            validrepo = getRepo()
            
            with open(manager.PLUGINFOLDER+"/MANIFEST/mainrepo.json") as manifestfile:
                parsedmanifest = json.load(manifestfile)

            for x in parsedmanifest["plugins"]: # For every package in the mainrepo.json manifest
                if x["name"] == package: # If the package's name matches the user inputted package
                    validzip = x["file"] # Declare a variable the package's zip file name
                    break
                else:
                    continue
            
            zipparams = {'raw': 'true'}
            zipurl = requests.get(validrepo +"/blob/master/"+ validzip, params=zipparams) # Send a request to the main repo for the zip file the user requested
            
            # If the repository returns 200
            if zipurl.status_code == 200:
                with open(manager.PLUGINFOLDER +"/"+ validzip, "x") as ziptocreate:
                    ziptocreate.close() # Create a zip file
                
                with open(manager.PLUGINFOLDER +"/"+ validzip, "wb") as zipfile: # Download the zip file from the repository
                    zipfile.write(zipurl.content) # And write it to the newly created zip file
                    zipname = zipfile.name
                    zipfile.close()
                
                extractzip = ZipFile(zipname)
                extractzip.extractall(path=manager.PLUGINFOLDER)

                os.remove(os.path.join(manager.PLUGINFOLDER, validzip))
            else:
                print(f"Error! Repository returned code {str(zipurl.status_code)}.") # Else, throw a hissy fit about the repository not returning 200
                sys.exit(0)

        else:
            raise ValueError
            
    except ValueError:
        print("Please include a package to install")
        sys.exit(1)