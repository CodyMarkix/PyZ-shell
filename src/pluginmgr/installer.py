import sys
import pluginmgr.manager as manager

def install(package):
    try:
        if package != " ":
            with open(manager.manager.PLUGINFOLDER+"/repolist.conf") as repolist:
                for x in repolist.readlines():
                    if "#" in x:
                        pass
                    else:
                        if "https://" in x:
                            print("Valid url found!")
        else:
            raise ValueError

    except ValueError:
        print("Please include a package to install")
        sys.exit(1)
