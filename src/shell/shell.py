import termcolor # Making the prompt pretty :D
import os
import sys
import importlib.util

# Importing importer.py
spec = importlib.util.spec_from_file_location("importer", "pluginmgr/importer.py") # The fact that you have to do
importer = importlib.util.module_from_spec(spec) #  all of this to import a python file
spec.loader.exec_module(importer) # outside the current directory angers me 

homedir = os.path.expanduser('~')
rcfilepath = homedir +"/.pyzrc"

prompt = "fallback prompt >" # Fallback prompt, in case there is no prompt in the .pyzrc file

# Aliases for errors
eoferr = EOFError
kbdinterrupt = KeyboardInterrupt

# The function for running the shell
def shell():
    # Execute the .pyzrc file
    rcfile = open(rcfilepath, "r")
    for x in rcfile:
        exec(x)

    # Import PyZ extensions - not functional for now
    # importer.importplugin()

    # The actual shell
    while True:
        try:
            inputcommand = input(prompt +" ")

            # Handling multiple-line things like loops and if statements
            for x in inputcommand.split():
                if x == "for":
                    forloop = []
                    forloop.append(inputcommand)
                    forloop.append(" ")

                    while True:
                        forcode = input("... ")
                        
                        if forcode != "":
                            forloop.append(forcode)
                            forloop.append("; ")
                        
                        elif forcode == "":
                            print(''.join(forloop))
                            exec(''.join(forloop))
                            break
                elif inputcommand == "exit()":
                    sys.exit(0)
                else:
                    exec(inputcommand)
        
        # Ignoring KeyboardInterrupts (Ctrl+C)
        except kbdinterrupt:
            print("KeyboardInterrupt")
            continue
        
        # Exiting the shell (Ctrl+D)
        except eoferr:
            print("")
            return

