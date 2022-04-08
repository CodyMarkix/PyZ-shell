# Importing libraries
import requests

# DO NOT CHANGE THIS VARIABLE, OTHERWISE, THE UPDATER BREAKS
REMOTEVERFILEURL = "https://raw.githubusercontent.com/CodyMarkix/PyZ-shell/master/src/updater/VERSIONSTRING"
CURRVERSION = ['version=0.9']

def check():
    remotefile = requests.get(REMOTEVERFILEURL).text
    remotefilearr = remotefile.split("\n")

    if CURRVERSION[0] == remotefilearr[0]:
        return True
    else:
        return False

    
def update():
    print("update")

print(check())