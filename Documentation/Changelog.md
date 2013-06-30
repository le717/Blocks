Blocks Change Log
=================

### 0.8.2.2
Released ?? ??, 2013

* Updated Legend to identify `F` as a `Free Tile`
* Added WT (Water Tile) to Legend (thanks Xiron)
* Added commented-out code for New button
* More of the Legend (thanks Xiron)
* Added New button, updated window size
* Bound `<Ctrl> + <n>` shortcut to New button
* Fixed error when `Save` button is pressed without opening a level first
* Convert new level layout to uppercase (syntax check)

### 0.8.2
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

### 0.5 
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

### 0.1
Released May 24, 2013

* First version
* Command-line style UI
* Reads and views level layouts
* Prompts for another layout
* Format legend (incomplete)
