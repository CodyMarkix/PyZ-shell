import os
import requests

def checkForUpdates():
    with open(os.environ['HOME'] +"/version.json", "w+") as versionjson:
        remotejson = requests.get("https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json")
        if remotejson.content == versionjson.read():
            return
        else:
            print(f'You have new updates available! Check the GitHub repo/your package manager.\n')