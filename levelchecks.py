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

__all__ = ("LevelChecks")


class LevelChecks(object):

    """Level syntax checker object.

    Run syntax checks on the user's level to ensure it is valid.

    Exposes one public method:
    * checkLevel {Method} Checks the level layout for syntax errors.
    """

    def __init__(self, layout):
        """Initalize syntax checks.

        @param layout {String} The level layout to be checked.
        """
        self.__layoutNormCase = layout.rstrip()
        self.__layout = layout.rstrip().upper()

    def _levelSize(self):
        """Check the size of the layout.

        @returns {Tuple.<boolean, string|None, string|None>}
            A three index tuple containing the results of the level size check.
            If there was an error, first index is True, second index
            the error dialog title, and the third the exact error message.
            Otherwise, first index is False,
            while second index and third index are both None.
        """
        # The level is not 8 lines
        numOfLines = len(self.__layoutNormCase[:-2].split("\n"))
        if (numOfLines != 8):
            return (True, "Size Error!", """Your level contains {0} lines!
The level must be exactly 8 lines.""".format(numOfLines))

        # No error was found
        return (False, None, None)

    def _charCheck(self):
        """Check if each character in the layout is valid.

        @returns {Tuple.<boolean, string|None, string|None>}
            A three index tuple containing the results
            of the valid characters check.
            If there was an error, first index is True, second index
            the error dialog title, and the third the exact error message.
            Otherwise, first index is False,
            while second index and third index are both None.
        """
        # Valid cubes that can be used
        cubeList = ("", "F", "BW", "YC", "YT", "RC", "RT",
                    "RB", "BC", "BT", "GT", "GC", "WB", "WH",
                    "WI", "WJ", "WM", "WL", "WR", "WT", "WV")

        # Get the each character's index, removing any new lines on them
        for index, char in enumerate(self.__layoutNormCase.split(" ")):
            index += 1

            char = char.strip().upper()
            # If any character in the layout is not in the list
            if char not in cubeList:
                return (True, "Syntax Error!",
                        """Invalid character "{0}" at position {1}."""
                        .format(char, index))

        # No error was found
        return (False, None, None)

    def _lineLength(self):
        """Check the length of each line.

        @returns {Tuple.<boolean, string|None, string|None>}
            A three index tuple containing the results
            of the line length check.
            If there was an error, first index is True, second index
            the error dialog title, and the third the exact error message.
            Otherwise, first index is False,
            while second index and third index are both None.
        """
        # Get the each line's length and text
        for lineNum, lineText in enumerate(self.__layoutNormCase.split("\n")):
            lineNum += 1
            lineLength = len(lineText)

            # If the line is less than 38 characters, counting spaces
            if lineLength < 38:
                return (True, "Line Error!", """Line {0} is {1} characters!
The line must be exactly 38 characters, including spaces.""".format(
                        lineNum, lineLength))

        # No error was found
        return (False, None, None)

        # TODO While all lines must be at least 38 characters,
        # some levels have lines that are 39 characters.
        # Technically, a line can be longer then the imposed 38 characters,
        # but odd, undocumented stuff occurs when extra characters are added
        # to the left or right sides of the level.
        # The checks should be revised once these anomalies are documented.

    def checkLevel(self):
        """Public method to run syntax checks on a level.

        @returns {Tuple.<string>|String} If an error was found,
            two index tuple, first index the error dialog title and the second
            the exact error message. Otherwise, a layout suitable for writing.
        """
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
        # Also strip any trailing new lines
        return self.__layout.rstrip()
