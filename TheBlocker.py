#! python3
# -*- coding: utf-8 -*-
"""
    The Blocker - Island Xtreme Stunts Minigame Level Editor
    Created 2013 Triangle717
    <http://triangle717.wordpress.com/>

    The Blocker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Blocker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with The Blocker. If not, see <http://www.gnu.org/licenses/>.

"""

import os

# GUI code
import tkinter as tk
from tkinter import ttk
# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

### Colored shell text
##import Color as color, Color.colors as colors

# Global variables
app = "The Blocker"
majver = "0.1"
minver = ""

def main():
    '''Views Minigame Level'''

    print("\nSelect a Minigame Level\n")

    # Draw (then withdraw) the root Tk window
    root = Tk()
    root.withdraw()

    # Overwrite root display settings
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the patch file
    level = filedialog.askopenfilename(
    parent=root,
    title="Select a Minigame Level")

    # The user clicked the cancel button
    if len(level) == 0:
        # Give focus back to console window
        root.destroy()
        # Quit Application
        raise SystemExit

    # The user selected a level
    else:
        # Give focus back to console window
        root.destroy()

        # Open file for reading
        with open(level, "rt") as f:
            lines = f.readlines()[:]
        # Remove nulls, since they cannot be printed
        layout = "".join(lines[2:])
        print(layout)
##        colors.pc(layout, color.FG_LIGHT_CYAN)

        # Print legend
        print("\nLegend: F = free block, BW = Blocked Wall, YC = Yellow Cube, YT = Yellow Tile,\nRC = Red Cube, RT = Red Tile, BC = Blue Cube, BT = Blue Tile")

    # Prompt for new level
    print("\nDo you want to load a new level? " + r"(y\N)")
    new_level = input("\n> ")
    if new_level.lower() == "y":
        # Loop back through
        main()
    else:
        # Close application
        raise SystemExit

if __name__ == "__main__":
    os.system("title {0} {1}".format(app, majver))
    main()