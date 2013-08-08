#! python3.3-32
# -*- coding: utf-8 -*-
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

from cx_Freeze import setup, Executable
import sys
import os

# Append build command to command-line arguments.
# Just type "python setup.py" and it will freeze
if len(sys.argv) == 1:
    sys.argv[1:] = ["build"]

if sys.maxsize == 2147483647:
    destfolder = os.path.join("Freeze", "Windows")
else:
    input('''\n64-bit binaries are not frozen.
Please freeze Blocks using 32-bit Python 3.3.''')
    raise SystemExit(0)

# Write the required RunAsAdmin cfg file
with open(os.path.join(destfolder, "RunAsAdmin.cfg"), "wt") as f:
    f.write("Blocks.exe")

build_exe_options = {"build_exe": destfolder,
                     "icon": "Media/Blocks.ico",
                     "include_files": [
                     "LICENSE.txt",
                     "Media/Blocks.ico",
                     "Media/BlocksIcon.gif",
                     "Documentation/Changelog.md",
                     "Documentation/Format-Details.md",
                     "Documentation/Tutorial.md"]
                     }

setup(
    name="Blocks",
    version="0.8.6",
    author="Triangle717",
    description="Island Xtreme Stunts Minigame Level Editor",
    license="GNU GPLv3",
    options={"build_exe": build_exe_options},
    executables=[Executable("Blocks.pyw",
        targetName="Blocks.exe", base="Win32GUI")]
)