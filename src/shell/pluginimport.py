#!/usr/bin/env python3
import sys
import os
# import importlib.util

def importplugin():
    sys.path.append(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    pluginlist = os.listdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    for plugin in pluginlist:
        print(plugin)

        # spec = importlib.util.spec_from_file_location(plugin, plugin +"/__init__.py") # The fact that you have to do
        #  = importlib.util.module_from_spec(spec) #  all of this to import a python file
        # spec.loader.exec_module(importer) # outside the current directory angers me 
