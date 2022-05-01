import os
import updatemgr.checker as checker
import pyziniter.verJSONcreate as verJSONcreate

if os.name in "nt":
    VERSIONFILE = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', 'PyZ', 'version.json')
else:
    VERSIONFILE = os.path.join(os.environ['HOME'], '.local', 'share', 'pyz', 'version.json')