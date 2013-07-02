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
import sys
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
    '''Dummy function for eas access to global variables'''
    pass

# Global variables
app = "Blocks"
majver = "0.8"
minver = ".2.7"
app_logo = os.path.join("Media", "BlocksIcon.gif")
app_icon = os.path.join("Media", "Blocks.ico")

try:
    # If the debug parameter is passed, enable the debugging messages
    if sys.argv[1] == "--debug":
        debug = True
        import traceback
        print("\nDebug messages have been enabled.\n")
except IndexError:
    # The parameter was not passed, don't display debugging messages
    debug = False

# ------------ Begin Level Layout Reading ------------ #

def read(*args):
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
    if len(level_file) == 0:
        # Close dialog box
        pass
    # The user selected a level
    else:
       # Get just the file name, assign it as global
        global level_file_name
        level_file_name = os.path.basename(level_file)
        level_name.set(level_file_name)
        # Open file for reading
        with open(level_file, "rt") as file:
            lines = file.readlines()[:]

        # Skip nulls, since they cannot be printed,
        # and display only the layout
        layout = "".join(lines[1:9])
        level.delete("1.0", "end")
        level.insert("1.0", layout)

# ------------ End Level Layout Reading ------------ #


# ------------ Begin Level Layout Syntax Check ------------ #

def syntax_check(*args):
    '''Checks the Minigame Level Layout for syntax errors'''

    # Get new layout from text box
    layout = level.get('1.0', 'end')
    if debug:
        print("The new layout is: \n\n{0}".format(layout))

    # Split the text at each space
    layout_syntax = layout.split(" ")

    # The allowed characters in a layout
    # TODO: Finish populating this, along with the legend
    itemlist = ["", "F", "BW", "YC", "YT", "RC", "RT", "BC", "BT", "GT", "GC",
    "WT", "WI", "WJ", "WM"]

    for index, char in enumerate(layout_syntax):
        # Remove \n, \t, and the like
        char = char.strip()

        # If any character in the layout is not in the list
        if char.upper() not in itemlist:
            if debug:
                print('Invalid character "{0}" at position {1}\n'.format(char, index))
            showerror("Error!", 'Invalid character: "{0}" at position {1}'.format(char, index))
            # return False so the saving process will not continue on
            return False

    # Remove the list, keep proper formatting
    fixed_layout = " ".join(layout_syntax)

    # Convert all text to uppercase
    upper_layout = fixed_layout.upper()

    if debug:
        print("The new layout (after syntax checking) is: \n\n{0}".format(upper_layout))
    # Send the corrected layout for writing
    write(upper_layout)

# ------------ End Level Layout Syntax Check ------------ #


# ------------ Begin Level Layout Writing ------------ #

def write(new_layout):
    '''Writes Modded Minigame Level'''

    try:
        # Get just the folder path to the file
        location = level_file.rstrip(level_file_name)

        # They are the same, but this is needed to remove an error
        backup_file = level_file

        # Used to rename the file if it already exists
        count = 0
        while os.path.exists(backup_file):
            # Update count
            count += 1
            # Define backup filename
            backup_file = os.path.join(location, "{0}{1}{2}".format(level_file_name, ".bak", str(count)))

        try:
            # Copy the file, try to preserve metadata
            shutil.copy2(level_file, backup_file)

            # Read (original, not .bak*) file in binary mode
            with open(level_file, "rb") as f:
                # Read just the first line
                for line in range(0, 1):
                    first_line = f.readline()

            # Convert layout from string to binary, removing the extra lines
            layout = str.encode(new_layout[:-2], encoding="utf-8", errors="strict")

            # Open the (original, not .bak*) level back up, again in binary mode
            with open(level_file, "wb") as f:
                # Rewrite the first line
                f.write(first_line)
                # Write the new layout
                f.write(layout)
                # Write requied ending line
                f.write(b"\r\n ")

            # Display sucess dialog, [:-1] to remove the trailing "\"
            tk.messagebox.showinfo("Success!", "Successfully saved {0} to {1}".format(level_file_name, location[:-1]))

        # A level was edited directly in Program Files,
        # and Blocks was run without Admin rights
        except PermissionError:
            showerror("Insufficient User Rights!", "Blocks does not have the user rights to save {0}!\nPlease relaunch Blocks as an Administrator.".format(level_file_name))
            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)

        # Any other unhandled error occurred
        except Exception:
            showerror("An Error Has Occurred!", "Blocks ran into an unknown error while trying to {0}!".format(level_file_name))
            if debug:
                # Display complete traceback to console
                traceback.print_exc(file=sys.stderr)

    # The user tried to same a level without loading one first
    except NameError:
        showerror("Cannot Save Level!", "A minigame level has not been selected for editing!")
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
    legend_window.minsize("400", "350")
    legend_window.maxsize("400", "350")
    # Lift it above main window, give it focus
    legend_window.lift()
    legend_window.focus()

    # Legend display
    # TODO: Finish populating list
    legend = ttk.Label(legend_window, text='''                                            === Available Colors ===
                                  R = Red, G = Green, B = Blue, Y = Yellow

                                            === Available Types ===
                                                    F = Free Tile,
                                                    BW = Blocked Wall,
                                              (R, G, B, Y)C = Cube,
                                              (R, G, B, Y)B = One-way Cube,
                                              (R, G, B, Y)T = Tile

                                                    === Water ===
                                                        W = Water
                          T = Tile, I = ??, J = ??, M = Middle





                          ''').grid()



    def close_legend(*args):
        '''Closes Legend Window'''
        legend_window.destroy()

    # Bind Escape key to close the legend window
    legend_window.bind('<Escape>', close_legend)

    # Close Legend button
    close_legend_button = ttk.Button(legend_window, text="Close Legend", command=close_legend)
    close_legend_button.grid(column=0, row=0, sticky=(tk.NW))

# ------------ End Level Legend Window ------------ #


# ------------ Begin Python Version Check ------------ #

def PyVerCheck():
    '''Dummy function for easy access to Python Version Check code'''
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
    # Close Blocks
    raise SystemExit

# ------------ End Python Version Check ------------ #


# ------------ Begin Tkinter GUI Layout ------------ #

def GUI():
    '''Dummy function for easy access to GUI code'''
    pass

# Root window settings
root = tk.Tk()
root.title("{0} {1}{2}".format(app, majver, minver))
# App icon
root.iconbitmap(app_icon)

# The window cannot be resized at all
# Length x width
root.minsize("575", "300")
#root.maxsize("575", "300")

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
ttk.Label(mainframe, textvariable=level_name).grid(column=0, row=2, columnspan=2)

# Where level is viewed and edited
level = tk.Text(mainframe, height=8, width=40, wrap="none")
level.grid(column=0, row=3, sticky=(tk.N, tk.S, tk.E))
level.insert("1.0", "Minigame layout will be displayed here.")

##legend = ttk.Label(mainframe, text='''                                                   === Available Colors ===
##                                        R = Red, G = Green, B = Blue, Y = Yellow
##                                                   === Available Types ===
##                                            F = Free Tile, BW = Blocked Wall,
##                                            (R, G, B, Y)C = Cube,
##                                            (R, G, B, Y)B = One-way Cube,
##                                            (R, G, B, Y)T = Tile,
##                                                            === Water ===
##                                        WT = Water Tile, WI = ??, WJ = ??, WM = ??''')
##legend.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E))
##sticky=(tk.W, tk.E)

about_blocks = ttk.Label(mainframe, text='''                 {0} {1}{2}
    Created 2013 Triangle717'''.format(app, majver, minver))
about_blocks.grid(column=2, row=0, sticky=tk.N)

# New button
##new_button = ttk.Button(mainframe,text="New", command=read)
##new_button.grid(column=2, row=1, sticky=tk.N)
# Open button
open_file = ttk.Button(mainframe, text="Open", command=read)
open_file.grid(column=2, row=2, sticky=tk.N)
# Save button
save_file = ttk.Button(mainframe, text="Save", command=syntax_check)
save_file.grid(column=2, row=3, sticky=tk.N)
# Character Legend button
legend_button = ttk.Button(mainframe, text="Character Legend", command=the_legend)
legend_button.grid(column=0, row=0, columnspan=2)

# Blocks Logo
blocks_logo = tk.PhotoImage(file=app_logo)
image_frame = ttk.Label(mainframe)
image_frame['image'] = blocks_logo
image_frame.grid(column=2, row=3, sticky=tk.S)

# Padding around all the elements
for child in mainframe.winfo_children(): child.grid_configure(padx=2, pady=2)

def close(*args):
    '''Closes Blocks'''
    raise SystemExit

## Bind <Ctrl + n> shortcut to New button
##root.bind("<Control-n>", close)
# Bind <Ctrl + q> shortcut to Open button
root.bind("<Control-q>", read)
# Bind <Ctrl + s> shortcut to Save button
root.bind("<Control-s>", syntax_check)
# Bind escape key to close function
root.bind("<Escape>", close)
# Bind <Ctrl + l> shortcut to Character Legend button
root.bind('<Control-l>', the_legend)

# Run program
root.mainloop()

# ------------ End Tkinter GUI Layout ------------ #