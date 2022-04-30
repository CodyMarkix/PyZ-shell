import os
import requests

def checkForUpdates():
    with open(os.environ['HOME'] +"/.local/share/pyz/version.json", "w+") as versionjson:
        remotejson = requests.get("https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json")
        print(remotejson.content)
        print(versionjson.read())

        if remotejson.content == versionjson.readlines():
            return
        else:
            print(f'You have new updates available! Check the GitHub repo/your package manager.\n')