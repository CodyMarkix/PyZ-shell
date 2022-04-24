import sys
import requests
import json
import os
from zipfile import ZipFile

import pluginmgr.manager as manager

def getRepo():
    with open(manager.PLUGINFOLDER+"/repolist.conf") as repolist:
        for x in repolist.readlines():
            if "#" in x:
                pass
            else:
                if "https://" in x:
                    return x

def install(package):
    try:
        if package != " ":                            
            validrepobrokey = getRepo() # Contains an \n character at the end, that's doo doo
            validrepo = validrepobrokey[:-1] # and we need to remove it
            
            with open(manager.PLUGINFOLDER+"/MANIFEST/mainrepo.json") as manifestfile:
                parsedmanifest = json.load(manifestfile)

            for x in parsedmanifest["plugins"]:
                if x["name"] == package:
                    validzip = x["file"]
                    break
                else:
                    continue
            
            zipparams = {'raw': 'true'}
            zipurl = requests.get(validrepo +"/blob/master/"+ validzip, params=zipparams)
            
            if zipurl.status_code == 200:
                with open(manager.PLUGINFOLDER +"/"+ validzip, "x") as ziptocreate:
                    ziptocreate.close()
                
                with open(manager.PLUGINFOLDER +"/"+ validzip, "wb") as zipfile:
                    zipfile.write(zipurl.content)
                    zipname = zipfile.name
                    zipfile.close()
                
                extractzip = ZipFile(zipname)
                extractzip.extractall(path=manager.PLUGINFOLDER)

                os.remove(manager.PLUGINFOLDER +"/"+ validzip)
            else:
                print("Error! Repository returned code "+ str(zipurl.status_code) +".")
                    

        else:
            raise ValueError
            
    except ValueError:
        print("Please include a package to install")
        sys.exit(1)