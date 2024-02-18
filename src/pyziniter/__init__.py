import pyziniter.pyzinit as pyzinit
import pyziniter.verJSONcreate as verJSONcreate
import os

if os.name in "nt":
    PYZFOLDER = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'PyZ')
else:
    PYZFOLDER = os.path.join(os.environ['HOME'], '.local', 'share', 'pyz')