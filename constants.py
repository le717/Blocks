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
Blocks Constants
"""

import os
import sys

# Global variables
app = "Blocks"
majver = "0.9"
minver = ".2"
creator = "Triangle717"

# Name of Blocks Exe/Py
exe_name = os.path.basename(sys.argv[0])

# Location of Blocks! Exe/Py
app_folder = os.path.dirname(sys.argv[0])

# Icons
app_logo = os.path.join("Media", "Blocks.gif")
app_icon = os.path.join("Media", "Blocks.ico")

# Global variable defining if a new level was created or not
new_level = None
