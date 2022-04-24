#!/usr/bin/env python3
import sys
import os
import importlib

def importplugin():
    sys.path.append(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    pluginlist = os.listdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    installedplugs = len(pluginlist)-2
    i = 0
    
    for plugin in pluginlist:
        if plugin != "repolist.conf":
            if i < installedplugs:
                importlib.import_module(plugin +".__init__")
                i += 1                
            else:
                pass
        else:
            continue