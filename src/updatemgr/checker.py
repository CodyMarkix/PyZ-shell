import os
import requests
import json
import pluginmgr.manager as manager

def checkForUpdates():
    with open(manager.HOMEFOLDER +"/.local/share/pyz/version.json", "r+") as versionjson:
        with open('/tmp/remotejson.json', 'x') as remotejsoncr:
            remotejsoncr.close()

        with open('/tmp/remotejson.json', 'wb') as remotejson:
            remotejsonrq = requests.get("https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json")
            remotejson.write(remotejsonrq.content)
        
        localjson = json.loads(versionjson.read())
        remotejson = json.loads(open('/tmp/remotejson.json', 'r').read())

        if localjson == remotejson:
            os.remove('/tmp/remotejson.json')
            return
        else:
            print(f'You have new updates available! Check the GitHub repo/your package manager.\n')
            os.remove('/tmp/remotejson.json')