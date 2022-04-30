import json
import os
import pluginmgr.manager as manager

def createVersionJSON():
    samplejsonnp = {
        "version": "0.9.5"
    }

    # jsoncreating = open(os.environ['HOME']+ "/.local/share/pyz/version.json", "x")
    # jsoncreating.close()

    with open(manager.HOMEFOLDER +"/.local/share/pyz/version.json", "w+") as versionjson:
        json.dump(samplejsonnp, versionjson)