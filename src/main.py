#!/usr/bin/env python3

# Importing modules
import os
import sys
import platform # Basically only for returning the host's arch

# Importing other files
import shell.shell as pyzshell
import shell.rccreator as rccreator

homedir = os.path.expanduser('~')
pyver = sys.version.split(" ")

# Putting "everything" together and running.
def main():
    
    if os.path.isfile(homedir+"/.pyzrc"):
        print("PyZ - A custom shell in Python, for Python.\nPython ver: "+ pyver[0] +" ("+ platform.architecture()[0] +")")
        pyzshell.shell()        
    
    else:
        rccreator.createrc()
        pyzshell.shell()

    return 0

main()