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


# Aliases for errors
eoferr = EOFError
kbdinterrupt = KeyboardInterrupt

def multipleLineCode(cmd: str):
    secondPartArr = []

    if (cmd[-1] == ":"):
        while True:
            secondPart = input("... ")
            if secondPart != "":
                secondPartArr.append(secondPart)
            
            elif secondPart == "":
                exec(cmd + " " + "; ".join(secondPartArr))
                return
    else:
        exec(cmd)
        return

# The function for running the shell
def shell():
    subprocess.call('', shell=True) # This is to make sure, the prompt isn't r/software gore material

    # Import PyZ extensions
    pluginimport.importplugin()

    # Execute the .pyzrc file
    if os.path.isfile(os.path.join(homedir, '.pyzrc')):
        with open(os.path.join(homedir, ".pyzrc")) as rcfile:
            for x in rcfile.readlines():
                exec(x)

    # The actual shell
    while True:
        try:
            inputcommand = input(f"{prompt} ")

            # Handling multiple-line things like loops and if statements
            if inputcommand.split(" ")[0] in ["for", "while", "if"]:
                multipleLineCode(inputcommand)
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
