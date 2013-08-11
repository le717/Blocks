Blocks Change Log
=================

### 0.8.7.8 ###
Released ?? ??, 2013

* Fixed New Level layout size
* Added dividers for all syntax check operations
* Cleaned up method of getting correct line numbers and location of characters
* Updated titles on syntax check error boxes
* Added line length to syntax check
* Merged level size error boxes
* Improved display of About text on main window
* Split **Blocks** constants into a separate script
* Reworked Python version check, it now works as excepted
* Improved method of uppercase conversion syntax check 
* Moved list of allowed characters in a layout to the global name-space
* Split line length check into separate function
* Split level size check into separate function
* Split character check into separate function
* Fixed deletion code in temporary file creation/deletion function
* Split level backup process into separate function
* Fixed bug in line length check causing an extra space to be added after the last character in the layout
* Delete lists created by syntax checks after the check is complete to free up system resources 
* Removed writing of `\r\n` at the end of each level
* Limited number of level backups to one (1), cleaned up backup code
* Dump any errors to log
* Rewrote command-line arguments using `argparse`
* Renamed `BlocksIcon.gif` to just `Blocks.gif`
* Added open (`-o`) command-line argument, invoked when relaunching **Blocks** as Administrator (Special thanks to 
[@Anonymooseable](https://github.com/Anonymooseable) for _majorly_ helping with this by suggesting one single line of code!)
* Removed usage of `traceback` module
* Fixed Administrator relaunch and loading of temporary level save
* Save temporary level to same location as log
* Split Administrator relaunch into separate function 
* Updated error logs

### 0.8.6 ###
Released July 20, 2013

* Removed outdated comments left over from 0.8.5
* Created blank (nothing but free tiles) layout for New Level creation
* Reactivated Python Version check
* Updated `setup.py` shebang to run with Python 3.3 x86 only
* Added console window title when the ``--debug`` parameter is given
* Fixed amount of text pulled from text box before writing (it was pulling out too many spaces)
* Added level size check to syntax checker, warns about level being too big and too small
* Updated debug messages present during the syntax check
* Updated invalid character message with proper location of character
* Update method of getting location of level file
* Fixed broken messages caused by previous change
* Fixed message mistakenly displayed if the ``--debug`` parameter is not given
* Changed variables for level size checker
* Broke level file opening and reading into separate functions
* Small internal renaming and organization
* Added new `new_level` variable to keep track if a new level is being created or not
* Improved internal layout of Legend
* Updated `setup.py` to conform to PEP 8 style guidelines

### 0.8.5 ###
Released July 4, 2013

* Updated Legend to identify `F` as a `Free Tile`
* Added WT (Water Tile) to Legend (thanks Xiron)
* Added commented-out code for New button
* More of the Legend (thanks Xiron)
* Added New button, updated window size
* Bound `<Ctrl> + <n>` shortcut to New button
* Fixed error when `Save` button is pressed without opening a level first
* Convert new level layout to uppercase (partial syntax checker)
* Reworked save work flow to enable addition of layout syntax checker
* Added syntax check for each character in layout, warns if error is present
* Updated variables and comments in `write()`
* Fixed outdated comment for Save button
* Disabled New button (until code to support it can be written)
* Added debug command-line parameter (`--debug`), moved debugging messages under it
* Display complete error traceback to console if debug parameter is enabled
* Reworked GUI to better support window resizing
* Rewrote legend for better understanding, and identify the _many_ Water tiles
* Moved legend to a new window, added Character Legend button to open window in former place of legend
* Bound `<Ctrl> + <l>` shortcut to Character Legend button
* Moved conversion of level layout to uppercase after syntax checking
* Changed keyboard bindings: `<Ctrl + Shift + O>` for Open button, `<Ctrl + q>` for Close button
`F12` key for Character Legend button, `<Ctrl + q>` for Close Character Legend button
* Marked Close Character Legend button as active
* Changed method of detecting Cancel button in File Open dialog
* Finished populating Character Legend
* Removed 64-bit build from `setup.py`
* Added Linux compatible hashbang
* Decreased minimum window size
* Removed commented `root.maxsize()` line
* Updated `setup.py` to selectively copy files in `Media` folder

### 0.8.2 ###
Released May 26, 2013

* Bound `Escape` key to exit button
* Changed binding of Open button to lowercase `o` (as in, "Oh!")
* Open web browser to `http://python.org/download/` if run on any version of Python below 3.3.0
* Added script dividers 
* Bound lowercase `s` key to Save button
* Restricted selectable files for viewing to `.TXT`
* Added ability to copy selected level file, append `.bak` to it
* Added ability to update copied filename if it already exists
* Changed bindings of Open and Save buttons to `<Ctrl> + <o>` and `<Ctrl> + <s>` shortcuts, respectively. 
* Limited the amount of level file read (it pulled out two too many lines)
* Added error message if user tries to save a level without opening one first
* Resized Blocks logo, moved location of logo in program, resized program window
* Added large version of `Blocks` icon
* Compressed Blender project
* Renamed `Blocks.gif` to 'BlocksIcon.gif`
* Added ability to save edited levels
* Handled `PermissionError` exception
* Added successful save message
* Added general exception handle
* Added file name to `PermissionError` and general exception message
* Removed unneeded variable
* Lots of script comments
* Fixed bug where entire level layout was not being written to file
* Fixed bug where extra line was being written the end of the file
* Fixed bug where text box was too small to display all of the level layout
* Changed binding of Open button to `<Ctrl> + <q>` (there is a bug with `<Ctrl> + <o>` adding spaces in the text area)
* Added display of currently opened file name

### 0.5 ###
Released May 24, 2013

* Added Python 3.3.0 version check
* Full Tkinter GUI
* Application icon, created by [rioforce](http://rioforce.wordpress.com)
* Display level layout in text box, doubles as editing area
* `Return` (`Enter`) key bound to Open button
* Improved internal code
* Renamed from **The Blocker** to **Blocks**
* Added `setup.py`
* Compiled into Windows x86 and x64 Exes

### 0.1 ###
Released May 24, 2013

* First version
* Command-line style UI
* Reads and views level layouts
* Prompts for another layout
* Format legend (incomplete)