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
import logging
import argparse
import platform

import constants as const


class Utils(object):

    """Utility functions.

    Contains utility functions for Blocks, including:
    * Windows platform check
    * Logging initialization
    * Command-line paramater initialization

    Exposes two public properties:
    * isWindows {boolean} True if the user is using the Windows platform.
    * openArg {boolean} True if the open parameter was correctly invoked.
    """

    def __init__(self):
        """Initalize public properties and run utility functions."""
        self.isWindows = False
        self.openArg = False
        self._logger()
        self._checkWindows()
        self._commandLine()

    def _checkWindows(self):
        """Check if we are running some version of Windows."""
        if "Windows" in platform.platform():
            self.isWindows = True
        return True

    def _commandLine(self):
        """Command-line arguments parser."""
        parser = argparse.ArgumentParser(
            description="{0} {1} Command-line arguments".format(
                const.appName, const.version))

        # Debug message and file open arguments
        parser.add_argument("-d", help="Dispay debugging messages",
                            action="store_true")
        parser.add_argument("-o", help="Open a level file for editing.")

        # Register parameters
        args = parser.parse_args()
        debugArgu = args.d
        openArgu = args.o

        # If the debug parameter is passed, enable debugging messages
        if debugArgu:
            const.debugMode = True
            # Write a console title on Windows
            if self.isWindows:
                os.system("title Blocks {0} - Debug".format(
                    const.version))
            print("\nDebug messages have been enabled.")
        self.openArg = openArgu
        return True

    def _logger(self):
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
                                            Created 2013-{2} {3}
                                                  Blocks.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/Blocks/issues
                                    and attach this file for an quicker fix!
\t\t\t\t\t\t\t      ############################################
                                    """.format(const.appName, const.version,
                                               const.currentYear,
                                               const.creator))
        return True
