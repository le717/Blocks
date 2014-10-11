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


class Blocks(object):

    def __init__(self):

        self.__levelPath = ""
        self.__levelName = ""
        self.__levelLayout = ""
        self.__firstLine = b""
        self.__newLevel = False

    def _displayError(self, title, message, traceback):
        """Display error message using a a Tkinter error dialog.

        @param title {string} Dialog error title.
        @param message {string} Dialog error message.
        @param traceback {Exception} Exception alias for debugging.
        """
        if const.debugMode:
            print(traceback)
        logging.exception("\nAn error has occurred:\n", exc_info=True)
        messagebox.showerror(title, message)
        return False

    def createLevel(self, *args):
        """Create a new level layout using a layout template."""
        # Blank (free) layout for when starting a new level
        blankLayout = """ F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F"""

        if const.debugMode:
            print("\nA new level is being created.")

        # Remove level name display, since there is no opened level
        self.__newLevel = True
        gui.levelName.set("")

        # Remove the old content and display blank layout in edit box
        gui.levelArea.delete("1.0", "end")
        gui.levelArea.insert("1.0", blankLayout)
        return True

    def _readLevel(self, levelFile):
        """Read a level file and get its contents."""
        if const.debugMode:
            print("\nA new level is not being created.")

        # Read just the first line
        with open(levelFile, "rb") as f1:
            self.__firstLine = f1.readline()

        # Remove hex values, as they cannot be displayed
        with open(levelFile, "rt") as f2:
            levelLayout = f2.readlines()[1:]
        return "".join(levelLayout)

    def _displayLevel(self, levelFile):
        """Dispay the level name and layout in the GUI.

        @param levelFile {string} Absolute path to the file being opened.
        """
        # Read the level, get just the file name
        levelLayout = self._readLevel(levelFile)
        self.__levelName = os.path.basename(levelFile)

        # We are not creating a new level
        self.__newLevel = False

        # Remove trailing new line so syntax checking can work correctly
        # TODO Move this to syntax checks
        levelLayout = levelLayout.rstrip()

        # Strip the file extension from the level name display
        fileName, extension = os.path.splitext(self.__levelName)
        if fileName.lower().endswith(".txt"):
            fileName = fileName.lower().rstrip(".txt")

        # Replace all text in the widget with the opened file contents
        gui.levelName.set(fileName)
        gui.levelArea.delete("1.0", "end")
        gui.levelArea.insert("1.0", levelLayout)

        # If a temporary file was opened, delete it
        if extension.lower() == ".bak":
            os.unlink(levelFile)
        return True

    def _writeFile(self, filePath, fileName, firstLine, layout, temporary=False):
        """Write the level layout to file.

        @param filePath {string} Absolute path to the resulting file.
        @param firstLine {bytes} The first line for the file.
        @param layout {bytes} The level layout to be written.
        @param temporary {boolean} If set to True, a temporary file will be
            created at "~".
        @return {boolean|string} True if temporary is set to False;
            the path to the temporary file.
        """
        # Name and location of the temporary file
        if temporary:
            filePath = os.path.join(os.path.expanduser("~"), fileName)

        # Write the file using binary mode in the following order:
        # First line, layout, file ending
        with open(os.path.join(filePath, fileName), "wb") as f:
            f.write(firstLine)
            f.write(layout)
            f.write(b"\r\n")

        if temporary:
            return filePath
        return True

    def _createBackup(self, location, backupFile):
        """Make a backup of the level before saving."""
        # Define the name and location of the backup
        backupFile = os.path.join(location, "{0}.bak".format(
            self.__levelName))

        try:
            # Copy the file
            shutil.copy2(os.path.join(self.__levelPath, self.__levelName), backupFile)
            return True

        # A level was edited directly in Program Files
        # or some other action that requires Administrator rights
        except PermissionError as p:
            self._displayError("Insufficient User Right!",
                               "Blocks does not have the user rights to save {0}!"
                               .format(levelFileName), p)
            return False

    def _syntaxCheck(self):
        """Check the level layout for syntax errors."""
        results = levelchecks.LevelChecks(self.__levelLayout).checkLevel()

        # An error in the level was found, display the details
        if type(results) == tuple:
            messagebox.showerror(results[0], results[1])
            return False
        return True

    def openLevel(self, *args):
        """Display Tkinter open dialog for selecting a level file."""
        filePath = filedialog.askopenfilename(
          parent=root,
          defaultextension=".TXT",
          filetypes=[("IXS Minigame Layout", ".TXT")],
          title="Select a Minigame Layout"
        )

        # A file was selected, read the layout
        if filePath:
            self.__levelPath = os.path.dirname(filePath)
            self._displayLevel(filePath)
            return True

    def saveLevel(self, *args):

        # Get new layout from text box, including the extra line
        # the Text Edit widget makes. This is required to make everything work.
        # TODO Is the above statement still true?
        levelLayout = gui.levelArea.get("1.0", "end")

        # Store the layout for usage elsewhere
        self.__levelLayout = levelLayout

        # TODO General Exception handling

        # The syntax checks passed
        if self._syntaxCheck():
            # TODO New level saving
            # if self.__newLevel:

            # Create a backup
            if self._createBackup(self.__levelPath, self.__levelName):

                # Create a bytes version of the layout for accurate writing
                binaryLayout = str.encode(self.__levelLayout, encoding="utf-8", errors="strict")

                # Write the file to disc.
                # PermissionError Exception handling is not needed here,
                # for if a backup cannot be written, the new file
                # certainly cannot be written.
                self._writeFile(self.__levelPath, self.__levelName, self.__firstLine, binaryLayout)
                messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
                                .format(self.__levelName, self.__levelPath))
                return True

            # TODO We've hit a PermissionError, prompt to reload using RunAsAdmin.
            else:
                return False

def relaunch(levelFilename, firstLine, layout):
    """
    On Windows: Prompt to reload with administrator rights.
    On Mac OS X/Linux: Tell user that elevated privileges are required.
    # TODO: Is this still required with Python 3.4 and later versions of 3.3?
    """
    if isWindows:
        admin = messagebox.askyesno(
            "Relaunch Blocks?",
            """Would you like to reload Blocks with Administrator rights?
Your level will be preserved between launch.""")

        # If user chooses to relaunch
        if admin:
            # Save a temporary file
            tempFile = self._writeFile(levelFilename, firstLine, layout, True)

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
            self._writeFile(level_file, firstLine, layout)

            # Display success dialog
            messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
                                .format(levelFileName, location))

        # A level was edited directly in Program Files or something like that,
        # and Blocks was run without Administrator rights
        except PermissionError as p:
            if const.debugMode:
                # Display traceback in console
                print(p)

            # Write traceback to log
            logging.exception("""
Something went wrong! Here's what happened
""", exc_info=True)

            # Run Admin relaunch process
            admin = relaunch(levelFileName, first_line, layout)

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
                .format(levelFileName))

            # Display traceback in console, write to log
            logging.exception("n\Something went wrong! Here's what happened\n",
                              exc_info=True)
            if const.debugMode:
                print(Exc)

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
        return False

    # Append proper file extension to filename if needed
    if not levelResave.lower().endswith(".txt"):
        levelResave = "{0}.TXT".format(levelResave)

    # Write a temporary level file using arbitrary first line
    tempLevel = self._writeFile("BlocksTempFile.txt", b"C\x01\x00\x001\r\n",
                          layout, True)

    # Overwrite the old level with the new one
    distutils.file_util.copy_file(tempLevel, levelResave)

    # After it is copied, delete the temporary file
    # and load the newly saved one
    os.unlink(tempLevel)
    _readLevel(levelResave)


class BlocksGUI(tk.Frame):

    """Tkinter-based GUI for Blocks.

    Provides public access to key visual areas including
    file name and editing area.
    """

    def __init__(self, parent, cmdFile):
        """Draw the GUI."""
        # Create an instance of the backend code
        blocks = Blocks()

        # Window settings
        tk.Frame.__init__(self, parent)
        parent.title("{0} {1}".format(
            const.appName, const.version))
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
            text="""      {0} {1}
Created 2013-{2}
      Triangle717""".format(const.appName, const.version,
                            const.currentYear))
        self.__aboutBlocks.grid(column=2, row=0, sticky=tk.N)

        # New, Open, Save, and Legend buttons
        self.__buttonNew = ttk.Button(self.__mainframe, text="New",
                                      command=blocks.createLevel)
        self.__buttonNew.grid(column=2, row=1, sticky=tk.N)
        self.__buttonOpen = ttk.Button(self.__mainframe, text="Open",
                                       command=blocks.openLevel)
        self.__buttonOpen.grid(column=2, row=2, sticky=tk.N)
        self.__buttonSave = ttk.Button(self.__mainframe, text="Save",
                                       command=blocks.saveLevel)
        self.__buttonSave.grid(column=2, row=3, sticky=tk.N)
        self.__buttonLegend = ttk.Button(self.__mainframe,
                                         text="Character Legend",
                                         command=self._charLegend)
        self.__buttonLegend.grid(column=0, row=1, columnspan=2, sticky=tk.N)

        # Some padding around all the elements
        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=1, pady=1)

        # Bind keyboard shortcuts
        parent.bind("<Control-n>", blocks.createLevel)
        parent.bind("<Control-o>", blocks.openLevel)
        parent.bind("<Control-s>", blocks.saveLevel)
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
            "Level Character Legend - Blocks {0}".format(
                const.version))

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
    init = utils.Utils()
    isWindows = init.isWindows
    root = tk.Tk()
    gui = BlocksGUI(root, init.openArg)
    root.mainloop()
