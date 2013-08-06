#! /usr/bin/env python3
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

# Import just what is needed at the moment
import sys
import os
import webbrowser

# Blocks constants
from constants import *

# User is not running >= Python 3.3.0
if sys.version_info < (3, 3, 0):
    # Import Python 2 Tkinter library
    import Tkinter as tk
    import tkMessageBox
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(app_icon)
    tkMessageBox.showerror("Unsupported Python Version!",
'''You are running Python {0}.
You need to download Python 3.3.0 or newer to run\n{1} {2}{3}.\n'''
.format(sys.version[0:5], app, majver, minver))

    # Opens only when user clicks OK
    # New tab, raise browser windows
    webbrowser.open_new_tab("http://python.org/download/")

    # Close Blocks
    raise SystemExit

# Now that we know we are running Python 3.3+,
# let's import everything else we needed
import shutil
import subprocess

# Tkinter GUI library
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter.messagebox import (showerror, askyesno)

try:
    # If the debug parameter is passed, enable the debugging messages
    if sys.argv[1] == "--debug":
        debug = True
        os.system("title Blocks {0}{1} - Debug".format(majver, minver))
        import traceback
        print("\nDebug messages have been enabled.\n")
except IndexError:
    # The debug parameter was not passed, don't display debugging messages
    debug = False


# ------------ Begin New Minigame Level ------------ #


def NewLevel(*args):
    '''Create a new Minigame Level'''

    # Update variable saying a new level was created
    global new_level
    new_level = True

    if debug:
        print("\nA new level is being created.\n")

    # Blank (free) layout for when starting a new level
    blank_layout = ''' F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F'''

    # Remove the old content
    level.delete("1.0", "end")
    # Add blank layout in edit box
    level.insert("1.0", blank_layout)


# ------------ End New Minigame Level  ------------ #


# ------------ Begin Level Layout Opening ------------ #


def OpenLevel(*args):
    '''Reads Minigame Level'''

    # File type label for dialog box
    formats = [("IXS Minigame Layout", ".TXT")]

    # Assign selected file as global
    global level_file
    # Select the level file
    level_file = askopenfilename(
        parent=root,
        defaultextension=".TXT",
        filetypes=formats,
        title="Select a Minigame Layout"
    )

    # The user clicked the cancel button
    if not level_file:
        # Close dialog box
        pass
    # The user selected a level
    else:

        # Display  full path to the file
        if debug:
            print(level_file)
        # Send the file off for reading
        ReadLevel(level_file)


# ------------ End Level Layout Opening ------------ #


# ------------ Begin Level Layout Reading ------------ #


def ReadLevel(level_file):
    '''Reads an existing level file'''

    # Update new level variable to denote a pre-existing level
    new_level = False
    if debug:
        print("\nA new level is not being created.\n")

    # Get just the file name, assign it as global
    global level_filename
    level_filename = os.path.basename(level_file)
    level_name.set(level_filename)

    # Open file for reading
    with open(level_file, "rt") as f:
        lines = f.readlines()[:]

    # Skip nulls, since they cannot be displayed
    layout = "".join(lines[1:9])

    # Remove the trailing new line so the syntax checker will work correctly
    layout = layout.rstrip("\n")

    # Remove all text in the widget
    level.delete("1.0", "end")

    # (music) Put the layout in the widget and edit it all up (music)
    level.insert("1.0", layout)


# ------------ End Level Layout Reading ------------ #


# ------------ Begin Level Layout Syntax Check ------------ #

# The allowed characters in a layout
# This is in the global namespace because a couple of things reference it
itemlist = ["", "F", "BW", "YC", "YT", "RC", "RT", "RB", "BC", "BT", "GT",
"GC", "WB", "WH", "WI", "WJ", "WM", "WL", "WR", "WT", "WV"]


def syntax_check(*args):
    '''Checks the  Level Layout for syntax errors'''

    # Get new layout from text box, including the extra line
    # the Text Edit widget makes. This is requried to make everything work
    layout = level.get('1.0', 'end')

    # Split the layout at each new line, removing the last two characters
    # This cannot be done above, it must be done here
    layout_size = layout[:-2].upper().split("\n")

    # Run level size check
    size_check = level_size(layout_size)

    # If the level size check returns an error,
    if size_check == "Error":
        # Return False so the saving process will not continue on
        return False

    # Delete the list to free up resources
    del layout_size[:]

    # Split the layout at each new line, removing the last character
    # This split has to be done again but differently for the check to work
    line_size = layout[:-1].upper().split("\n")

    # Run line length check
    line_check = line_length(line_size)

    # If the line length check returns an error,
    if line_check == "Error":
        # Return False so the saving process will not continue on
        return False

    # Delete the list to free up resources
    del line_size[:]

    # Split the text at each space
    layout_syntax = layout.split(" ")

    # Run character check
    valid_char = char_check(layout_syntax)

    # If the character check returns an error,
    if valid_char == "Error":
        # Return False so the saving process will not continue on
        return False

    # Delete the list to free up resources
    del layout_syntax[:]

    # Display final debug message for the syntax checker
    if debug:
        print("\n\nThe new layout (after syntax checking) is: \n\n{0}".format(
            layout))

    # Send the corrected layout for writing
    # new_layout[:-1] so the last character is not left out
    # Also convert layout to uppercase so IXS won't crash
    write(layout[:-1].upper())


# --- Begin Level Size Check --- #


def level_size(layout_size):
    '''Checks the size of the layout'''

    if debug:
        print("\nThe new layout is:\n")

    # Get the indices and text for each line
    for lineno, linetext in enumerate(layout_size):

        # Display line number and line content if debug messages are enabled
        if debug:
            print(lineno, linetext)
        # Do nothing else, all we need are the indices
        pass

    # The actual line number
    lineno += 1

    if (  # The level is more than 8 lines
        lineno > 8 or
        # The level is less than 8 lines
        lineno < 8):

        # Display error message in console if debug messages are enabled
        if debug:
            print('''\nYour level contains {0} lines!
The level must be exactly 8 lines.'''.format(lineno))

        # Display error message to user telling them about the error
        showerror("Size Error!",
'''Your level contains {0} lines!
The level must be exactly 8 lines.\n'''.format(lineno))

        # Return custom error message everything will work
        return "Error"

# --- End Level Size Check --- #


# --- Begin Line Length Check --- #


def line_length(line_size):
    '''Checks the length of each line'''

    # Bit of spacing for debug messages
    if debug:
        print()

    # Get the indices and text for each line
    for linenum, linedata in enumerate(line_size):

        # The actual line number
        linenum += 1

        # How long is each line?
        len_of_line = len(linedata)

        # Display length of each line if debug messages are enabled
        if debug:
            print("Line {0} is {1} characters long".format(
                linenum, len_of_line))

        # If the line is less than 38 characters, counting spaces
        if len_of_line < 38:

            # Tell user the error
            if debug:
                print('''Line {0} is {1} characters! The line must be exactly
38 characters, including spaces.'''.format(linenum, len_of_line))

            showerror("Length Error!", '''Line {0} is {1} characters!
The line must be exactly 38 characters, including spaces.'''.format(
    linenum, len_of_line))

            # Return custom error message everything will work
            return "Error"

            """
            While all lines must be at least 38 characters, some levels has
            lines that are 39 characters.
            Techinally, they can be longer, but odd, undocumented stuff occurs
            when extra characters are added
            to the left or right side of the layout.
            """

# --- End Line Length Check --- #


# --- Begin Character Syntax Check --- #


def char_check(layout_syntax):
    '''Checks if each character in the layout is valid'''

    # Get indices and text for each line
    for index, char in enumerate(layout_syntax):

        # Remove \n, \t, and the like
        char = char.strip()

        # The proper location of the character
        index += 1

        # If any character in the layout is not in the list
        if char.upper() not in itemlist:
            if debug:
                print('\nInvalid character "{0}" at position {1}\n'.format(
                    char, index))
            showerror("Syntax Error!",
            'Invalid character: "{0}" at position {1}'.format(char, index))

            # Return custom error message everything will work
            return "Error"


# --- End Character Syntax Check --- #


# ------------ End Level Layout Syntax Check ------------ #


# ------------ Begin Level Layout Writing ------------ #

def backup(location, backup_file):
    '''Makes a backup of the level before saving'''

    # Used to rename the file if it already exists
    count = 0
    while os.path.exists(backup_file):

        # Update count
        count += 1

        # Define backup filename
        #FIXME: in 0.8.7 release: Limit the number of backups made to 3,
        # but preserve the first backup, AKA the oldest one
        backup_file = os.path.join(location, "{0}{1}{2}".format(
            level_filename, ".bak", str(count)))

        try:
            # Copy the file, and try to preserve metadata
            shutil.copy2(level_file, backup_file)
            # This has to be here so an infinite number
            # of backups are not created
            break

        # A level was edited directly in Program Files,
        # or some other action that requried Admin rights
        except PermissionError:

            showerror("Insufficient User Right!",
'''Blocks does not have the user rights to save {0}!'''.format(level_filename))

            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)


def write(new_layout):
    '''Writes Modded Minigame Level'''

    #OPTIMIZE: This entire function, breaking it up,
    # allowing for the relaunch, new level, and maybe --open parameter

    try:
        # Get just the folder path to the file
        location = os.path.dirname(level_file)

        try:
            # Read (original, not .bak*) file in binary mode
            with open(level_file, "rb") as f:
                # Read just the first line
                for line in range(0, 1):
                    first_line = f.readline()

            # Run process to backup the level
            backup(location, level_file)

            # Convert layout from str(ing) to binary
            layout = str.encode(new_layout, encoding="utf-8", errors="strict")

            # Open the (original, not .bak*) level back up, again in binary mode
            with open(level_file, "wb") as f:
                # Rewrite the first line
                f.write(first_line)
                # Write the new layout
                f.write(layout)

            # Display sucess dialog
            tk.messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
            .format(level_filename, location))

        # A level was edited directly in Program Files,
        # and Blocks was run without Admin rights
        except PermissionError:

            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)

            #TODO: Possibly add ability to save temp file and reopen it?
            admin = askyesno("Reload Blocks?",
'''Would you like to relaunch Blocks with Administrator rights?
Your level will be lost in the process!''')

            # If user chooses to relaunch
            if admin:
                temp_file = temp_write(True, first_line, layout)
                print(temp_file)
                subprocess.call(["RunAsAdmin.exe", '--open "{0}"'.format(
                    temp_file)])
                raise SystemExit(0)

            else:
                # Return False so the saving process will not continue on:
                return False

        # Any other unhandled error occurred
        except Exception:
            showerror("An Error Has Occurred!",
"Blocks ran into an unknown error while trying to {0}!".format(level_filename))
            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)

    # The user tried to same a level without loading one first
    except NameError:
        showerror("Cannot Save Level!",
"A minigame level has not been selected for editing!")
        if debug:
            # Display complete traceback to console
            traceback.print_exc(file=sys.stderr)


def temp_write(new=True, first_line=None, layout=None):
    '''Saves the level to a temporary file'''

    # Name and location of temp file
    name = os.path.join(app_folder, "Temp_Level.TXT")

    # Meaning we need to write a new temporary level
    if new:
        # Write the temp file, using binary mode
        with open(name, "wb") as f:
            # Rewrite the first line
            f.write(first_line)
            # Write the new layout
            f.write(layout)

        # Send back the path to the temporary level
        return name

    # Meaning we need to remove a temporary level
    elif not new:
        os.unlink(name)


# ------------ End Level Layout Writing ------------ #


# ------------ Begin Level Legend Window ------------ #


def CharLegend(*args):
    '''Contains Level Character Legend'''

    # Spawn a new window, parent it to main window
    legend_window = tk.Toplevel(root)
    # App Icon
    legend_window.iconbitmap(app_icon)
    # The window cannot be resized at all
    # Length x width
    legend_window.minsize("400", "260")
    legend_window.maxsize("400", "260")
    # Lift it above main window, give it focus
    legend_window.lift()
    legend_window.focus()

    # The legend itself
    legend_text = '''\t\t        === Available Colors ===
\t              R = Red, G = Green, B = Blue, Y = Yellow

\t\t        === Available Types ===
\t\t\t  F = Free Tile,
\t\t              BW = Blocked Wall,
\t\t            (R, G, B, Y)C = Cube,
\t\t            (R, G, B, Y)T = Tile,
\t\tRB = One-way, west-bound Red Cube

\t\t\t=== Water ===
\t        WH = Small Horizontal, WV = Small Vertical,
\t            WI = Top, WJ = Left, WM = Right,
\t            WT = Top Left, WL = Top Right,
\t            WR = Bottom Left, WB = Bottom Right'''

    # Display the legend
    ttk.Label(legend_window, text=legend_text).grid()

    def CloseCharLegend(*args):
        '''Closes Character Legend Window'''
        legend_window.destroy()

    # Bind <Ctrl + q> shortcut to close the legend window
    legend_window.bind('<Control-q>', CloseCharLegend)

    # Close Legend button
    close_legend_button = ttk.Button(legend_window, default="active",
        text="Close", command=CloseCharLegend)
    close_legend_button.grid(column=1, row=1, sticky=tk.S)


# ------------ End Level Legend Window ------------ #


# ------------ Begin Tkinter GUI Layout ------------ #


def GUI():
    '''Dummy function for easy access to GUI code'''
    pass

# Root window settings
root = tk.Tk()
root.title("{0} {1}{2}".format(app, majver, minver))
# App icon
root.iconbitmap(app_icon)

# The smallest size the window can be
# Length x width
root.minsize("575", "225")

# Frame settings
mainframe = ttk.Frame(root, padding="7 7 7 7")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Resizing code
root.columnconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

# Level (file) name display
level_name = tk.StringVar()
ttk.Label(mainframe, textvariable=level_name).grid(
    column=0, row=2, columnspan=2)

# Where level is viewed and edited
level = tk.Text(mainframe, height=8, width=40, wrap="none")
level.grid(column=0, row=3, sticky=(tk.N, tk.S, tk.E))
level.insert("1.0", "Minigame layout will be displayed here.")

# About Blocks text
about_blocks = ttk.Label(mainframe, text='''           {0} {1}{2}
  Created 2013 Triangle717'''.format(app, majver, minver))
about_blocks.grid(column=2, row=0, sticky=tk.N)

# New button
##new_button = ttk.Button(mainframe, text="New", command=NewLevel)
##new_button.grid(column=2, row=1, sticky=tk.N)
# Open button
open_file = ttk.Button(mainframe, text="Open", command=OpenLevel)
open_file.grid(column=2, row=2, sticky=tk.N)
# Save button
save_file = ttk.Button(mainframe, text="Save", command=syntax_check)
save_file.grid(column=2, row=3, sticky=tk.N)
# Character Legend button
legend_button = ttk.Button(mainframe, text="Character Legend",
command=CharLegend)
legend_button.grid(column=0, row=0, columnspan=2)

# Blocks Logo
blocks_logo = tk.PhotoImage(file=app_logo)
image_frame = ttk.Label(mainframe)
image_frame['image'] = blocks_logo
image_frame.grid(column=2, row=3, sticky=tk.S)

# Padding around all the elements
for child in mainframe.winfo_children():
    child.grid_configure(padx=2, pady=2)


def Close(*args):
    '''Closes Blocks'''
    raise SystemExit

## Bind <Ctrl + n> shortcut to New button
root.bind("<Control-n>", NewLevel)
# Bind <Ctrl + Shift + O> (as in, Oh!) shortcut to Open button
root.bind("<Control-O>", OpenLevel)
# Bind <Ctrl + s> shortcut to Save button
root.bind("<Control-s>", syntax_check)
# Bind <Ctrl + q> shortcut to close function
root.bind("<Control-q>", Close)
# Bind F12 key to Character Legend button
root.bind('<F12>', CharLegend)

# Run program
root.mainloop()


# ------------ End Tkinter GUI Layout ------------ #