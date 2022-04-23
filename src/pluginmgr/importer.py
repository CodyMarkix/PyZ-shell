#!/usr/bin/env python3
import sys
import os

def importplugin():
    sys.path.append(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    pluginlist = os.listdir(os.path.join(os.environ['HOME'], ".local", "share", "pyz", "plugins"))
    for plugin in pluginlist:
        print(plugin)