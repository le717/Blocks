#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Blocks - Island Xtreme Stunts Minigame Level Editor
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

# Import just what is needed at the moment
import sys
import os
import webbrowser

# Blocks constants
import constants as const

# User is running Python 2, use that version's Tkinter
if sys.version_info < (3, 3, 0):
    import Tkinter as tk
    import tkMessageBox

    # Display error message
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(const.appIcon)
    tkMessageBox.showerror("Unsupported Python Version!",
                           """You are running Python {0}.
You need to download Python 3.3.0 or newer to run\n{1} {2}{3}.\n"""
                           .format(sys.version[0:5], const.app,
                                   const.majVer, const.minVer))
    webbrowser.open_new_tab("http://python.org/download/")
    raise SystemExit(0)

# Now that we know we are running Python 3.3+,
# let's import everything else we needed
import shutil
import subprocess
import argparse
import logging
import platform
import distutils.file_util

# Tkinter GUI library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import (showerror, askyesno)
import tkinter.filedialog

#TODO: Finish writing new level code

# ------------ Begin Preload Checks And Arguments ------------ #


def info():
    """Python and OS checks."""
    # Check if Python is x86 or x64
    # Based on code from Python help for platform module and my own tests
    if sys.maxsize < 2 ** 32:
        py_arch = "x86"
    else:
        py_arch = "AMD64"

    logging.info("Begin logging to {0}".format(loggingFile))
    logging.info("You are running {0} {1} {2} on {3} {4}.".format(
        platform.python_implementation(), py_arch, platform.python_version(),
        platform.machine(), platform.platform()))
    logging.info("""
                                #############################################
                                            {0} Version {1}{2}
                                          Created 2013-{3} {4}
                                                Blocks.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/Blocks/issues
                                    and attach this file for an quicker fix!
                                #############################################
                                """.format(const.app, const.majVer,
                                           const.minVer, const.currentYear,
                                           const.creator))


def commandLine():
    """Command-line arguments parser."""
    parser = argparse.ArgumentParser(
        description="{0} {1}{2} Command-line arguments".format(
            const.app, const.majVer, const.minVer))

    # Debug message argument
    parser.add_argument("-d", "--debug",
                        help="Dispay debugging messages", action="store_true")

    # Open file argument
    parser.add_argument("-o", help="""Open a level file for editing.
WARNING: any files loaded through this are deleted. Please use the Open button
in the GUI instead!""")

    # Register parameters
    args = parser.parse_args()
    debugarg = args.debug
    openarg = args.o

    # If the debug parameter is passed, enable the debugging messages
    if debugarg:
        const.debug = True
        os.system("title Blocks {0}{1} - Debug".format(
            const.majVer, const.minVer))
        print("\nDebug messages have been enabled.\n")

    # If the open argument is valid,
    if openarg is not None:
        # Open it!
        GUI(openarg)
    # Otherwise, just run Blocks.
    else:
        GUI(False)

# ------------ End Preload Checks And Arguments ------------ #


# ------------ Begin New Minigame Level ------------ #


def createNewLevel(*args):
    """Create a new Minigame Level."""
    # Update variable saying a new level was created
    global newLevel
    newLevel = True

    # Remove level name display, since there is no opened level
    level_name.set("")

    if const.debug:
        print("\nA new level is being created.\n")

    # Blank (free) layout for when starting a new level
    blank_layout = """ F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F"""

    # Remove the old content
    level.delete("1.0", "end")
    # Add blank layout in edit box
    level.insert("1.0", blank_layout)


# ------------ End New Minigame Level  ------------ #


# ------------ Begin Level Layout Opening ------------ #


def openLevel(*args):
    """Reads Minigame Level."""
    global level_file
    level_file = tkinter.filedialog.askopenfilename(
        parent=root,
        defaultextension=".TXT",
        filetypes=[("IXS Minigame Layout", ".TXT")],
        title="Select a Minigame Layout"
    )

    # The user clicked the cancel button
    if not level_file:
        # Close dialog box
        pass

    # The user selected a level
    else:
        # Display  full path to the file
        if const.debug:
            print(level_file)

        # Send the file off for reading
        readLevel(level_file)


# ------------ End Level Layout Opening ------------ #


# ------------ Begin Level Layout Reading ------------ #


def readLevel(level_file, cmd=False):
    """Reads an existing level file."""
    # Update new level variable to denote a pre-existing level
    global newLevel
    newLevel = False
    if const.debug:
        print("\nA new level is not being created.\n")

    # Get just the file name, assign it as global
    global level_filename
    level_filename = os.path.basename(level_file)

    # Set the filename display
    level_name.set(level_filename)

    # Open file for reading
    with open(level_file, "rt") as f:
        lines = f.readlines()[:]

    # Skip hex values, since they cannot be displayed
    layout = "".join(lines[1:9])

    # Remove the trailing new line so the syntax checker will work correctly
    layout = layout.rstrip("\n")

    # Remove all text in the widget
    level.delete("1.0", "end")

    # (music) Put the layout in the widget and edit it all up (music)
    level.insert("1.0", layout)

    # If the command-line parameter was invoked,
    if cmd:
        # If the temporary level exists (safety check),
        if os.path.exists(level_file):
            # Then delete it.
            os.unlink(level_file)


# ------------ End Level Layout Reading ------------ #


# ------------ Begin Level Layout Syntax Check ------------ #

# The allowed characters in a layout
# This is in the global namespace because a couple of checks reference it
blockList = ("", "F", "BW", "YC", "YT", "RC", "RT", "RB", "BC", "BT", "GT",
            "GC", "WB", "WH", "WI", "WJ", "WM", "WL", "WR", "WT", "WV")


def syntaxCheck(*args):
    """Checks the Level Layout for syntax errors."""

    # Get new layout from text box, including the extra line
    # the Text Edit widget makes. This is required to make everything work
    layout = level.get("1.0", "end")

    # Split the layout at each new line, removing the last two characters
    # This cannot be done above, it must be done here
    layout_size = layout[:-2].upper().split("\n")

    # Run level size check
    size_check = levelSize(layout_size)

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
    line_check = lineLength(line_size)

    # If the line length check returns an error,
    if line_check == "Error":
        # Return False so the saving process will not continue on
        return False

    # Delete the list to free up resources
    del line_size[:]

    # Split the text at each space
    layoutSyntax = layout.split(" ")

    # Run character check
    valid_char = charCheck(layoutSyntax)

    # If the character check returns an error,
    if valid_char == "Error":
        # Return False so the saving process will not continue on
        return False

    # Delete the list to free up resources
    del layoutSyntax[:]

    # Display final debug message for the syntax checker
    if const.debug:
        print("\n\nThe new layout (after syntax checking) is: \n\n{0}".format(
            layout))

    # Send the corrected layout for writing
    # new_layout[:-1] so the last character is not left out
    # Also convert layout to uppercase so IXS won't crash
    saveLevel(layout[:-1].upper())


# --- Begin Level Size Check --- #


def levelSize(layout_size):
    """Checks the size of the layout."""
    if const.debug:
        print("\nThe new layout is:\n")

    # Get the indices and text for each line
    for lineno, linetext in enumerate(layout_size):

        # Display line number and line content if debug messages are enabled
        if const.debug:
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
        if const.debug:
            print("""\nYour level contains {0} lines!
The level must be exactly 8 lines.""".format(lineno))

        # Display error message to user telling them about the error
        showerror("Size Error!",
                  """Your level contains {0} lines!
The level must be exactly 8 lines.\n""".format(lineno))

        # Return custom error message everything will work
        return "Error"

# --- End Level Size Check --- #


# --- Begin Line Length Check --- #


def lineLength(line_size):
    """Checks the length of each line."""
    # Bit of spacing for debug messages
    if const.debug:
        print()

    # Get the indices and text for each line
    for linenum, linedata in enumerate(line_size):

        # The actual line number
        linenum += 1

        # How long is each line?
        len_of_line = len(linedata)

        # Display length of each line if debug messages are enabled
        if const.debug:
            print("Line {0} is {1} characters long".format(
                linenum, len_of_line))

        # If the line is less than 38 characters, counting spaces
        if len_of_line < 38:

            # Tell user the error
            if const.debug:
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


def charCheck(layoutSyntax):
    """Checks if each character in the layout is valid."""
    # Get indices and text for each line
    for index, char in enumerate(layoutSyntax):

        # Remove \n, \t, and the like
        char = char.strip()

        # The proper location of the character
        index += 1

        # If any character in the layout is not in the list
        if char.upper() not in blockList:
            if const.debug:
                print('\nInvalid character "{0}" at position {1}\n'.format(
                    char, index))
            showerror("Syntax Error!",
                      'Invalid character: "{0}" at position {1}'.format(
                          char, index))

            # Return custom error message everything will work
            return "Error"


# --- End Character Syntax Check --- #


# ------------ End Level Layout Syntax Check ------------ #


# ------------ Begin RunAsAdmin Intergration ------------ #


def launch(level_filename, first_line, layout):
    """Reloads Blocks with administrator rights."""
    #FIXME: Don't run this on Mac OS X and Linux
    admin = askyesno("Relaunch Blocks?",
                     """Would you like to reload Blocks with Administrator rights?
Your level will be preserved between launch.""")

    # If user chooses to relaunch
    if admin:
        # Save a temporary file
        temp_file = tempWrite(level_filename, first_line, layout)

        # Launch RunAsAdmin to reload Blocks,
        # invoke command-line parameter to reload the level
        subprocess.call(["RunAsAdmin.exe", '-o "{0}"'.format(
            temp_file)])

        # Now we close Blocks, and let RunAsAdmin take over
        logging.shutdown()
        raise SystemExit(0)

    # User did not want to relaunch Blocks
    else:
        return False


# ------------ End RunAsAdmin Intergration ------------ #


# ------------ Begin Level Layout Saving ------------ #

def createBackup(location, backupFile):
    """Makes a backup of the level before saving."""
    # Define the name and location of the backup
    backupFile = os.path.join(location, "{0}{1}".format(
        level_filename, ".bak"))

    try:
        # Copy the file, and try to preserve time stamp
        shutil.copy2(level_file, backupFile)

    # A level was edited directly in Program Files,
    # or some other action that required Admin rights
    except PermissionError as Perm:

        showerror("Insufficient User Right!",
                  '''Blocks does not have the user rights to save {0}!'''
                  .format(level_filename))

        if const.debug:
            # Display traceback to console
            print(Perm)

        # Write traceback to log
        logging.debug("\n")
        logging.exception("Something went wrong! Here's what happened\n",
                          exc_info=True)


def saveLevel(new_layout):
    """Writes Modded Minigame Level."""
    # Convert layout from string to bytes
    layout = str.encode(new_layout, encoding="utf-8", errors="strict")

    try:

        # If a new level is being created, raise NameError so we can save it
        if const.newLevel:
            raise NameError

        # Get just the folder path to the file
        location = os.path.dirname(level_file)

        try:
            # Read original file in binary mode
            with open(level_file, "rb") as f:
                # Read just the first line
                for line in range(0, 1):
                    first_line = f.readline()

            # Run process to backup the level
            createBackup(location, level_file)

            # Open back up the original level and rewrite it
            with open(level_file, "wb") as f:
                f.write(first_line)
                f.write(layout)
                f.write(b"\r\n")

            # Display success dialog
            tk.messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
                                   .format(level_filename, location))

        # A level was edited directly in Program Files or something like that,
        # and Blocks was run without Administrator rights
        except PermissionError as Perm:
            if const.debug:
                # Display traceback in console
                print(Perm)

            # Write traceback to log
            logging.debug("\n")
            logging.exception('''Something went wrong! Here's what happened
''', exc_info=True)

            # Run Admin relaunch process
            admin = launch(level_filename, first_line, layout)

            # The user did not want to relaunch
            if not admin:
                # Stop the saving process
                return False

        # Meaning the user the 'Cancel' buttton when opening a file
        # Not catching this exception would trigger Exception
        # and get stuck in an endless loop, so the level could NEVER be saved
        except FileNotFoundError as FNFE:

            if const.debug:
                # Display traceback in console
                print(FNFE)

            # Write traceback to log
            logging.debug("\n")
            logging.exception("Something went wrong! Here's what happened\n",
                              exc_info=True)

            # Run process to save the layout
            savetheUnsaved(layout)

        # Any other unhandled error occurred
        except Exception as Exc:
            showerror("An Error Has Occurred!",
                      "Blocks ran into an unknown error while trying to {0}!"
                      .format(level_filename))

            if const.debug:
                # Display traceback in console
                print(Exc)

            # Write traceback to log
            logging.debug("\n")
            logging.exception("Something went wrong! Here's what happened\n",
                              exc_info=True)

    # The user tried to save a level without loading one first
    except NameError as NE:

        if const.debug:
            # Display traceback in console
            print(NE)

        # Write traceback to log
        logging.exception("\nSomething went wrong! Here's what happened\n",
                          exc_info=True)

        # Run process to save the temporary layout
        savetheUnsaved(layout)


# ------------ Begin New Level Saving ------------ #


def savetheUnsaved(layout):
    """Save an unsaved level layout to file."""
    # File selection dialog, allows for creation of new files
    level_resave = tk.filedialog.asksaveasfilename(
        parent=root,
        defaultextension=".TXT",
        filetypes=[("IXS Minigame Layout", ".TXT")],
        title="Save your level"
    )

    # User did not select a file
    if not level_resave:
        # Stop the saving process
        return False

    # Split the filename into name and extension
    name, ext = os.path.splitext(level_resave)

    # If file does not end with .TXT,
    if not level_resave.lower().endswith(".txt"):

        # Append proper file extension to filename
        level_resave = "{0}.TXT".format(level_resave)

    # Write a temporary level file, using arbitrary first line
    temp_level = tempWrite("BlocksTempFile.txt", b"C\x01\x00\x001\r\n",
                                                  layout)

    # Copy the temporary level over the other level
    distutils.file_util.copy_file(temp_level, level_resave)

    # After it is copied, delete the temporary file
    os.unlink(temp_level)

    # Load the newly saved level
    readLevel(level_resave)


# ------------ End New Level Saving ------------ #


# ------------ Begin Temporary Level Saving ------------ #

def tempWrite(name, first_line, layout):
    """Saves the level to a temporary file."""
    # Name and location of temporary file
    path = os.path.join(os.path.expanduser("~"), name)

    # Write the temp file, using binary mode
    with open(path, "wb") as f:
        # Rewrite the first line
        f.write(first_line)
        # Write the new layout
        f.write(layout)
        # Write the line ending
        f.write(b"\r\n")

    # Send back the path to the temporary level
    return path


# ------------ End Temporary Level Saving ------------ #


# ------------ End Level Layout Saving ------------ #


# ------------ Begin Level Legend Window ------------ #


def charLegend(*args):
    """Contains Level Character Legend."""
    # Spawn a new window, parent it to main window
    legend_window = tk.Toplevel(root)

    # Use different window title
    legend_window.title("Level Character Legend - Blocks {0}{1}".format(
                        const.majVer, const.minVer))

    # Window Icon
    legend_window.iconbitmap(const.appIcon)

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
        """Closes Character Legend Window."""
        legend_window.destroy()

    # Bind <Ctrl + q> shortcut to close the legend window
    legend_window.bind('<Control-q>', CloseCharLegend)

    # Close Legend button
    close_legend_button = ttk.Button(legend_window, default="active",
                                     text="Close", command=CloseCharLegend)
    close_legend_button.grid(column=1, row=1, sticky=tk.S)


# ------------ End Level Legend Window ------------ #


# ------------ Begin Tkinter GUI Layout ------------ #


def closeBlocks(*args):
    """Close Blocks."""
    logging.shutdown()
    raise SystemExit(0)


def GUI(cmdfile=False):
    """Tkinter GUI."""
    # Mark as global so everything works
    global root, level_name, level

    # Root window settings
    global root
    root = tk.Tk()
    root.title("{0} {1}{2}".format(const.app, const.majVer, const.minVer))

    # App window icon
    root.iconbitmap(const.appIcon)

    # The smallest size the window can be
    # Length x width
    root.minsize("575", "250")

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

    # Where level is displayed and edited
    level = tk.Text(mainframe, height=8, width=40, wrap="none")
    level.grid(column=0, row=3, sticky=(tk.N, tk.S, tk.E))
    level.insert("1.0", "Minigame layout will be displayed here.")

    # About Blocks text
    about_blocks = ttk.Label(mainframe, text="""      {0} {1}{2}
Created 2013-{3}
      Triangle717""".format(
        const.app, const.majVer, const.minVer, const.currentYear))
    about_blocks.grid(column=2, row=0, sticky=tk.N)

    # New button
    new_button = ttk.Button(mainframe, text="New", command=createNewLevel)
    new_button.grid(column=2, row=1, sticky=tk.N)

    # Open button
    open_file = ttk.Button(mainframe, text="Open", command=openLevel)
    open_file.grid(column=2, row=2, sticky=tk.N)

    # Save button
    save_file = ttk.Button(mainframe, text="Save", command=syntaxCheck)
    save_file.grid(column=2, row=3, sticky=tk.N)

    # Character Legend button
    legend_button = ttk.Button(mainframe, text="Character Legend",
                               command=charLegend)
    legend_button.grid(column=0, row=1, columnspan=2, sticky=tk.N)

    # Blocks Logo
    blocks_logo = tk.PhotoImage(file=const.appLogo)
    image_frame = ttk.Label(mainframe)
    image_frame['image'] = blocks_logo
    image_frame.grid(column=2, row=3, sticky=tk.S)

    # Padding around all the elements
    for child in mainframe.winfo_children():
        child.grid_configure(padx=2, pady=2)

    # Bind <Ctrl + n> shortcut to New button
    root.bind("<Control-n>", createNewLevel)

    # Bind <Ctrl + Shift + O> (as in, Oh!) shortcut to Open button
    root.bind("<Control-O>", openLevel)

    # Bind <Ctrl + s> shortcut to Save button
    root.bind("<Control-s>", syntaxCheck)

    # Bind <Ctrl + q> shortcut to close function
    root.bind("<Control-q>", closeBlocks)

    # Bind F12 key to Character Legend button
    root.bind('<F12>', charLegend)

    # If the argument is a valid file
    if os.path.isfile(cmdfile):
        # Open it!
        if const.debug:
            print("\n{0}\nis being opened".format(cmdfile))
        root.after(1, readLevel(cmdfile, True))

    # Run program
    root.mainloop()

# ------------ End Tkinter GUI Layout ------------ #

if __name__ == "__main__":
    # Location and name of log file
    loggingFile = os.path.join(os.path.expanduser("~"), "Blocks.log")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s : %(levelname)s : %(message)s",
        filename=loggingFile,
        filemode="a",
    )

    # Start Blocks
    info()
    commandLine()
