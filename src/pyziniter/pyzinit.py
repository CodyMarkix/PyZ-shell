import os
import pyziniter

def initialize():
    pyzfolder = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'PyZ') if os.name == 'nt' else os.path.join(os.environ['HOME'], '.local', 'share', 'pyz')
    pyziniter.verJSONcreate.createVersionJSON()