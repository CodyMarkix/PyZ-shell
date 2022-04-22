#!/usr/bin/env python3

# Importing modules
import os
import sys
import platform # Basically only for returning the host's arch
# Importing other files
import shell.shell as pyzshell
import shell.rccreator as rccreator
import pluginmgr.manager as plugmgr

homedir = os.path.expanduser('~')
pyver = sys.version.split(" ")

# Putting "everything" together and running.
def main():
    sys.argv.extend(" ")

    if sys.argv[1] == "plugm":
        if sys.argv[2] == "help":
            plugmgr.help()
            sys.exit(0)
        
        elif sys.argv[2] == "init":
            plugmgr.init()
            sys.exit(0)

        elif sys.argv[2] == "update":
            plugmgr.update()
            sys.exit(0)
        
        else:
            plugmgr.help()
            sys.exit(0)

    if os.path.isfile(homedir+"/.pyzrc"):
        print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
        pyzshell.shell()        
    
    else:
        rccreator.createrc()
        pyzshell.shell()

    return 0

main()