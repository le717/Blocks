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
# import json
import logging
import argparse
import platform
import subprocess
import tkinter as tk

import constants as const


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
    * runAsAdmin() TODO.
    """

    def __init__(self):
        """Initalize public properties and run utility functions."""
        self.openArg = False
        self.isWindows = False
        self._logger()
        self._checkWindows()
        self._commandLine()

    def _checkWindows(self):
        """Check if we are running some version of Windows.

        @returns {Boolean} Always returns True.
        """
        if "Windows" in platform.platform():
            self.isWindows = True
        return True

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
                os.system("title Blocks {0} - Debug".format(
                    const.version))
            print("\nDebug messages have been enabled.")
        self.openArg = openArg
        return True

    def _logger(self):
        """Initalize the logging system.

        @returns {Boolean} Always returns True.
        """
        pythonArch = "x64"
        loggingFile = os.path.join(os.path.expanduser("~"),
                                   "Blocks.log")

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
\t\t\t\t\t\t\t      ############################################
                                              {0} Version {1}
                                            Created 2013-2014 {2}


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/Blocks/issues
                                    and attach this file for an quicker fix!
\t\t\t\t\t\t\t      ############################################
                                    """.format(const.appName, const.version,
                                               const.creator))
        return True

    def runAsAdmin(self):
        """Check for and reload Blocks with administrator rights.

        Immediately ends if the user is running a non-Windows platform.

        @returns {?Boolean} False if running non-Windows platform,
            is already running with administrator rights, or the user
            does not want to reload the program.
        """
        # Non-Windows platform
        if not self.isWindows:
            return False

        # We only need the ctypes module on Windows
        import ctypes

        # The program is already being run with admin rights
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            return False

        # TODO Check if the user has answered this question already
        # Ask to reload the program
        root = tk.Tk()
        root.withdraw()
        reloadAsAdmin = tk.messagebox.askyesno("Reload Blocks?",
        """Would you like to reload Blocks with Administrator rights?
 Not doing so may cause odd behavior when saving files!
 (You will only be asked this question once.)""")
        root.destroy()

        # No reloading is happening here
        if not reloadAsAdmin:
            return False

        # If user wants to reload, invoke RunAsAdmin
        subprocess.call("RunAsAdmin.exe")

        # Close program and let RunAsAdmin take over
        logging.shutdown()
        raise SystemExit(0)
