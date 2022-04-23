import os
import requests
import sys

repolistjson = "# List of repos for PyZ plugins.\nSee man pyz-plugins.\n\n# Main repository\nhttps://github.com/CodyMarkix/PyZ-plugm-repo"
PLUGINFOLDER = os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins")

def init():
    print("Creating plugins folder...")

    os.mkdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz"))
    os.mkdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))

    print("Creating repolist.json...")
    rplistfile = open(PLUGINFOLDER +"/repolist.conf", 'x')
    rplistfile.close()

    repolistfile = open(PLUGINFOLDER +"/repolist.conf", "a+")
    repolistpath = os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins", "repolist.json")

    print("Writing to repolist.conf...")
    repolistfile.write(repolistjson)
    repolistfile.close()

    print("Initialized!")

def help():
    helptext = "PlugM - PyZ's plugin manager!\n\ninit - initializes PlugM - WARNING FOR FIRST-TIME USERS, YOU WANT TO RUN THIS BEFORE ANYTHING ELSE\nupdate - Updates available plugins\n"
    print(helptext)

def update():
    repolistfile = open(PLUGINFOLDER +"/repolist.conf", "r")
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
                    print(requests.get(m +"/raw/master/make.ps1").content)
                else:
                    print("Couldn't connect to mirror!")
                    sys.exit(0)

                print("Updated!")