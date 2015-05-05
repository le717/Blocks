#import subprocess


import os
from PyQt5 import uic


#uic.compileUi("ui/Blocks.ui", open("ui/Blocks.py", "wt"), execute=True, from_imports=True)
uic.compileUiDir("ui", ["execute=True", "from_imports=True"])  #, execute=True)  #, from_imports=True)
#uic.compileUiDir("ui", ["execute=True", "from_imports=True"], execute=True)  #, from_imports=True)

#subprocess.call(["pyuic5.bat", "ui/Blocks.ui", "-o", "ui/main.py"])
#subprocess.call(["pyrcc5", "ui/images.qrc", "-o", "ui/images_rc.py"])
