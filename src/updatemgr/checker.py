import os
import requests
import codecs
import json

def checkForUpdates():
    with open(os.environ['HOME'] +"/.local/share/pyz/version.json", "r+") as versionjson:
        remotejson = requests.get("https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json")
        localjson = json.loads(versionjson.read())

        print(json.dumps(codecs.decode(remotejson.content)), localjson)

        # if codecs.decode(remotejson.content) == versionjson.readlines():
        #     return
        # else:
        #     print(f'You have new updates available! Check the GitHub repo/your package manager.\n')