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

import os


def Write(destfolder):
    '''Write files when freezing Blocks for Windows'''

    # Write the required RunAsAdmin.cfg file
    with open(os.path.join(destfolder, "RunAsAdmin.cfg"), "wt") as f:
        f.write("Blocks.exe")

    # Write a batch script to launch Blocks
    with open(os.path.join(os.path.dirname(destfolder), "Blocks.bat"),
         "wt") as f:
        f.write('''@echo off
REM Blocks - Island Xtreme Stunts Minigame Level Editor
REM Created 2013 Triangle717
REM <http://Triangle717.WordPress.com/>

REM Blocks is free software: you can redistribute it and/or modify
REM it under the terms of the GNU General Public License as published by
REM the Free Software Foundation, either version 3 of the License, or
REM (at your option) any later version.

REM Blocks is distributed in the hope that it will be useful,
REM but WITHOUT ANY WARRANTY; without even the implied warranty of
REM MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM GNU General Public License for more details.

REM You should have received a copy of the GNU General Public License
REM along with Blocks. If not, see <http://www.gnu.org/licenses/>.

REM Launches Blocks for Windows

REM Quotes in case there are spaces in the folder path
cd "%~p0\Windows"
start Blocks.exe
exit''')