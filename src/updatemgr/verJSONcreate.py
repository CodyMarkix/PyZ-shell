import json
import os

def createVersionJSON():
    samplejsonnp = {
        "version": "0.9.5"
    }

    # jsoncreating = open(os.environ['HOME']+ "/.local/share/pyz/version.json", "x")
    # jsoncreating.close()

    with open(os.environ['HOME'] +"/version.json", "w+") as versionjson:
        json.dump(samplejsonnp, versionjson)