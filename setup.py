#! python3.3-32
# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Blocks - Island Xtreme Stunts Minigame Level Editor
Created 2013 Triangle717
<http://Triangle717.WordPress.com/>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
    raise SystemExit

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