import os
import pyziniter

def initialize():
    pyzfolder = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'PyZ') if os.name == 'nt' else os.path.join(os.environ['HOMe'], '.local', 'share', 'pyz')

    os.mkdir(pyzfolder)
    pyziniter.verJSONcreate.createVersionJSON()