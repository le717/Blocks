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
import json
import logging
import argparse
import platform
import subprocess
from PyQt5 import QtWidgets

from . import constants as const

__all__ = ("Utils")


class Utils(object):

    """Utility functions.

    Contains utility functions for Blocks, including:
    * Windows platform check
    * Logging initialization
    * Command-line paramater initialization
    * Reloading with administrator rights

    Exposes two public properties and one public method:
    * openArg {Boolean} True if the open parameter was correctly invoked.
    * isWindows {Boolean} True if the user is using the Windows platform.
    * runAsAdmin {Method} Tests for and prompts to reload
        with administrator rights.
    """

    def __init__(self):
        """Initalize public properties and run utility functions."""
        self.openArg = None
        self.isWindows = "Windows" in platform.platform()
        self._commandLine()
        self.__configData = None
        self.__configPath = self._getConfigPath()
        self.__jsonFile = os.path.join(self.__configPath, "Blocks.json")
        self._logger()
        self._loadConfig()

    def _reloadApp(self):
        """Reload Blocks with administrator rights."""
        logging.info("Reloading using RunAsAdmin")
        subprocess.call("RunAsAdmin.exe")
        logging.shutdown()
        raise SystemExit(0)

    def _getConfigPath(self):
        """Get the file path where configuration files will be stored.

        On Windows, the root folder is %AppData%, while on Mac OS X and Linux
        it is ~. On all platforms, the rest of the path is Triangle717/Blocks.

        @returns {String} The configuration path.
        """
        root = os.path.expanduser("~")
        if self.isWindows:
            root = os.path.expandvars("%AppData%")

        # Create the path if needed
        path = os.path.join(root, "Triangle717", "Blocks")
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def _loadConfig(self):
        """Read and store the configuration file.

        @returns {Boolean} True if the config file was read, False otherwise.
        """
        try:
            # Make sure it exists
            if os.path.exists(self.__jsonFile):
                logging.info("Reading config file from {0}".format(self.__jsonFile))
                with open(self.__jsonFile, "rt", encoding="utf-8") as f:
                    self.__configData = json.load(f)
                return True
            return False

        # The file is not valid JSON, sliently fail
        except ValueError:
            logging.warning("The config file is not valid!")
            return False

    def _saveConfig(self, value):
        """Write the JSON-based config file.

        @returns {Boolean} True if the config file was written,
            False otherwise.
        """
        try:
            jsonData = {"adminReload": value}
            logging.info("Writing config file to {0}".format(self.__jsonFile))
            with open(self.__jsonFile, "wt", encoding="utf_8") as f:
                f.write(json.dumps(jsonData, indent=4, sort_keys=True))
            return True

        # Silently fail
        except PermissionError:
            logging.warning("The config file could not be saved!")
            return False

    def _commandLine(self):
        """Command-line arguments parser.

        @returns {Boolean} Always returns True.
        """
        parser = argparse.ArgumentParser(
            description="{0} {1} Command-line arguments".format(
                const.appName, const.version))

        # Debug message and file open arguments
        parser.add_argument("-d", "--debug",
                            help="Dispay debugging messages",
                            action="store_true")
        parser.add_argument("-o", "--open",
                            help="Open a level file for editing.")

        # Register parameters
        args = parser.parse_args()
        debugArg = args.debug
        openArg = args.open

        # If the debug parameter is passed, enable debugging messages
        if debugArg:
            const.debugMode = True

            # Write a console title on Windows
            if self.isWindows:
                os.system("title {0} {1} - Debug".format(
                          const.appName, const.version))
            print("\nDebug messages have been enabled.")
        self.openArg = openArg
        return True

    def _logger(self):
        """Initalize the logging system.

        @returns {Boolean} Always returns True.
        """
        pythonArch = "x64"
        loggingFile = os.path.join(self.__configPath, "Blocks.log")

        # Check if Python is x86
        if sys.maxsize < 2 ** 32:
            pythonArch = "x86"

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filename=loggingFile,
            filemode="a"
        )

        logging.info("Begin logging to {0}".format(loggingFile))
        logging.info("You are running {0} {1} {2} on {3} {4}.".format(
                     platform.python_implementation(),
                     pythonArch,
                     platform.python_version(),
                     platform.machine(),
                     platform.platform())
                     )
        logging.info("""
#########################################
{0} v{1}
Created 2013-2015 {2}

If you run into a bug, open an issue at
https://github.com/le717/Blocks/issues
and attach this file for an quicker fix!
#########################################
                                    """.format(const.appName, const.version,
                                               const.creator))
        return True

    def runAsAdmin(self):
        """Check for and reload Blocks with administrator rights.

        Immediately ends if the user is running a non-Windows platform
        or the open command-line parameter was used.

        @returns {?Boolean} False if running non-Windows platform,
            is already running with administrator rights, or the user
            does not want to reload the program.
        """
        # Non-Windows platform or command-line was used
        if not self.isWindows or self.openArg is not None:
            return False

        # The program is already being run with admin rights
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            return False

        # Make sure we have data
        if self.__configData is not None:
            # If the user chose to reload, do so
            if self.__configData["adminReload"]:
                self._reloadApp()

            # Otherwise, continue on
            return False

        # Ask to reload the program
        dialog = QtWidgets.QMessageBox()
        reloadAsAdmin = dialog.question(dialog, "Reload Blocks?", "\n".join(
            ("Would you like to reload Blocks with Administrator rights?",
             "Not doing so may cause odd behavior when saving files!",
             "(You will only be asked this question once.)")))

        # No reloading is happening here
        if reloadAsAdmin != 16384:
            self._saveConfig(False)
            return False

        # Save results and reload
        self._saveConfig(True)
        self._reloadApp()
