def setAlias(alias, cmd):
    try:
        if alias == None or cmd == None or alias == None and cmd == None:
            raise ValueError
        else:
            alias = cmd
    except ValueError:
        print("Setting alias failed! No alias/cmd found")