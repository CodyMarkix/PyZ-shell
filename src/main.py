#!/usr/bin/env python3

# Importing modules
import os
import sys
import platform # Basically only for returning the host's arch

# Importing other files
import shell.shell as pyzshell
import shell.rccreator as rccreator
import pluginmgr.manager as plugmgr
import updatemgr.checker as checker
import updatemgr.verJSONcreate as verJSONcreate

homedir = os.path.expanduser('~')
pyver = sys.version.split(" ")

# Putting "everything" together and running.
def main():
    sys.argv.extend(" ")


    # Long ass check for if the user wants to run PlugM,
    # and if so, check what PlugM command the user is running.
    if sys.argv[1] == "plugm":
        if sys.argv[2] == "help":
            plugmgr.help()
            sys.exit(0)
        
        elif sys.argv[2] == "init":
            plugmgr.mgrinit.init()
            sys.exit(0)

        elif sys.argv[2] == "update":
            plugmgr.updater.update()
            sys.exit(0)
        
        elif sys.argv[2] == "search":
            plugmgr.searcher.search(sys.argv[3])
            sys.exit(0)

        elif sys.argv[2] == "install":
            plugmgr.installer.install(sys.argv[3])
            sys.exit(0)

        elif sys.argv[2] == "remove":
            plugmgr.remover.remove(sys.argv[3])
            sys.exit(0)

        else:
            plugmgr.help()
            sys.exit(0)

    elif sys.argv[1] == " ":
        checker.checkForUpdates()
        
        if os.path.isfile(homedir+"/.pyzrc"):
            if os.path.isfile(plugmgr.PLUGINFOLDER +"/version.json"):
                print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
                pyzshell.shell()        
            else:
                verJSONcreate.createVersionJSON()
                print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
                pyzshell.shell() 

        else:
            rccreator.createrc()
            pyzshell.shell()
    else:
        print("Either enter a valid command or run the shell without any command!")

    return 0

main()