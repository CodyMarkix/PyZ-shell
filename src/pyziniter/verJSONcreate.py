import json
import os
import pluginmgr.manager as manager
import updatemgr
import pyziniter

def createVersionJSON():
    samplejsonnp = {
        "version": "1.0.0"
    }

    if (not os.path.isdir(updatemgr.VERSIONFILE[:-12])):
        os.mkdir(updatemgr.VERSIONFILE[:-12])

    jsoncreating = open(updatemgr.VERSIONFILE, "x")
    jsoncreating.close()

    with open(updatemgr.VERSIONFILE, "w+") as versionjson:
        json.dump(samplejsonnp, versionjson)