Minigame Level Format Details
=============================

File Details
------------

### Known For Sure

* The levels are nothing more than plain text using ANSI encoding.
* They are located in `cdc\Z14WPO`, `cdc\Z14WPO\LEVELS`, `cdc\Z14WWH` and `cdc\Z14WWH\LEVELS`. They do not exist in any other folders.
* They are named according to the level number in-game: `LEVEL1.TXT`, located in `Z14WWH\LEVELS`, is the first level in Jack O' Trade's store.
* They consist of 10 (ten) lines: the first is a letter, followed by the Hex values 01 00 00, and a number. The letter and number ID something, unsure what. The next 9 lines are the level itself (laid out in a 13x8 grid). The last line is blank.
  If this last line is missing, the game will crash.
* It is possible to add barrier (or possibly any) block to the left edges, but they have to be offset to the other direction. Furthermore, if a barrier block is on the left corner, and you add a block directly to its right, the game will crash.

### Needs More Research

* You can add new colored blocks, but unless they were already in the level, they cannot be used. Adding new ones and pushing only one to it's proper location will complete the level.
* It is possible to place a block where Pepper spawns at the beginning of the level. He always starts on the seventh square on the bottom row -  directly in the middle of the row. If you put a barrier block there, he'll just spawn on it (untested what happens if a colored block is placed there).
* Unknown if level can be made any bigger.


Layout Details
---------------

*Coming Soon.*

