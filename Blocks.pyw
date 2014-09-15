#! /usr/bin/env python3
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
import webbrowser

# User is running Python 2, use that version's Tkinter
if sys.version_info[:2] < (3, 3):
    import Tkinter as tk
    import tkMessageBox

    # Display error message
    root = tk.Tk()
    root.withdraw()
    tkMessageBox.showerror("Unsupported Python Version!",
                           """You are running Python {0}.
You need to download Python 3.3.0 or newer to run Blocks."""
                           .format(sys.version[0:5]))
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
from tkinter import filedialog, messagebox

# Blocks constants and level syntax checking
import constants as const
import levelchecks
import utils


def commandLine():
    """Command-line arguments parser."""
    parser = argparse.ArgumentParser(
        description="{0} {1}{2} Command-line arguments".format(
            const.appName, const.majVer, const.minVer))

    # Debug message and file open arguments
    parser.add_argument("-d", help="Dispay debugging messages",
                        action="store_true")
    parser.add_argument("-o", help="Open a level file for editing.")

    # Register parameters
    args = parser.parse_args()
    debugArg = args.d
    openArg = args.o

    # If the debug parameter is passed, enable debugging messages
    if debugArg:
        const.debugMode = True
        if isWindows:
            os.system("title Blocks {0}{1} - Debug".format(
                const.majVer, const.minVer))
        print("\nDebug messages have been enabled.")

    # Return result of -o parameter
    return openArg


def createNewLevel(*args):
    """Create a new Minigame Level."""
    # Update variable saying a new level was created
    global newLevel
    newLevel = True

    # Remove level name display, since there is no opened level
    gui.levelName.set("")

    if const.debugMode:
        print("\nA new level is being created.")

    # Blank (free) layout for when starting a new level
    blankLayout = """ F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F"""

    # Remove the old content and display blank layout in edit box
    gui.levelArea.delete("1.0", "end")
    gui.levelArea.insert("1.0", blankLayout)


def openLevel(*args):
    """Reads Minigame Level."""
    global level_file
    level_file = filedialog.askopenfilename(
        parent=root,
        defaultextension=".TXT",
        filetypes=[("IXS Minigame Layout", ".TXT")],
        title="Select a Minigame Layout"
    )

    if level_file:
        # Display full path to the file
        if const.debugMode:
            print(level_file)

        # Send the file off for reading
        readLevel(level_file)


def readLevel(levelFile):
    """Reads an existing level file."""
    # Update new level variable to denote a pre-existing level
    global newLevel
    newLevel = False
    if const.debugMode:
        print("\nA new level is not being created.")

    # Get just the file name, assign it as global
    global level_filename
    level_filename = os.path.basename(levelFile)

    # Read the level layout
    with open(levelFile, "rt") as f:
        levelLayout = f.readlines()[:]

    # Remove binary values, as they cannot be displayed
    levelLayout = "".join(levelLayout[1:9])

    # Remove trailing new line so the syntax checking can work correctly
    levelLayout = levelLayout.rstrip()

    # Replace all text in the widget with the opened file contents
    gui.levelArea.delete("1.0", "end")
    gui.levelName.set(level_filename)
    gui.levelArea.insert("1.0", levelLayout)

    # If a temporary file was opened, delete it
    if levelFile.endswith(".bak"):
        os.unlink(levelFile)


def syntaxCheck(*args):
    """Check the Level Layout for syntax errors."""
    # Get new layout from text box, including the extra line
    # the Text Edit widget makes. This is required to make everything work
    userLevel = gui.levelArea.get("1.0", "end")

    # Run the layout through various syntax checks
    checks = levelchecks.LevelChecks(userLevel)
    userLevel = checks.checkLevel()

    # An error in the level was found, give user the details
    if type(userLevel) == tuple:
        messagebox.showerror(userLevel[0], userLevel[1])
        return False

    # Send the corrected layout for writing
    saveLevel(userLevel)


def relaunch(levelFilename, firstLine, layout):
    """
    On Windows: Prompt to load Blocks on Windows with administrator rights.
    On Mac OS X/Linux: Tell user that elevated privileges are required.
    """
    if isWindows:
        admin = messagebox.askyesno(
            "Relaunch Blocks?",
            """Would you like to reload Blocks with Administrator rights?
Your level will be preserved between launch.""")

        # If user chooses to relaunch
        if admin:
            # Save a temporary file
            tempFile = tempWrite(levelFilename, firstLine, layout)

            # Launch RunAsAdmin to reload Blocks,
            # invoke command-line parameter to reload the level
            subprocess.call(["RunAsAdmin.exe", '-o "{0}"'.format(
                tempFile)])

            # Now we close Blocks, and let RunAsAdmin take over
            logging.shutdown()
            raise SystemExit(0)

    # Mac OS X/Linux
    messagebox.showerror(
        "Insufficient Privileges!",
        """Blocks does not have sufficient privileges to save in that location.
Please choose a different location or reload Blocks with elevated privileges.
""")
    return False


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
        messagebox.showerror(
            "Insufficient User Right!",
            """Blocks does not have the user rights to save {0}!"""
            .format(level_filename))

        if const.debugMode:
            # Display traceback to console
            print(Perm)

        # Write traceback to log
        logging.exception("\nSomething went wrong! Here's what happened\n",
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
            messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
                                .format(level_filename, location))

        # A level was edited directly in Program Files or something like that,
        # and Blocks was run without Administrator rights
        except PermissionError as Perm:
            if const.debugMode:
                # Display traceback in console
                print(Perm)

            # Write traceback to log
            logging.exception("""
Something went wrong! Here's what happened
""", exc_info=True)

            # Run Admin relaunch process
            admin = relaunch(level_filename, first_line, layout)

            # The user did not want to relaunch
            if not admin:
                # Stop the saving process
                return False

        # Meaning the user the 'Cancel' button when opening a file
        # Not catching this exception would trigger Exception
        # and get stuck in an endless loop, so the level could NEVER be saved
        except FileNotFoundError as FNFE:
            if const.debugMode:
                # Display traceback in console
                print(FNFE)

            # Write traceback to log
            logging.exception("\nSomething went wrong! Here's what happened\n",
                              exc_info=True)

            # Run process to save the layout
            saveNewLevel(layout)

        # Any other unhandled error occurred
        except Exception as Exc:
            messagebox.showerror(
                "An Error Has Occurred!",
                "Blocks ran into an unknown error while trying to {0}!"
                .format(level_filename))

            if const.debugMode:
                # Display traceback in console
                print(Exc)

            # Write traceback to log
            logging.exception("n\Something went wrong! Here's what happened\n",
                              exc_info=True)

    # The user tried to save a level without loading one first
    except NameError as NE:
        if const.debugMode:
            # Display traceback in console
            print(NE)

        # Write traceback to log
        logging.exception("\nSomething went wrong! Here's what happened\n",
                          exc_info=True)

        # Run process to save the temporary layout
        saveNewLevel(layout)



def saveNewLevel(layout):
    """Save an unsaved level layout to file."""
    # File selection dialog, allows for creation of new files
    levelResave = filedialog.asksaveasfilename(
        parent=root,
        defaultextension=".TXT",
        filetypes=[("IXS Minigame Layout", ".TXT")],
        title="Save your level"
    )

    # User did not select a file
    if not levelResave:
        # Stop the saving process
        return False

    # Split the filename into name and extension
    name, ext = os.path.splitext(levelResave)

    # Append proper file extension to filename if needed
    if not levelResave.upper().endswith(".TXT"):
        levelResave = "{0}.TXT".format(levelResave)

    # Write a temporary level file, using arbitrary first line
    tempLevel = tempWrite("BlocksTempFile.txt", b"C\x01\x00\x001\r\n",
                          layout)

    # Overwrite the old level with the new one
    distutils.file_util.copy_file(tempLevel, levelResave)

    # After it is copied, delete the temporary file
    # and load the newly saved one
    os.unlink(tempLevel)
    readLevel(levelResave)


def tempWrite(tempFileName, firstLine, layout):
    """Saves the level to a temporary file."""
    # Name and location of temporary file
    path = os.path.join(os.path.expanduser("~"), tempFileName)

    # Write the temporary file, using binary mode, in the following order:
    # First line, new level, file ending
    with open(path, "wb") as f:
        f.write(firstLine)
        f.write(layout)
        f.write(b"\r\n")
    return path

class BlocksGUI(tk.Frame):

    """Tkinter-based GUI for Blocks.

    Provides public access to key visual areas including
    file name and editing area.
    """

    def __init__(self, parent, cmdFile):
        """Draw the GUI."""
        # Window settings
        tk.Frame.__init__(self, parent)
        parent.title("{0} {1}{2}".format(
            const.appName, const.majVer, const.minVer))
        parent.iconbitmap(const.appIcon)
        parent.minsize("575", "250")
        self.__mainframe = ttk.Frame(root, padding="7 7 7 7")
        self.__mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Window resizing
        parent.columnconfigure(0, weight=1)
        self.__mainframe.columnconfigure(0, weight=1)
        self.__mainframe.columnconfigure(1, weight=1)
        self.__mainframe.columnconfigure(2, weight=1)
        self.__mainframe.rowconfigure(0, weight=1)
        self.__mainframe.rowconfigure(1, weight=1)
        self.__mainframe.rowconfigure(2, weight=1)

        # Blocks Logo
        self.__blocksLogo = tk.PhotoImage(file=const.appLogo)
        self.__imageFrame = ttk.Label(self.__mainframe)
        self.__imageFrame["image"] = self.__blocksLogo
        self.__imageFrame.grid(column=2, row=3, sticky=tk.S)

        # Level (file) name display
        self.levelName = tk.StringVar()
        ttk.Label(self.__mainframe, textvariable=self.levelName).grid(
            column=0, row=2, columnspan=2)

        # Level editing area
        self.levelArea = tk.Text(self.__mainframe,
                                 height=8, width=40, wrap="none")
        self.levelArea.grid(column=0, row=3, sticky=(tk.N, tk.S, tk.E))
        self.levelArea.insert("1.0", "Minigame layout will be displayed here.")

        # About Blocks text
        self.__aboutBlocks = ttk.Label(
            self.__mainframe,
            text="""      {0} {1}{2}
Created 2013-{3}
      Triangle717""".format(const.appName, const.majVer, const.minVer,
                            const.currentYear))
        self.__aboutBlocks.grid(column=2, row=0, sticky=tk.N)

        # New, Open, Save, and Legend buttons
        self.__buttonNew = ttk.Button(self.__mainframe, text="New",
                                      command=createNewLevel)
        self.__buttonNew.grid(column=2, row=1, sticky=tk.N)
        self.__buttonOpen = ttk.Button(self.__mainframe, text="Open",
                                       command=openLevel)
        self.__buttonOpen.grid(column=2, row=2, sticky=tk.N)
        self.__buttonSave = ttk.Button(self.__mainframe, text="Save",
                                       command=syntaxCheck)
        self.__buttonSave.grid(column=2, row=3, sticky=tk.N)
        self.__buttonLegend = ttk.Button(self.__mainframe,
                                         text="Character Legend",
                                         command=self._charLegend)
        self.__buttonLegend.grid(column=0, row=1, columnspan=2, sticky=tk.N)

        # Some padding around all the elements
        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=1, pady=1)

        # Bind keyboard shortcuts
        parent.bind("<Control-n>", createNewLevel)
        parent.bind("<Control-o>", openLevel)
        parent.bind("<Control-s>", syntaxCheck)
        parent.bind("<Control-q>", self._close)
        parent.bind("<F12>", self._charLegend)

        # If the argument is a valid file, open it
        if (cmdFile is not None and os.path.isfile(cmdFile)):
            if const.debugMode:
                print("\n{0}\nis being opened for reading.".format(
                    os.path.abspath(cmdFile)))
            root.after(1, readLevel, cmdFile)

    def _close(self, *args):
        """Close Blocks."""
        logging.shutdown()
        raise SystemExit(0)

    def _charLegend(self, *args):
        """Chart stating valid cubes that can be used."""
        # Spawn a new window, parent it to main window
        self.__legendWindow = tk.Toplevel(root)
        self.__legendWindow.iconbitmap(const.appIcon)
        self.__legendWindow.title(
            "Level Character Legend - Blocks {0}{1}".format(
                const.majVer, const.minVer))

        # The window is not resizable
        self.__legendWindow.minsize("400", "260")
        self.__legendWindow.maxsize("400", "260")

        # Give it focus
        self.__legendWindow.lift()
        self.__legendWindow.focus()

        # The legend itself
        self.__legendText = """\t\t        === Available Colors ===
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
\t            WR = Bottom Left, WB = Bottom Right"""

        # Display the legend
        ttk.Label(self.__legendWindow, text=self.__legendText).grid()

        # Close button and keyboard shortcut
        buttonLegendClose = ttk.Button(self.__legendWindow, default="active",
                                       text="Close", command=self._closeLegend)
        buttonLegendClose.grid(column=1, row=1, sticky=tk.S)
        self.__legendWindow.bind("<Control-q>", self._closeLegend)

    def _closeLegend(self, *args):
        """Close cube legend window."""
        self.__legendWindow.destroy()


if __name__ == "__main__":
    # Check if we are running some version of Windows
    isWindows = False
    if "Windows" in platform.platform():
        isWindows = True

    # Start Blocks
    logger()
    root = tk.Tk()
    gui = BlocksGUI(root, commandLine())
    root.mainloop()
