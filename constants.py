# Blocks constants

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