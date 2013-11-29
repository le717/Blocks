#! /usr/bin/python3
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

-------------------------------------
Remove unneded Tkinter files after freezing Blocks!
"""

import os
import distutils.dir_util


def cleanup(destfolder):
    """Remove unneeded Tkinter files"""
    # Small bit of whitespace
    print("\n")
    # Delete the unneeded items from the freeze
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tcl", "tzdata"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tcl", "http1.0"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tk", "demos"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tk", "images"))
