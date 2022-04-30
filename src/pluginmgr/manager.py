import os

# Sample repolist.json and plugin folder path
repolistjson = "# List of repos for PyZ plugins.\nSee man pyz-plugins.\n\n# Main repository\nhttps://github.com/CodyMarkix/PyZ-plugm-repo"
if os.name in "nt":
    HOMEFOLDER = os.environ['USERPROFILE']
    PLUGINFOLDER = os.path.join(HOMEFOLDER, 'AppData', 'Roaming', 'PyZ', 'plugins')
else:
    HOMEFOLDER = os.environ['HOME']
    PLUGINFOLDER = os.path.join(HOMEFOLDER, ".local", "share", "pyz", "plugins")

def help():
    helptext = "PlugM - PyZ's plugin manager!\n\ninit - initializes PlugM - WARNING FOR FIRST-TIME USERS, YOU WANT TO RUN THIS BEFORE ANYTHING ELSE\nupdate - Updates available plugins\n"
    print(helptext)