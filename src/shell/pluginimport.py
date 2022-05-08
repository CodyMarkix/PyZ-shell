#!/usr/bin/env python3
import sys
import os
import importlib
import pluginmgr.manager as manager

def importplugin():
    sys.path.append(manager.PLUGINFOLDER)
    
    if os.path.isdir(manager.PLUGINFOLDER):
        pluginlist = os.listdir(manager.PLUGINFOLDER)
        installedplugs = len(pluginlist)-2
        i = 0
        
        # This is probably garbage code but I don't want to break my program any further.
        for plugin in pluginlist:
            if plugin != "repolist.conf" and plugin != "MANIFEST":
                if i < installedplugs:
                    importlib.import_module(plugin)
                    i += 1                
                else:
                    pass
            else:
                continue
    else:
        pass