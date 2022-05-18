#!/usr/bin/env python3

# Importing modules
import os
import sys
import platform # Basically only for returning the host's arch
import threading

# Importing other files
import shell
import pluginmgr
import updatemgr
import pyziniter
import api

homedir = os.path.expanduser('~')
pyver = sys.version.split(" ")

apithread = threading.Thread(target=api.connection.start, daemon=True)

# Putting "everything" together and running.
def main():
    sys.argv.extend(" ")

    # Long ass check for if the user wants to run PlugM,
    # and if so, check what PlugM command the user is running.
    if sys.argv[1] == "plugm":
        if sys.argv[2] == "help":
            pluginmgr.help()
            sys.exit(0)
        
        elif sys.argv[2] == "init":
            pluginmgr.mgrinit.init()
            sys.exit(0)

        elif sys.argv[2] == "update":
            pluginmgr.updater.update()
            sys.exit(0)
        
        elif sys.argv[2] == "search":
            pluginmgr.searcher.search(sys.argv[3])
            sys.exit(0)

        elif sys.argv[2] == "install":
            pluginmgr.installer.install(sys.argv[3])
            sys.exit(0)

        elif sys.argv[2] == "remove":
            pluginmgr.remover.remove(sys.argv[3])
            sys.exit(0)

        else:
            pluginmgr.manager.help()
            sys.exit(0)

    elif sys.argv[1] == " ":
        apithread.start()
        if os.path.isdir(pyziniter.PYZFOLDER):
            updatemgr.checker.checkForUpdates()
        else:
            pyziniter.pyzinit.initialize()
        
        if os.path.isfile(os.path.join(homedir, ".pyzrc")):
            if os.path.isfile(updatemgr.VERSIONFILE):
                print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
                shell.pyzshell.shell()        
            else:
                print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
                shell.pyzshell.shell() 

        else:
            shell.rccreator.createrc()
            shell.pyzshell.shell()
    else:
        print("Either enter a valid command or run the shell without any command!")

    return 0

pyzthread = threading.Thread(target=main)
pyzthread.start()
