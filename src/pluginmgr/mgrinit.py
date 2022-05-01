import os
import pluginmgr.manager as manager

def init():
    print("Creating plugins folder...")

    # Creates the pyz folder and plugins
    # os.mkdir(os.path.join(manager.HOMEFOLDER, ".local", "share", "pyz"))
    os.mkdir(manager.PLUGINFOLDER)
    os.mkdir(os.path.join(manager.PLUGINFOLDER, 'MANIFEST'))

    print("Creating repolist.json...")
    rplistfile = open(os.path.join(manager.PLUGINFOLDER, "repolist.conf"), 'x')
    rplistfile.close()

    print("Creating local manifest.json...")
    localmanifest = open(os.path.join(manager.PLUGINFOLDER, "MANIFEST", "mainrepo.json"), 'x')
    localmanifest.close()

    repolistfile = open(os.path.join(manager.PLUGINFOLDER, "repolist.conf"), "a+")
    if os.name in "nt":
        repolistpath = os.path.join(manager.HOMEFOLDER, "AppData", "PyZ", "plugins", "repolist.json")        
    else:
        repolistpath = os.path.join(manager.HOMEFOLDER, ".local", "share", "pyz", "plugins", "repolist.json")

    # Appends the sample repolist.conf to the end-user's repolist.conf.
    # This could be done in write-mode instead of append-mode, but whatever.
    print("Writing to repolist.conf...")
    repolistfile.write(manager.repolistjson)
    repolistfile.close()

    print("Initialized! You can now start using PlugM.")