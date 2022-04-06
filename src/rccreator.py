import os

# Creating the rc file

homedir = os.path.expanduser('~')
rcfilepath = homedir +"/.pyzrc"

def createrc():
    while True:
        creatercprompt = input("There appears to be no .pyzrc file.\nDo you want to create one? [Y/n] ")
        
        if creatercprompt == "y" or creatercprompt == "Y":
            break
        elif creatercprompt == "n" or creatercprompt == "N":
            return
        else:
            break
    
    rcfile = open(rcfilepath, "w+")
    samplerc = "#!/usr/bin/env python3\n\n# PyZ's .rc file - In this file you can do things like customize your prompt,\n# execute python code when opening your shell, etc.\n# DO NOT MODIFY THESE NOTES OTHERWISE, THE CODE WILL MAYBE BREAK\n\n# The prompt that is shown in the console, something like $PS1 in bash.\n# By default, the prompt utilizes python and the termcolor module.\n# However, since the prompt is basically a python string, you can basically have it almost anything\n# global prompt; prompt = \"[ \"+ termcolor.colored(os.getcwd(), \"green\") + \" ]\"+ termcolor.colored(\" >\", \"blue\")"
    
    rcfile.write(samplerc)
    rcfile.close
    
    return