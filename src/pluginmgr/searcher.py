import sys
import json
import termcolor
import pluginmgr.manager as manager

def search(term):
    try:
        if term != " ": 
            with open(manager.PLUGINFOLDER+"/MANIFEST/mainrepo.json") as manifestfile:
                parsedmanifest = json.load(manifestfile)

            for x in parsedmanifest["plugins"]:
                if term in x["name"]:
                    print("["+termcolor.colored(x["name"], 'green')+"]"+"\nVersion: "+x["version"]+"\nDescription: "+x["description"])
        else:
            raise ValueError

    except ValueError:
        print("Please enter a valid search term!")
        sys.exit(1)