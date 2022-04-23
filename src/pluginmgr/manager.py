import os

import pluginmgr.mgrinit as mgrinit
import pluginmgr.installer as installer
import pluginmgr.searcher as searcher
import pluginmgr.updater as updater
import pluginmgr.repomgr as repomgr

repolistjson = "# List of repos for PyZ plugins.\nSee man pyz-plugins.\n\n# Main repository\nhttps://github.com/CodyMarkix/PyZ-plugm-repo"
PLUGINFOLDER = os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins")

def help():
    helptext = "PlugM - PyZ's plugin manager!\n\ninit - initializes PlugM - WARNING FOR FIRST-TIME USERS, YOU WANT TO RUN THIS BEFORE ANYTHING ELSE\nupdate - Updates available plugins\n"
    print(helptext)