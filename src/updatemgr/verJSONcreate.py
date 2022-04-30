import json
import os
import pluginmgr.manager as manager
import updatemgr

def createVersionJSON():
    samplejsonnp = {
        "version": "0.9.5"
    }

    jsoncreating = open(os.environ['HOME']+ "/.local/share/pyz/version.json", "x")
    jsoncreating.close()

    with open(updatemgr.VERSIONFILE, "w+") as versionjson:
        json.dump(samplejsonnp, versionjson)