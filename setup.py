#! /usr/bin/python3.4-32
# -*- coding: utf-8 -*-
"""Blocks - Island Xtreme Stunts Minigame Level Editor.

Created 2013-2015 Triangle717
<http://Triangle717.WordPress.com/>

Blocks is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Blocks is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Blocks. If not, see <http://www.gnu.org/licenses/>.

"""

import os
import sys
import subprocess
from cx_Freeze import (setup, Executable)

import constants as const
from Tools.bin import (copyfiles, runasadmin)
base = None

# Only compile GUI on full build
if sys.argv[1] == "build":
    print("Generating GUI resources")
    from PyQt5 import uic
    uic.compileUiDir("ui")
    subprocess.call(["pyrcc5", "ui/images.qrc", "-o", "images_rc.py"])

# Windows
if sys.platform == "win32":
    base = "Win32GUI"

    # This is x86 Python
    if sys.maxsize < 2 ** 32:
        destFolder = os.path.join("bin", "Windows")

    # Do not freeze on x64 Python
    else:
        input("""\n64-bit binaries are not frozen.
    Please freeze Blocks using 32-bit Python 3.3.""")
        raise SystemExit(0)

# Mac OS X
elif sys.platform == "darwin":
    destFolder = os.path.join("bin", "Mac OS X")

# Linux
else:
    destFolder = os.path.join("bin", "Linux")

# Create the freeze path if it doesn't exist
if not os.path.exists(destFolder):
    os.makedirs(destFolder)

# Copy required files
build_exe_options = {
    "build_exe": destFolder,
    "create_shared_zip": True,
    "compressed": True,
    "optimize": 2,
    "icon": "Media/Blocks.ico"
}

setup(
    name=const.appName,
    version=const.version,
    author=const.creator,
    description=const.appName,
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("Blocks.pyw",
                 targetName="Blocks.exe", base=base)]
)

# Copy any required files/directories
filesForCopying = [
    "LICENSE",
    "LICENSE.RunAsAdmin.txt",
    "README.md",
    os.path.join("Media", "Blocks.png"),
    os.path.join("Media", "Blocks.ico"),
    os.path.join("Documentation", "Changelog.md"),
    os.path.join("Documentation", "Format-Details.md"),
    os.path.join("Documentation", "Tutorial.md")
]
copyfiles.main(filesForCopying, destFolder)

# Add RunAsAdmin config
if sys.platform == "win32":
    runasadmin.main(destFolder)
