import requests
import codecs
import sys
import pluginmgr.manager as manager

def update():
    repolistfile = open(manager.PLUGINFOLDER +"/repolist.conf", "r")
    mirrors = repolistfile.read()

    repolistarr = mirrors.split("\n")
    for m in repolistarr:
        if "https://" in m:
            if "#" in m:
                continue
            else:
                print("Connecting to "+ m +"...")

                mirrorrequest = requests.get(m)
                if mirrorrequest.status_code == 200:
                    print("Connected to "+ m +"!")
                    remotemanifest = requests.get(m +"/raw/master/MANIFEST.json").content
                    remotemanifeststr = codecs.decode(remotemanifest)
                    
                    localmanifest = open(manager.PLUGINFOLDER+"/MANIFEST/mainrepo.json", "w+")
                    localmanifest.write(remotemanifeststr)
                    localmanifest.close()

                else:
                    print("Couldn't connect to mirror!")
                    sys.exit(0)

                print("Updated!")