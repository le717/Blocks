#! usr/bin/env python3.3-32
# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    Blocks - Island Xtreme Stunts Minigame Level Editor
    Created 2013 Triangle717
    <http://Triangle717.WordPress.com/>

    Blocks is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Blocks is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Blocks. If not, see <http://www.gnu.org/licenses/>.

"""
# Blocks setup script using cx_Freeze.
# Taken from https://github.com/Lyrositor/EBPatcher
# and https://github.com/JrMasterModelBuilder/JAM-Extractor
# With changes by Triangle717

from cx_Freeze import (setup, Executable)
import sys
import os

from constants import (majver, minver)
import files

# Append build command to command-line arguments.
# Just type "python setup.py" and it will freeze
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

# Do we hide the console window, or not?
base = None

# This is being frozen on Windows
if sys.platform == "win32":

    # On Windows, yes, hide the console window
    base = "Win32GUI"

    # This is x86 Python
    if sys.maxsize == 2147483647:
        destfolder = os.path.join("Freeze", "Windows")

    # This is x64 Python
    else:
        input('''\n64-bit binaries are not frozen.
    Please freeze Blocks using 32-bit Python 3.3.''')
        raise SystemExit(0)

# This is being frozen on Mac OS X
elif sys.platform == "darwin":
    destfolder = os.path.join("Freeze", "Mac OS X")

# This is some flavor of Linux
else:
    destfolder = os.path.join("Freeze", "Linux")

# Create the freeze path if it doesn't exist
if not os.path.exists(destfolder):
    os.makedirs(destfolder)

# # Write RunAsAdmin.cfg  and Blocks.bat on Windows only
if base is not None:
    files.Write(destfolder)

# Copy required files
build_exe_options = {"build_exe": destfolder,
                    "icon": "Media/Blocks.ico",
                    "include_files": [
                    "LICENSE.txt",
                    "LICENSE.RunAsAdmin.txt",
                    "Media/Blocks.ico",
                    "Media/Blocks.gif",
                    "Documentation/Changelog.md",
                    "Documentation/Format-Details.md",
                    "Documentation/Tutorial.md"]
                    }

setup(
    name="Blocks",
    version="{0}{1}".format(majver, minver),
    author="Triangle717",
    description="Island Xtreme Stunts Minigame Level Editor",
    license="GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("Blocks.pyw",
        targetName="Blocks.exe", base=base)]
)