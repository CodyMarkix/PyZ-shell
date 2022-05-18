import shell.shell as shell

def chPrompt(newprompt):
    shell.prompt = newprompt
    return None

def getPrompt():
    return shell.prompt