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
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import levelchecks


class TestRunner(object):
    def __init__(self, loc):
        self.__fileContents = {}
        self.__filesDir = os.path.join(os.getcwd(), loc)
        self.testsSkipped = 0
        self.testsPassed = 0
        print()

    def _readLevel(self, keyName, filePath):
        """Read a level file and get its contents.

        @param filePath {string} Absolute path to the file being opened.
        @return {string} The layout contained in the file."""
        # Remove hex values, as they cannot be displayed or used
        with open(os.path.join(self.__filesDir, filePath), "rt") as f:
            levelLayout = f.readlines()[1:]
        self.__fileContents[keyName] = "".join(levelLayout)

    def xrun(self, contents, filePath, expectResult, msg):
        "Warn the test was skipped."
        print("\nIt {0}.\n".format(msg))
        print("#" * 7, "SKIP", "#" * 7)
        self.testsSkipped += 1;

    def run(self, keyName, filePath, expectResult, msg):
        "Run a test, using a simple assert to confirm it passed."
        self._readLevel(keyName, filePath)
        print("\nIt {0}.\n".format(msg))
        results = levelchecks.LevelChecks(self.__fileContents[keyName]).checkLevel()
        assert type(results) == expectResult, False
        print(results)
        print("*" * 7, "PASS", "*" * 7)
        self.testsPassed += 1;

# Create a test runner instance
runner = TestRunner("syntax-check-files")
runner.run("newLine", "line-new.txt", str, "should return the layout if the layout does have a new line")
runner.run("noNewLine", "line-new-not.txt", str, "should return the layout if the layout does NOT have a new line")
runner.run("shortLine", "line-too-short.txt", tuple, "should return an error if a line too short")
runner.run("missingLine", "line-missing.txt", tuple, "should return an error if a line is missing")
runner.run("badCharacter", "bad-character.txt", tuple, "should return an error if a the layout has an invalid character")

print("\n\n{0} success, {1} failures.".format(runner.testsPassed, runner.testsSkipped))
