import termcolor # Making the prompt pretty :D
import os
import sys
import shell.pluginimport as pluginimport

# Path for the pyzrc file
homedir = os.path.expanduser('~')
rcfilepath = homedir +"/.pyzrc"

prompt = "fallback prompt >" # Fallback prompt, in case there is no prompt in the .pyzrc file

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
            exec(inputcommand + " " + "; ".join(forloop2))
            return

def whileLoop():
    whileloop2 = []

    while True:
        whilecode = input("... ")
        
        if whilecode != "":
            whileloop2.append(whilecode)
        
        elif whilecode == "":
            # codenovar = forloop.pop()
            # testvar = '; '.join(forloop)
            exec(inputcommand + " " + "; ".join(whileloop2))
            return

# The function for running the shell
def shell():
    # Execute the .pyzrc file
    rcfile = open(rcfilepath, "r")
    for x in rcfile:
        exec(x)

    # Import PyZ extensions
    pluginimport.importplugin()

    # The actual shell
    while True:
        try:
            global inputcommand
            inputcommand = input(prompt +" ")

            # Handling multiple-line things like loops and if statements
            if inputcommand.split(" ")[0] == "for":
                forLoop()
            elif inputcommand.split(" ")[0] == "while":
                whileLoop()
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

