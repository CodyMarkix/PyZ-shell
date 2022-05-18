import termcolor # Making the prompt pretty :D
import os
import shell.pluginimport as pluginimport
import api
import subprocess
import sys

# Path for the pyzrc file
homedir = os.path.expanduser('~')
rcfilepath = homedir +"/.pyzrc"

prompt = "fallback prompt >" # Fallback prompt, in case there is no prompt in the .pyzrc file
inputcommand = None

# Aliases for errors
eoferr = EOFError
kbdinterrupt = KeyboardInterrupt

def forLoop():
    forloop2 = []

    while True:
        forcode = input("... ")
        
        if forcode != "":
            forloop2.append(forcode)
        
        elif forcode == "":
            # codenovar = forloop.pop()
            # testvar = '; '.join(forloop)
            samplevar = inputcommand + " " + "; ".join(forloop2)
            exec(inputcommand + " " + "; ".join(forloop2))
            return

def whileLoop():
    whileloop2 = []

    while True:
        whilecode = input("... ")
        
        if whilecode != "":
            whileloop2.append(whilecode)
        
        elif whilecode == "":
            exec(inputcommand + " " + "; ".join(whileloop2))
            return

def ifStatement():
    ifcode2 = []

    while True:
        ifcode = input("... ")
        
        if ifcode != "":
            ifcode2.append(ifcode)
        
        elif ifcode == "":
            exec(inputcommand + " " + "; ".join(ifcode2))
            return


# The function for running the shell
def shell():
    subprocess.call('', shell=True) # This is to make sure, the prompt isn't r/software gore material

    # Execute the .pyzrc file
    if os.path.isfile(os.path.join(homedir, '.pyzrc')):
        # getShortPath()
        rcfile = open(rcfilepath, "r")
        for x in rcfile:
            exec(x)

    # Import PyZ extensions
    pluginimport.importplugin()

    # The actual shell
    while True:
        try:
            inputcommand = input(f"{prompt} ")

            # Handling multiple-line things like loops and if statements
            if inputcommand.split(" ")[0] == "for":
                forLoop()
            elif inputcommand.split(" ")[0] == "while":
                whileLoop()
            elif inputcommand.split(" ")[0] == "if":
                ifStatement()
            elif inputcommand == "exit()":
                api.connection.stop()
                sys.exit(0)
            else:
                exec(inputcommand)

        # Ignoring KeyboardInterrupts (Ctrl+C)
        except kbdinterrupt:
            print("\nKeyboardInterrupt")
            continue
        
        # Exiting the shell (Ctrl+D)
        except eoferr:
            api.connection.stop()
            print("")
            return

        except Exception as err:
            print(f'{err.__class__.__name__}: {err}')
            continue
