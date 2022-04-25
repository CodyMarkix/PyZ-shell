import os
import pluginmgr.manager as manager

def init():
    print("Creating plugins folder...")

    # Creates the pyz folder and plugins
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

    # Appends the sample repolist.conf to the end-user's repolist.conf.
    # This could be done in write-mode instead of append-mode, but whatever.
    print("Writing to repolist.conf...")
    repolistfile.write(manager.repolistjson)
    repolistfile.close()

    print("Initialized! You can now start using PlugM.")