import os
import json
import pluginmgr.manager as manager

def init():
    print("Creating plugins folder...")
    os.mkdir(manager.PLUGINFOLDER)
    os.mkdir(os.path.join(manager.PLUGINFOLDER, 'MANIFEST'))

    print("Creating repolist.json...")
    rplistfile = open(os.path.join(manager.PLUGINFOLDER, "repolist.conf"), 'x')
    rplistfile.close()

    print("Creating local manifest.json...")
    localmanifest = open(os.path.join(manager.PLUGINFOLDER, "MANIFEST", "mainrepo.json"), 'x')
    localmanifest.close()

    print("Creating installedpkg.json")
    installedpkg = open(os.path.join(manager.PLUGINFOLDER, "installedpkg.json"), 'x')
    installedpkg.close()

    repolistfile = open(os.path.join(manager.PLUGINFOLDER, "repolist.conf"), "w")
    if os.name in "nt":
        repolistpath = os.path.join(manager.HOMEFOLDER, "AppData", "PyZ", "plugins", "repolist.json")        
    else:
        repolistpath = os.path.join(manager.HOMEFOLDER, ".local", "share", "pyz", "plugins", "repolist.json")

    # Appends the sample repolist.conf to the end-user's repolist.conf.
    # This could be done in write-mode instead of append-mode, but whatever.
    print("Writing to repolist.conf...")
    breakpoint()
    repolistfile.write(manager.repolistjson)
    repolistfile.close()

    with open(os.path.join(manager.PLUGINFOLDER, 'installedpkg.json'), 'w') as f:
        json.dump({"packages": []}, f, indent=4)

    print("Initialized! You can now start using PlugM.")