import sys
import pluginmgr.manager as manager

def addRepo(repository):
    try:
        if repository != " ":
            with open(manager.PLUGINFOLDER+"/repolist.conf", "a+") as repolist:
                repolist.write(repository)
        else:
            raise ValueError

    except ValueError:
        print("Enter a repository to install!")
        sys.exit(0)

