# -*- coding: utf-8 -*-
"""Blocks - Island Xtreme Stunts Minigame Level Editor.

Created 2013-2014 Triangle717
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
import sys
from datetime import datetime

app = "Blocks"
majVer = "0.9"
minVer = ".2"
creator = "Triangle717"
currentYear = datetime.now().year
debugMode = False
newLevel = None

# Name of Blocks Exe/Py
exeName = os.path.basename(sys.argv[0])

# Location of Blocks Exe/Py
appFolder = os.path.dirname(sys.argv[0])

# Icons
appLogo = os.path.join("Media", "Blocks.gif")
appIcon = os.path.join("Media", "Blocks.ico")
