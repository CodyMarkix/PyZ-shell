import os
import pyziniter

def initialize():
    os.mkdir(pyziniter.PYZFOLDER)
    pyziniter.verJSONcreate.createVersionJSON()