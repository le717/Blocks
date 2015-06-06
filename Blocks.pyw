#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Blocks - Island Xtreme Stunts Minigame Level Editor.

Created 2013-2015 Triangle717
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
import stat
import shutil
import logging
import traceback
from PyQt5 import QtWidgets
# from PyQt5.QtGui import QFontDatabase

from src import (constants as const, linter, utils)
from ui import (main as mainUi,
                legendMain as legendMainUi,
                legendWater as legendWaterUi
                )

__all__ = ("Blocks", "UI")


class Blocks(object):

    """Core Blocks code and actions.

    Exposes four public methods:
    * createLevel {Method} Entry point to creating a new, blank level.
    * openLevel {Method} Entry point to opening an existing level.
    * openLevelAuto {Method} GUI-less entry point to opening an existing level.
    * saveLevel {Method} Entry point to saving a level.
    """

    def __init__(self, ui):
        """Initialize private properties."""
        self.__filePath = ""
        self.__fileName = ""
        self.__levelLayout = ""
        self.__firstLine = b""
        self.__newLevel = False
        self.__fileOpen = False

        self.__uiLevelName = ui.lbLevelName
        self.__uiLevelArea = ui.pteLevelArea
        self.__uiErrors = QtWidgets.QMessageBox()

    def __changePermissions(self, filePath, fileName):
        """Change a file permissions to make it writable.

        @param {String} filePath Absolute path to the file being changed.
        @param {String} fileName File name for changing.
        @return {Boolean} Returns True if the permissions could be changed,
          False otherwise.
        """
        myFile = os.path.join(filePath, fileName)
        if os.path.isfile(myFile):
            os.chmod(myFile, stat.S_IWRITE)
            return True
        return False

    def __displayError(self, title, message, trace=None):
        """Display error message dialog.

        @param {String} title Dialog error title.
        @param {String} message Dialog error message.
        @param {Exception} [trace=None] Exception alias for debugging.
        @return {Boolean} Always returns False.
        """
        # Run Exception logging only if an exception occurred
        if trace is not None:
            logging.exception("\nAn error has occurred:\n", exc_info=True)
            if const.debugMode:
                print(traceback.format_exc())

        # Otherwise, log it as an error
        else:
            logging.error("\nAn error has occurred:\n{0}".format(message))

        self.__uiErrors.critical(self.__uiErrors, title, message)
        return False

    def __readLevel(self, filePath):
        """Read a level file and get its contents.

        @param {String} filePath Absolute path to the file being opened.
        @return {String} The layout contained in the file.
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

    def __displayLevel(self, filePath, readFile):
        """Display the level name and layout in the GUI.

        It is not acceptable to call this directly,
            call openLevel() or openLevelAuto() instead.

        @param {String} filePath Absolute path to the file being opened.
        @param {Boolean} readFile True if the file needs to be read from disk.
        @return {Boolean} Always returns True.
        """
        # Read the level, get just the file
        self.__fileName = os.path.basename(filePath)
        if readFile:
            levelLayout = self.__readLevel(filePath)
        # Reuse the layout we already have
        else:
            levelLayout = self.__levelLayout

        # We are not creating a new level
        self.__newLevel = False
        if const.debugMode:
            print("\nEditing an existing level.")

        # Strip the file extension from the level name display
        fileName, extension = os.path.splitext(self.__fileName)
        if fileName.lower().endswith(".txt"):
            fileName = fileName.lower().rstrip(".txt")

        # Replace all text in the widget with the opened file contents
        self.__uiLevelName.setText(fileName)
        self.__uiLevelArea.setPlainText(levelLayout)
        return True

    def __writeFile(self, filePath, fileName, firstLine, levelLayout):
        """Write the level layout to file.

        @param {String} filePath Absolute path to the resulting file.
        @param {String} fileName File name for the resulting file.
        @param {Bytes} firstLine The first line for the file.
        @param {Bytes} levelLayout The level layout to be written.
        @return {Boolean} Always returns True;
            False if a PermissionError was hit.
        """
        try:
            # Write the file using binary mode in the following order:
            # First line, layout, file ending
            with open(os.path.join(filePath, fileName), "wb") as f:
                f.write(firstLine)
                f.write(levelLayout)
                f.write(b"\r\n ")
            return True

        # We cannot save a file in this location
        except PermissionError as p:
            if self.__newLevel:
                self.__displayError("Insufficient Privileges!",
                                    "You can't save to {0}"
                                    .format(fileName.replace("\\", "/")), p)
            return False

    def __createBackup(self, location, backupFile):
        """Make a backup of the level before saving.

        @param {String} location  Absolute path to the file being opened.
        @param {String} backupFile File name for the backup file.
        @return {Boolean} True if a backup was successfully saved;
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
            self.__displayError("Insufficient Privileges!",
                                "You can't save to {0}"
                                .format(backupFile.replace("\\", "/")), p)
            return False

    def __syntaxChecks(self, levelLayout):
        """Check the level layout for syntax errors.

        @param {Bytes} levelLayout The level layout to be written.
        @return {Boolean} False of a syntax error was found;
            level layout suitable for saving.
        """
        results = linter.Linter(levelLayout).lintLevel()

        # An error in the level was found, display the details
        if type(results) == tuple:
            if const.debugMode:
                print(results[0], results[1])
            self.__displayError(results[0], results[1])
            return False
        return results

    def __selectDestFile(self):
        """File selection dialog for new level file.

        @return {Boolean|String} Absolute path to the resulting file;
            False otherwise.
        """
        newFile = QtWidgets.QFileDialog.getSaveFileName(
            caption="Save As",
            filter="Text files (*.txt)"
        )

        if newFile[0]:
            # Uppercase the file extension
            fileName = "{0}.TXT".format(newFile[0][:-4])
            return fileName
        return False

    def __getDestDetails(self):
        """Generate the destination's file details and save backup file.

        Reuses the information if we are saving an existing file,
            and prompts for new details if we are saving a new file or
            the backup file could not be written.

        @return {List.<string|False>} Three index list containing the file's
             destination, file name, and first line if no error occurred,
             otherwise all three indexes all indexes are False.
        """
        # We need to alias these in case a new file is being written
        details = [self.__filePath, self.__fileName, self.__firstLine]

        # Ensure the file still exists
        if not os.path.exists(os.path.join(details[0], details[1])):
            self.__newLevel = True

        # We are saving a new level or
        # we are saving an existing level
        # but we don't have the permissions required
        if (self.__newLevel or
            (not self.__newLevel and not
             self.__createBackup(details[0], details[1]))):
            destFile = self.__selectDestFile()

            # The user did not select a new destination
            if not destFile:
                return (False, False, False)

            # Update the necessary values
            details[0] = os.path.dirname(destFile)
            details[1] = os.path.basename(destFile)
            details[2] = b"C\x01\x00\x001\r\n"
        return details

    def createLevel(self):
        """Create a new level layout using a layout template.

        @return {Boolean} Always returns True.
        """
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
        self.__fileOpen = True
        self.__uiLevelName.setText("")

        # Remove the old content and display blank layout in edit box
        self.__uiLevelArea.setPlainText(blankLayout)
        return True

    def openLevelAuto(self, filePath, readAgain):
        """Open a level file without a GUI dialog box.

        @param {String} filePath Absolute path to the file being opened.
        @param {Boolean} readAgain True if the file needs to be read from disk.
        @return {Boolean} Always returns True.
        """
        self.__fileOpen = True
        self.__filePath = os.path.dirname(os.path.abspath(filePath))
        self.__displayLevel(filePath, readAgain)
        return True

    def openLevel(self):
        """Display file open dialog for selecting a level file.

        @return {Boolean} True if a file was selected for opening;
            False otherwise.
        """
        filePath = QtWidgets.QFileDialog.getOpenFileName(
            caption="Open File",
            filter="Text files (*.txt)"
        )

        # A file was selected, read the layout
        if filePath[0]:
            self.openLevelAuto(filePath[0], True)
            return True
        return False

    def saveLevel(self):
        """Save the level layout.

        @return {Boolean} False if any errors occurred;
            True otherwise.
        """
        # Do not permit saving before opening a file
        if not self.__fileOpen:
            self.__displayError("No File!",
                                "You need to open a level before saving!")
            return False

        # Store the new layout
        self.__levelLayout = self.__uiLevelArea.toPlainText()

        # Check the level layout for errors
        self.__levelLayout = self.__syntaxChecks(self.__levelLayout)
        if not self.__levelLayout:
            return False

        # Get the destination details
        filePath, fileName, firstLine = self.__getDestDetails()
        if not filePath:
            return False

        # Create a bytes version of the layout for accurate writing
        binaryLayout = str.encode(self.__levelLayout, encoding="utf-8",
                                  errors="strict")

        # Change the permissions of the file to make it writable.
        # This should help reduce permission exceptions.
        self.__changePermissions(filePath, fileName)

        # Write the file to disk.
        # PermissionError handling is not needed here
        # as it is handled in writeFile()
        if self.__writeFile(filePath, fileName, firstLine, binaryLayout):
            self.__uiErrors.information(self.__uiErrors, "Success!",
                                        "Successfully saved {0} to {1}".
                                        format(fileName, filePath))
        else:
            # Could not save the file
            return False

        # Reload the level
        self.openLevelAuto(os.path.join(filePath, fileName), False)
        return True


class UI:

    """PyQt 5-based GUI for Blocks.

    Provides public access to key visual areas including
    file name and editing area.
    """

    def __init__(self, openArg):
        """Setup the GUI.

        @param {String|None} openArg Absolute path to the file being opened.
            Passing None will not invoke the automatic opening.
        """
        self.__openArg = openArg
        self.__qApp = QtWidgets.QApplication(sys.argv)
        self.__qApp.setStyle("fusion")
        self.__MainWindow = QtWidgets.QMainWindow()
        self.ui = mainUi.Ui_MainWindow()
        self.ui.setupUi(self.__MainWindow)

        # Create an instance of the back-end code
        self.__blocks = Blocks(self.ui)

        # Connect the buttons
        self.ui.btnNew.clicked.connect(self.__blocks.createLevel)
        self.ui.btnOpen.clicked.connect(self.__blocks.openLevel)
        self.ui.btnSave.clicked.connect(self.__blocks.saveLevel)

        # Connect the menu items
        self.ui.actionNew.triggered.connect(self.__blocks.createLevel)
        self.ui.actionOpen.triggered.connect(self.__blocks.openLevel)
        self.ui.actionSave.triggered.connect(self.__blocks.saveLevel)
        self.ui.actionLegendMain.triggered.connect(self.__showMainLegend)
        self.ui.actionLegendWater.triggered.connect(self.__showWaterLegend)
        # Quit menu item is connected in generated main.py

        # Display app details and run app
        self.__setDetails()
        self.__start()

    def __start(self):
        """Start the application."""
        # Show the UI
        self.__MainWindow.show()

        # If the argument is a valid file, open it
        if (self.__openArg is not None and os.path.isfile(self.__openArg)):
            if const.debugMode:
                print("\n{0}\nis being opened for reading.".format(
                    os.path.abspath(self.__openArg)))
            self.__blocks.openLevelAuto(self.__openArg, True)

        # Run the application
        init.runAsAdmin()
        self.__qApp.exec_()

    def __setDetails(self):
        """Set the program details in the GUI.

        @return {Boolean} Always returns True.
        """
        self.__MainWindow.setWindowTitle(
            self.__MainWindow.windowTitle().replace("app-name", const.appName))
        self.__MainWindow.setWindowTitle(
            self.__MainWindow.windowTitle().replace("app-ver", const.version))
        self.ui.appDetails.setText(
            self.ui.appDetails.text().replace("app-name", const.appName))
        self.ui.appDetails.setText(
            self.ui.appDetails.text().replace("app-ver", const.version))
        self.ui.appCreator.setText(
            self.ui.appCreator.text().replace("app-creator", const.creator))
        return True

    def __showMainLegend(self):
        """Display the Main Blocks Legend dialog.

        @return {Boolean} Always returns True.
        """
        dialogWindow = QtWidgets.QDialog()
        ui = legendMainUi.Ui_legendDiagMain()
        ui.setupUi(dialogWindow)
        dialogWindow.setWindowTitle(
            dialogWindow.windowTitle().replace("app-name", const.appName))
        dialogWindow.exec_()
        return True

    def __showWaterLegend(self):
        """Display the Water Blocks Legend dialog.

        @return {Boolean} Always returns True.
        """
        dialogWindow = QtWidgets.QDialog()
        ui = legendWaterUi.Ui_legendDiagWater()
        ui.setupUi(dialogWindow)
        dialogWindow.setWindowTitle(
            dialogWindow.windowTitle().replace("app-name", const.appName))
        dialogWindow.exec_()
        return True


if __name__ == "__main__":
    init = utils.Utils()
    UI(init.openArg)
