import json
import os
import pluginmgr.manager as manager
import updatemgr
import pyziniter

def createVersionJSON():
    samplejsonnp = {
        "version": "1.0.0"
    }

    jsoncreating = open(updatemgr.VERSIONFILE, "x")
    jsoncreating.close()

    with open(updatemgr.VERSIONFILE, "w+") as versionjson:
        json.dump(samplejsonnp, versionjson)