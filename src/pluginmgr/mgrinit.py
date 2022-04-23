import os
import pluginmgr.manager as manager

def init():
    print("Creating plugins folder...")

    os.mkdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz"))
    os.mkdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))

    print("Creating repolist.json...")
    rplistfile = open(manager.PLUGINFOLDER +"/repolist.conf", 'x')
    rplistfile.close()

    print("Creating local manifest.json...")
    localmanifest = open(manager.PLUGINFOLDER +"/MANIFEST/mainrepo.json", 'x')
    localmanifest.close()

    repolistfile = open(manager.PLUGINFOLDER +"/repolist.conf", "a+")
    repolistpath = os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins", "repolist.json")

    print("Writing to repolist.conf...")
    repolistfile.write(manager.repolistjson)
    repolistfile.close()

    print("Initialized! You can now start using PlugM.")