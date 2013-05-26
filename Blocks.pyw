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
import sys
import os
import shutil
import webbrowser
try:
    # Python 3 import
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    from tkinter import ttk
    from tkinter.messagebox import showerror
except ImportError:
    # Python 2 import
    import Tkinter as tk
    from tkMessageBox import showerror

# Global variables
app = "Blocks"
majver = "0.6"
minver = ".5"
app_logo = os.path.join("Media", "BlocksIcon.gif")
app_icon = os.path.join("Media", "Blocks.ico")

# ------------ Begin Level Layout Reading ------------ #

def read(*args):
    '''Reads Minigame Level.'''

    # File type label for dialog box
    formats = [("IXS Minigame Layout", ".TXT")]

    # Assign selected file as global
    global level_file
    # Select the level file
    level_file = askopenfilename(
    parent=root,
    defaultextension=".TXT",
    filetypes=formats,
    title="Select a Minigame Layout")

    # The user clicked the cancel button
    if len(level_file) == 0:
        # Close dialog box
        pass

    # The user selected a level
    else:
       # Get just the file name, assign it as global
        global level_file_name
        level_file_name = os.path.basename(level_file)
        # Open file for reading
        with open(level_file, "rt") as file:
            lines = file.readlines()[:]

        # Skip nulls, since they cannot be printed,
        # and display only the layout
        layout = "".join(lines[2:9])
        level.delete("1.0", "end")
        level.insert("1.0", layout)

# ------------ End Level Layout Reading ------------ #

# ------------ Begin Level Layout Writing ------------ #

def write(*args):
    '''Writes Modded Minigame Level.'''

    try:
        # Get just the folder path to the file
        location = level_file.rstrip(level_file_name)
    except NameError:
        showerror("Cannot Save Level!", "A minigame level has not been selected for editing!")

    # name == everything before extenstion,
    # ext == the extenstion
    name, ext = os.path.splitext(level_file_name)

    # They are the same
    new_file = level_file

    # Used to rename the file if it already exists
    count = 0
    while os.path.exists(new_file):
        # Update count
        count += 1
        # Define new file name
        new_file = os.path.join(location, '{0}{1}{2}{3}'.format(name, ext, ".bak", str(count)))
    #print(new_file)
    # Copy the file, try to preserve metadata
    shutil.copy2(level_file, new_file)
    # For now
    raise SyntaxError
##    pass


# ------------ End Level Layout Writing ------------ #

# ------------ Begin Python Version Check ------------ #

def PyVerCheck():
    '''Dummy function for easy access to Python Version Check code.'''
    pass

# User is not running < Python 3.3.0
if sys.version_info < (3,3,0):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(app_icon)
    showerror("Unsupported Python Version!", "You are running Python {0}.\nYou need to download Python 3.3.0 or newer to run\n{1} {2}{3}.\n".format(sys.version[0:5], app, majver, minver))
    # Opens only when user clicks OK
    # New tab, raise browser window (if possible)
    webbrowser.open_new_tab("http://python.org/download/")
    raise SystemExit

# ------------ End Python Version Check ------------ #


# ------------ Begin Tkinter GUI Layout ------------ #

def GUI():
    '''Dummy function for easy access to GUI code.'''
    pass

# Root window settings
root = tk.Tk()
root.title("{0} {1}{2}".format(app, majver, minver))
# The window cannot be resized at all
root.minsize("500", "260")
root.maxsize("500", "260")

# Frame settings
mainframe = ttk.Frame(root, padding="7 7 7 7")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)

# Where level is viewed (and in the future, edited)
level = tk.Text(mainframe, height=7, width=40, wrap="none")
level.grid(column=0, row=3)
level.insert("1.0", "Minigame layout will be displayed here.")

# Legend display
# TODO: Finish populating list
ttk.Label(mainframe, text='''                                              Legend:
            F = free block, BW = Blocked Wall, YC = Yellow Cube,
            YT = Yellow Tile, RC = Red Cube, RT = Red Tile,
            BC = Blue Cube, BT = Blue Tile''').grid(column=0, row=0, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text='''                 {0} {1}{2}
    Created 2013 Triangle717'''.format(app, majver, minver)).grid(column=2, row=0, sticky=tk.N)

# Open button
ttk.Button(mainframe, text="Open", command=read).grid(column=2, row=1, sticky=tk.N)
# Save button
ttk.Button(mainframe, text="Save", command=write).grid(column=2, row=2, sticky=tk.N)

# Blocks Logo
blocks_logo = tk.PhotoImage(file=app_logo)
image_frame = ttk.Label(mainframe)
image_frame['image'] = blocks_logo
image_frame.grid(column=2, row=3, sticky=tk.N)

# Padding around elements
for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

def close(*args):
    '''Closes Blocks.'''
    raise SystemExit

# Bind <Ctrl + o> (lowercase "o" (as in "Oh!")) shortcut to Open button
root.bind("<Control-o>", read)
# Bind <Ctrl + s> shortcut to Save button
root.bind("<Control-s>", write)
# Bind escape key to close function
root.bind("<Escape>", close)
# Add app icon, run program
root.iconbitmap(app_icon)
root.mainloop()

# ------------ End Tkinter GUI Layout ------------ #