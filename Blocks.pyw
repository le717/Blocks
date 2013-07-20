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


def globals():
    '''Dummy function for easy access to global variables'''
    pass

# Global variables
app = "Blocks"
majver = "0.8"
minver = ".6"
app_logo = os.path.join("Media", "BlocksIcon.gif")
app_icon = os.path.join("Media", "Blocks.ico")

# Global variable defining if a new level was created or not
new_level = False

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


def New(*args):
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


def Open(*args):
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
    title="Select a Minigame Layout")

    # The user clicked the cancel button
    if not level_file:
        # Close dialog box
        pass
    # The user selected a level
    else:
        read(level_file)


# ------------ End Level Layout Opening ------------ #


# ------------ Begin Level Layout Reading ------------ #


def read(level_file):
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

    # Skip nulls, since they cannot be displayed,
    # and display only the layout
    layout = "".join(lines[1:9])
    level.delete("1.0", "end")
    level.insert("1.0", layout)


# ------------ End Level Layout Reading ------------ #


# ------------ Begin Level Layout Syntax Check ------------ #


def syntax_check(*args):
    '''Checks the  Level Layout for syntax errors'''

    # Get new layout from text box, minus the new line the text widget adds
    layout = level.get('1.0', 'end -2 chars')

    # Split the layout at each new line
    layout_size = layout.split("\n")

    # Get the index for each line in the layout
    if debug:
        print("The new layout is: \n")
    for lineno, linetext in enumerate(layout_size):
        # Display line number and line content if debug messages are enabled
        if debug:
            print(lineno, linetext)
        # Do nothing else, all we need are the indices
        pass

    # If lineno is more than 7, AKA the level is more than 8 lines
    if lineno > 7:
        # Display error message in console if debug messages are enabled
        if debug:
            print("\nThe level is too big! It must be only 8 lines, and yours is {0} lines!\n".format(lineno + 1))
        # Display error message to user telling them the level is too big
        showerror("Level Error!", '''The level layout must be no more than 8 lines.
Your layout takes up {0} lines!'''.format(lineno + 1))

        # Return False so the saving process will not continue on
        return False

    # On the flip side, if the index equals 0, AKA the level area is blank
    # I could have merged these two messages, but I wanted to show different
    # messages depending on the error. I still may split them...
    if lineno < 7:
        # Display error message in console if debug messages are enabled
        if debug:
            print("\nThe level is too small! It must be 8 lines, and yours is {0} lines!\n".format(lineno + 1))
        # Display error message to user telling them the level is too small
        showerror("Error!", '''The level layout must be 8 lines.
Your layout is only {0} lines!'''.format(lineno + 1))

        # Return False so the saving process will not continue on
        return False

    # Split the text at each space
    layout_syntax = layout.split(" ")

    # The allowed characters in a layout
    itemlist = ["", "F", "BW", "YC", "YT", "RC", "RT", "RB", "BC", "BT", "GT",
    "GC", "WB", "WH", "WI", "WJ", "WM", "WL", "WR", "WT", "WV"]

    for index, char in enumerate(layout_syntax):
        # Remove \n, \t, and the like
        char = char.strip()

        # If any character in the layout is not in the list
        if char.upper() not in itemlist:
            if debug:
                print('\nInvalid character "{0}" at position {1}\n'.format(
                    char, index + 1))
            showerror("Syntax Error!",
            'Invalid character: "{0}" at position {1}'.format(char, index + 1))
            # Return False so the saving process will not continue on
            return False

    # Remove the list, keep proper formatting
    fixed_layout = " ".join(layout_syntax)

    # Convert all text to uppercase
    upper_layout = fixed_layout.upper()

    if debug:
        print("\n\nThe new layout (after syntax checking) is: \n\n{0}".format(
            upper_layout))
    # Send the corrected layout for writing
    write(upper_layout)

# ------------ End Level Layout Syntax Check ------------ #


# ------------ Begin Level Layout Writing ------------ #

def write(new_layout):
    '''Writes Modded Minigame Level'''

    try:
        # Get just the folder path to the file
        location = os.path.dirname(level_file)

        # They are the same, but this is needed to remove an error
        backup_file = level_file

        # Used to rename the file if it already exists
        count = 0
        while os.path.exists(backup_file):
            # Update count
            count += 1
            # Define backup filename
            backup_file = os.path.join(location, "{0}{1}{2}".format(
                level_filename, ".bak", str(count)))

        try:
            # Copy the file, try to preserve metadata
            shutil.copy2(level_file, backup_file)

            # Read (original, not .bak*) file in binary mode
            with open(level_file, "rb") as f:
                # Read just the first line
                for line in range(0, 1):
                    first_line = f.readline()

            # Convert layout from string to binary
            layout = str.encode(new_layout, encoding="utf-8", errors="strict")

            # Open the (original, not .bak*) level back up, again in binary mode
            with open(level_file, "wb") as f:
                # Rewrite the first line
                f.write(first_line)
                # Write the new layout
                f.write(layout)
                # Write requied ending line
                f.write(b"\r\n ")

            # Display sucess dialog
            tk.messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
            .format(level_filename, location))

        # A level was edited directly in Program Files,
        # and Blocks was run without Admin rights
        except PermissionError:
            showerror("Insufficient User Rights!",
'''Blocks does not have the user rights to save {0}!
Please relaunch Blocks as an Administrator.'''.format(level_filename))
            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)

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


# ------------ End Level Layout Writing ------------ #


# ------------ Begin Level Legend Window ------------ #


def the_legend(*args):
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

    def close_legend(*args):
        '''Closes Legend Window'''
        legend_window.destroy()

    # Bind <Ctrl + q> shortcut to close the legend window
    legend_window.bind('<Control-q>', close_legend)

    # Close Legend button
    close_legend_button = ttk.Button(legend_window, default="active",
        text="Close", command=close_legend)
    close_legend_button.grid(column=1, row=1, sticky=tk.S)


# ------------ End Level Legend Window ------------ #


# ------------ Begin Python Version Check ------------ #


def PyVerCheck(*args):
    '''Dummy function for easy access to Python Version Check code'''
    pass

# User is not running >= Python 3.3.0
if sys.version_info < (3, 3, 0):
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(app_icon)
    showerror("Unsupported Python Version!", '''You are running Python {0}.
You need to download Python 3.3.0 or newer to run\n{1} {2}{3}.\n'''
.format(sys.version[0:5], app, majver, minver))
    # Opens only when user clicks OK
    # New tab, raise browser window (if possible)
    webbrowser.open_new_tab("http://python.org/download/")
    # Close Blocks
    raise SystemExit


# ------------ End Python Version Check ------------ #


# ------------ Begin Tkinter GUI Layout ------------ #


def GUI():
    '''Dummy function for easy access to GUI code'''
    pass

# Run Python Version check
PyVerCheck()
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
about_blocks = ttk.Label(mainframe, text='''                 {0} {1}{2}
    Created 2013 Triangle717'''.format(app, majver, minver))
about_blocks.grid(column=2, row=0, sticky=tk.N)

# New button
##new_button = ttk.Button(mainframe,text="New", command=New)
##new_button.grid(column=2, row=1, sticky=tk.N)
# Open button
open_file = ttk.Button(mainframe, text="Open", command=Open)
open_file.grid(column=2, row=2, sticky=tk.N)
# Save button
save_file = ttk.Button(mainframe, text="Save", command=syntax_check)
save_file.grid(column=2, row=3, sticky=tk.N)
# Character Legend button
legend_button = ttk.Button(mainframe, text="Character Legend",
command=the_legend)
legend_button.grid(column=0, row=0, columnspan=2)

# Blocks Logo
blocks_logo = tk.PhotoImage(file=app_logo)
image_frame = ttk.Label(mainframe)
image_frame['image'] = blocks_logo
image_frame.grid(column=2, row=3, sticky=tk.S)

# Padding around all the elements
for child in mainframe.winfo_children():
    child.grid_configure(padx=2, pady=2)


def close(*args):
    '''Closes Blocks'''
    raise SystemExit

## Bind <Ctrl + n> shortcut to New button
##root.bind("<Control-n>", New)
# Bind <Ctrl + Shift + O> (as in, Oh!) shortcut to Open button
root.bind("<Control-O>", Open)
# Bind <Ctrl + s> shortcut to Save button
root.bind("<Control-s>", syntax_check)
# Bind <Ctrl + q> shortcut to close function
root.bind("<Control-q>", close)
# Bind F12 key to Character Legend button
root.bind('<F12>', the_legend)

# Run program
root.mainloop()


# ------------ End Tkinter GUI Layout ------------ #