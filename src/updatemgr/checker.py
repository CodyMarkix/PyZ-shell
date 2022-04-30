import os
import requests
import json
import pluginmgr.manager as manager
import updatemgr

if os.name in "nt":
    tmplocation = os.path.join(os.environ['temp'], "remotejson.json")
else:
    tmplocation = os.path.join('/', 'tmp', 'remotejson.json')

def checkForUpdates():
    with open(updatemgr.VERSIONFILE, "r+") as versionjson:
        with open(tmplocation, 'x') as remotejsoncr:
            remotejsoncr.close()

        with open(tmplocation, 'wb') as remotejson:
            remotejsonrq = requests.get("https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/version.json")
            remotejson.write(remotejsonrq.content)
        
        localjson = json.loads(versionjson.read())
        remotejson = json.loads(open(tmplocation, 'r').read())

        if localjson == remotejson:
            os.remove(tmplocation)
            return
        else:
            print(f'You have new updates available! Check the GitHub repo/your package manager.\n')
            os.remove(tmplocation)