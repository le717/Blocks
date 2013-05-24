#! python3
# -*- coding: utf-8 -*-
"""
    Blocks - Island Xtreme Stunts Minigame Level Editor
    Created 2013 Triangle717
    <http://triangle717.wordpress.com/>

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

# Append build to the arguments. Just type "python setup.py" and it will compile
if len(sys.argv) == 1: sys.argv[1:] = ["build"]

# Compile into the proper folder depending on the architecture
# Based on code from the Python help file (platform module) and my own tests
if sys.maxsize == 2147483647:
    destfolder = "Compile2/Windows32"
else:
    destfolder = "Compile2/Windows64"

build_exe_options = {"build_exe": destfolder,
                     "icon": "Media/Blocks.ico",
                     "include_files": ["Media"]}

setup(
    name = "Blocks",
    version = "0.5",
    author = "Triangle717",
    description = "Island Xtreme Stunts Minigame Level Editor",
    license = "GNU GPLv3",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Blocks.pyw", targetName="Blocks.exe", base="Win32GUI")]
)