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
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Blocks. If not, see <http://www.gnu.org/licenses/>.

"""

import os
import sys
import webbrowser

try:
    # Python 3 Tkinter
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog, messagebox
except ImportError:
    # Python 2 Tkinter
    import Tkinter as tk
    import tkMessageBox as messagebox

# User is running < Python 3.3.0
if sys.version_info[:2] < (3, 3):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Unsupported Python Version!",
                         """You are running Python {0}.
You need to download Python 3.3.0 or newer to run Blocks."""
                         .format(sys.version[0:5]))
    webbrowser.open_new_tab("http://python.org/download/")
    raise SystemExit(0)

# Now that we know we are running Python 3.3+,
# let's import everything else we needed
import stat
import shutil
import logging
import traceback

# Blocks-specific modules
import utils
import levelchecks
import constants as const


class Blocks(object):

    """Core Blocks code and actions.

    Exposes four public methods:
    * createLevel: Entry point to creating a new, blank level.
    * openLevel: Entry point to opening an existing level.
    * openLevelAuto: GUI-less entry point to opening an existing level.
    * saveLevel: Entry point to saving a level.
    """

    def __init__(self):
        """Initialize private properties."""
        self.__filePath = ""
        self.__fileName = ""
        self.__levelLayout = ""
        self.__firstLine = b""
        self.__newLevel = False

    def _changePermissions(self, filePath, fileName):
        """Change a file permissions to make it writable.

        @param filePath {String} Absolute path to the file being changed.
        @param fileName {String} File name for changing.
        @returns {Boolean} Returns True if the permissions could be changed,
          False otherwise.
        """
        myFile = os.path.join(filePath, fileName)
        if os.path.isfile(myFile):
            os.chmod(myFile, stat.S_IWRITE)
            return True
        return False

    def _displayError(self, title, message, trace=None):
        """Display error message using a a Tkinter error dialog.

        @param title {String} Dialog error title.
        @param message {String} Dialog error message.
        @param trace {Exception} Exception alias for debugging.
        @returns {Boolean} Always returns False.
        """
        # Run Exception logging only if an exception occurred
        if trace is not None:
            logging.exception("\nAn error has occurred:\n", exc_info=True)
            if const.debugMode:
                print(traceback.format_exc())

        # Otherwise, log it as an error
        else:
            logging.error("\nAn error has occurred:\n{0}".format(message))

        messagebox.showerror(title, message)
        return False

    def _readLevel(self, filePath):
        """Read a level file and get its contents.

        @param filePath {String} Absolute path to the file being opened.
        @returns {String} The layout contained in the file.
        """
        if const.debugMode:
            print("\nA new level is not being created.")

        # Read just the first line
        with open(filePath, "rb") as f1:
            self.__firstLine = f1.readline()

        # Remove hex values, as they cannot be displayed
        with open(filePath, "rt") as f2:
            levelLayout = f2.readlines()[1:]
        return "".join(levelLayout)

    def _displayLevel(self, filePath, readFile):
        """Display the level name and layout in the GUI.

        It is not acceptable to call this directly,
            access this by calling openLevelAuto() instead.

        @param filePath {String} Absolute path to the file being opened.
        @param readFile {Boolean} True if the file needs to be read from disk.
        @returns {Boolean} Always returns True.
        """
        # Read the level, get just the file name
        self.__fileName = os.path.basename(filePath)
        if readFile:
            levelLayout = self._readLevel(filePath)
        # Reuse the layout we already have
        else:
            levelLayout = self.__levelLayout

        # We are not creating a new level
        self.__newLevel = False

        # Strip the file extension from the level name display
        fileName, extension = os.path.splitext(self.__fileName)
        if fileName.lower().endswith(".txt"):
            fileName = fileName.lower().rstrip(".txt")

        # Replace all text in the widget with the opened file contents
        gui.levelName.set(fileName)
        gui.levelArea.delete("1.0", "end")
        gui.levelArea.insert("1.0", levelLayout)

        # If a temporary file was opened, delete it
        if extension.lower() == ".tmp":
            os.unlink(filePath)
        return True

    def _writeFile(self, filePath, fileName, firstLine,
                   levelLayout, temporary=False):
        """Write the level layout to file.

        @param filePath {String} Absolute path to the resulting file.
        @param fileName {String} File name for the resulting file.
        @param firstLine {Bytes} The first line for the file.
        @param levelLayout {Bytes} The level layout to be written.
        @param temporary {Boolean} If set to True, a temporary file will be
            created at "~".
        @returns {Boolean|String} True if temporary is set to False;
            Path to the temporary file if temporary is set to True;
            False if a PermissionError was hit.
        """
        # Name and location of the temporary file
        if temporary:
            filePath = os.path.join(os.path.expanduser("~"),
                                    "{0}.tmp".format(fileName))

        try:
            # Write the file using binary mode in the following order:
            # First line, layout, file ending
            with open(os.path.join(filePath, fileName), "wb") as f:
                f.write(firstLine)
                f.write(levelLayout)
                f.write(b"\r\n")

            if temporary:
                return filePath
            return True

        # We cannot save a file in this location
        except PermissionError as p:
            if self.__newLevel:
                self._displayError("Insufficient Privileges!",
                                   "You can't save to {0}"
                                   .format(fileName.replace("\\", "/")), p)
            return False

    def _createBackup(self, location, backupFile):
        """Make a backup of the level before saving.

        @param location {String} Absolute path to the file being opened.
        @param backupFile File name for the backup file.
        @returns {Boolean} True if a backup was successfully saved;
            False if a PermissionError was hit.
        """
        # Define the name and location of the backup
        backupFile = os.path.join(location, "{0}.bak".format(
            self.__fileName))

        try:
            # Copy the file
            shutil.copy2(os.path.join(self.__filePath, self.__fileName),
                         backupFile)
            return True

        # We cannot save a file in this location
        except PermissionError as p:
            self._displayError("Insufficient Privileges!",
                               "You can't save to {0}"
                               .format(backupFile.replace("\\", "/")), p)
            return False

    def _syntaxChecks(self, levelLayout):
        """Check the level layout for syntax errors.

        @param levelLayout {Bytes} The level layout to be written.
        @returns {Boolean} False of a syntax error was found;
            level layout suitable for saving.
        """
        results = levelchecks.LevelChecks(levelLayout).checkLevel()

        # An error in the level was found, display the details
        if type(results) == tuple:
            if const.debugMode:
                print(results[0], results[1])
            self._displayError(results[0], results[1])
            return False
        return results

    def _selectDestFile(self):
        """File selection dialog for new level file.

        @returns {Boolean|String} Absolute path to the resulting file;
            False otherwise.
        """
        newFile = filedialog.asksaveasfilename(
            parent=root,
            defaultextension=".TXT",
            filetypes=[("IXS Minigame Layout", ".TXT")],
            title="Save As"
        )

        if newFile:
            # Append proper file extension to file name if needed
            if not newFile.lower().endswith(".txt"):
                newFile = "{0}.TXT".format(newFile)
            return newFile
        return False

    def _getDestDetails(self):
        """Generate the destination's file details and save backup file.

        Reuses the information if we are saving an existing file,
            and prompts for new details if we are saving a new file or
            the backup file could not be written.

        @returns {Tuple.<string>} Three index tuple containing the file's
             destination, fie nanme, and first line.
        """
        # We need to alias these in case a new file is being written
        details = (self.__filePath, self.__fileName, self.__firstLine)

        # We are saving a new level or
        # we are saving an existing level
        # but we don't have the permissions required
        if (self.__newLevel or
            (not self.__newLevel and not
             self._createBackup(details[0], details[1]))):
            destFile = self._selectDestFile()

            # The user did not select a new destination
            if not destFile:
                return False

            # Update the necessary values
            details[0] = os.path.dirname(destFile)
            details[1] = os.path.basename(destFile)
            details[2] = b"C\x01\x00\x001\r\n"
        return details

    def createLevel(self, *args):
        """Create a new level layout using a layout template.

        @returns {Boolean} Always returns True.
        """
        # Blank (free) layout for when starting a new level
        blankLayout = """ F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F\n"""

        if const.debugMode:
            print("\nA new level is being created.")

        # Remove level name display, since there is no opened level
        self.__newLevel = True
        gui.levelName.set("")

        # Remove the old content and display blank layout in edit box
        gui.levelArea.delete("1.0", "end")
        gui.levelArea.insert("1.0", blankLayout)
        return True

    def openLevelAuto(self, filePath, readAgain):
        """Open a level file without a GUI dialog box.

        @param filePath {String} Absolute path to the file being opened.
        @param readAgain {Boolean} True if the file needs to be read from disk.
        @returns {Boolean} Always returns True.
        """
        self.__filePath = os.path.dirname(os.path.abspath(filePath))
        self._displayLevel(filePath, readAgain)
        return True

    def openLevel(self, *args):
        """Display Tkinter open dialog for selecting a level file.

        @returns {Boolean} True if a file was selected for opening;
            False otherwise.
        """
        filePath = filedialog.askopenfilename(
            parent=root,
            defaultextension=".TXT",
            filetypes=[("IXS Minigame Layout", ".TXT")],
            title="Open"
        )

        # A file was selected, read the layout
        if filePath:
            self.openLevelAuto(filePath, True)
            return True
        return False

    def saveLevel(self, *args):
        """Save the level layout.

        @returns {Boolean} False if any errors occurred;
            True otherwise.
        """
        # Get and store the new layout
        levelLayout = gui.levelArea.get("1.0", "end")
        self.__levelLayout = levelLayout

        # Get the destination details
        filePath, fileName, firstLine = self._getDestDetails()

        # Check the level layout for errors
        levelLayout = self._syntaxChecks(levelLayout)
        if not levelLayout:
            return False
        else:
            # Create a bytes version of the layout for accurate writing
            binaryLayout = str.encode(levelLayout, encoding="utf-8",
                                      errors="strict")

            # Change the permissions of the file to make it writable.
            # This should help reduce permission exceptions.
            self._changePermissions(filePath, fileName)

            # Write the file to disk.
            # PermissionError handling is not needed here,
            # as it is handled in _writeFile()
            if self._writeFile(filePath, fileName, firstLine, binaryLayout):
                messagebox.showinfo("Success!", "Successfully saved {0} to {1}"
                                    .format(fileName, filePath))
            else:
                # Could not save the file
                return False

            # Reload the level
            self.openLevelAuto(os.path.join(filePath, fileName), False)
            return True


class BlocksGUI(tk.Frame):

    """Tkinter-based GUI for Blocks.

    Provides public access to key visual areas including
    file name and editing area.

    @param parent {Tkinter} Tkinter frame all elements to which are parented.
    @param cmdFile {String|None} Absolute path to the file being opened.
        Passing None will not invoke the automatic opening.
    """

    def __init__(self, parent, cmdFile):
        """Draw the GUI."""
        # Create an instance of the back-end code
        blocks = Blocks()

        # Window settings
        tk.Frame.__init__(self, parent)
        parent.title("{0} {1}".format(
            const.appName, const.version))
        parent.iconbitmap(const.appIcon)
        parent.minsize("575", "250")
        self.__mainframe = ttk.Frame(root, padding="7 7 7 7")
        self.__mainframe.grid(column=0, row=0,
                              sticky=(tk.N, tk.W, tk.E, tk.S))

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
        self.levelArea.insert("1.0",
                              "Minigame layout will be displayed here.")

        # About Blocks text
        self.__aboutBlocks = ttk.Label(
            self.__mainframe,
            text="""      {0} {1}
Created 2013-2014
      Triangle717""".format(const.appName, const.version))
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
        self.__buttonLegend.grid(column=0, row=0, columnspan=2, rowspan=1,
                                 sticky=(tk.N, tk.S))

        # Some padding around all the elements
        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=1, pady=1)

        # Bind keyboard shortcuts
        parent.bind("<Control-n>", blocks.createLevel)
        parent.bind("<Control-O>", blocks.openLevel)
        parent.bind("<Control-s>", blocks.saveLevel)
        parent.bind("<Control-q>", self._close)
        parent.bind("<F12>", self._charLegend)

        # If the argument is a valid file, open it
        if (cmdFile is not None and os.path.isfile(cmdFile)):
            if const.debugMode:
                print("\n{0}\nis being opened for reading.".format(
                    os.path.abspath(cmdFile)))
            root.after(1, blocks.openLevelAuto, cmdFile, True)

    def _close(self, *args):
        """Close Blocks."""
        logging.shutdown()
        raise SystemExit(0)

    def _closeLegend(self, *args):
        """Close character legend window."""
        self.__legendWindow.destroy()

    def _charLegend(self, *args):
        """Chart listing valid cubes that can be used."""
        # Spawn a new window, parent it to main window
        self.__legendWindow = tk.Toplevel(root)
        self.__legendWindow.iconbitmap(const.appIcon)
        self.__legendWindow.title(
            "Level Character Legend - Blocks {0}".format(
                const.version))

        # The dialog is not resizable
        self.__legendWindow.minsize("400", "260")
        self.__legendWindow.maxsize("400", "260")

        # Give it focus
        self.__legendWindow.lift()
        self.__legendWindow.focus()

        # The legend itself
        # TODO I hate this layout, ask for revision help
        self.__legendText = """\t\t        === Available Colors ===
\t              R = Red, G = Green, B = Blue, Y = Yellow

\t\t        === Available Types ===
\t\t\t  F = Free Tile,
\t\t              BW = Blocked Wall,
\t\t            (R, G, B, Y)C = Cube,
\t\t            (R, G, B, Y)T = Tile,
\t\tRB = One way, west-bound Red Cube

\t\t\t=== Water ===
\t        WH = Small Horizontal, WV = Small Vertical,
\t            WI = Top, WJ = Left, WM = Right,
\t            WT = Top Left, WL = Top Right,
\t            WR = Bottom Left, WB = Bottom Right"""

        # Display the legend
        ttk.Label(self.__legendWindow, text=self.__legendText).grid()

        # Close button and keyboard shortcut
        buttonLegendClose = ttk.Button(self.__legendWindow,
                                       default="active", text="Close",
                                       command=self._closeLegend)
        buttonLegendClose.grid(column=1, row=1, sticky=tk.S)
        self.__legendWindow.bind("<Control-q>", self._closeLegend)


if __name__ == "__main__":
    init = utils.Utils()
    # Before we do anything, we need to check for administrator rights
    init.runAsAdmin()
    root = tk.Tk()
    gui = BlocksGUI(root, init.openArg)
    root.mainloop()
