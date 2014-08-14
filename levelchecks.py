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


class LevelChecks(object):
    """Run syntax checks on the user's level to ensure it is valid."""
    def __init__(self, userLevel):
        """Initalize private variables."""
        self.__userLevelNormCase = userLevel
        self.__userLevel = userLevel.upper()

    def _levelSize(self):
        """Checks the size of the layout."""
        # Get the each line's number and text
        for lineNum, lineText in enumerate(self.__userLevel[:-2].split("\n")):
            lineNum += 1

        # The level is more than or less than 8 lines
        if (lineNum > 8 or lineNum < 8):
            return (True, "Size Error!", """Your level contains {0} lines!
The level must be exactly 8 lines.""".format(lineNum))

        # No error was found
        return (False, None, None)

    def _charCheck(self):
        """Checks if each character in the layout is valid."""
        # Valid cubes that can be used
        cubeList = ("", "F", "BW", "YC", "YT", "RC", "RT",
                    "RB", "BC", "BT", "GT", "GC", "WB", "WH",
                    "WI", "WJ", "WM", "WL", "WR", "WT", "WV")

        # # Get the each character's index, removing any new lines on them
        for index, char in enumerate(self.__userLevelNormCase.split(" ")):
            char = char.strip()
            index += 1

            # If any character in the layout is not in the list
            if char.upper() not in cubeList:
                return (True, "Syntax Error!",
                        """Invalid character "{0}" at position {1}"""
                        .format(char, index))

        # No error was found
        return (False, None, None)

    def _lineLength(self):
        """Checks the length of each line."""
        # Get the each line's number text, and length
        for lineNum, lineText in enumerate(self.__userLevel[:-1].split("\n")):
            lineNum += 1
            lineLength = len(lineText)

            # If the line is less than 38 characters, counting spaces
            if lineLength < 38:
                return (True, "Line Error!", """Line {0} is {1} characters!
The line must be exactly 38 characters, including spaces.""".format(
                        lineNum, lineLength))

        # No error was found
        return (False, None, None)

        # NOTE:
        # While all lines must be at least 38 characters,
        # some levels have lines that are 39 characters.
        # Technically, a line can be longer then the imposed 38 characters,
        # but odd, undocumented stuff occurs when extra characters are added
        # to the left or right sides of the level.

    def checkLevel(self):
        """Public function to run syntax checks on a level."""
        sizeCheck = self._levelSize()
        lineCheck = self._lineLength()
        cubeCheck = self._charCheck()

        # Report any errors and return a corrected level if none were found
        if sizeCheck[0]:
            return (sizeCheck[1], sizeCheck[2])
        elif lineCheck[0]:
            return (lineCheck[1], lineCheck[2])
        elif cubeCheck[0]:
            return (cubeCheck[1], cubeCheck[2])
        return self.__userLevel[:-1]

# print(type(self.__userLevel[:-1]))
# checks = LevelChecks(blankLayout)
# checks.checkLevel()
