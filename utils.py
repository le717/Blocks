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
import platform

import constants as const


class Utils(object):

    def __init__(self):
        self.__pythonArch = "x64"

    def _logger(self):
        loggingFile = os.path.join(os.path.expanduser("~"),
                                   "Blocks.log")

        # Check if Python is x86
        if sys.maxsize < 2 ** 32:
            self.__pythonArch = "x86"

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filename=self.loggingFile,
            filemode="a"
        )

        logging.info("Begin logging to {0}".format(self.loggingFile))
        logging.info("You are running {0} {1} {2} on {3} {4}.".format(
                     platform.python_implementation(),
                     self.__pythonArch,
                     platform.python_version(),
                     platform.machine(),
                     platform.platform())
                    )
        logging.info("""\n        ############################################
                                              {0} Version {1}{2}
                                            Created 2013-{3} {4}
                                                  Blocks.log


                                    If you run into a bug, open an issue at
                                    https://github.com/le717/Blocks/issues
                                    and attach this file for an quicker fix!
                                  ############################################
                                    """.format(const.appName, const.majVer,
                                               const.minVer, const.currentYear,
                                               const.creator))
