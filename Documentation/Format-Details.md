Minigame Level Format Details
=============================

File Details
------------

### Known For Sure

* The levels are nothing more than plain text using ANSI encoding.
* They are located in `cdc\Z14WPO`, `cdc\Z14WPO\LEVELS`, `cdc\Z14WWH` and `cdc\Z14WWH\LEVELS`. They do not exist in any  other folders.
* They are named according to the level number in-game: `LEVEL1.TXT`, located in `Z14WWH\LEVELS`, is the first level in Jack O' Trade's store.
* It is possible to add barrier (or possibly any) block to the left edges, but they have to be offset to the other direction (more on that in [Layout Details](#layout-details). Furthermore, if a barrier block is on the left corner, and you add a block directly to its right, the game will crash.
* It is possible to place any type of block where Pepper spawns at the beginning of the level. He always starts on the seventh square on the bottom row -  directly in the middle of the row. If you put a barrier block there, he'll just spawn on it.
* It is impossible to add new rows to a level from the level file alone.

### Needs More Research

* What folders and files go to what location in-game
* They consist of 10 (ten) lines: the first is a letter, followed by the Hex values `01 00 0`, and a number. The letter and number ID something, unsure what. The next 9 lines are the level itself (laid out in a 13x8 grid). The last line is blank.
  If this last line is missing, the game will crash.
* You can add new colored blocks, but unless they were already in the level, they cannot be used. Adding new ones and pushing only one to it's proper location will complete the level.
* If a new column is added on either the left or right, the entire layout shifts, using different values. Find out excatly how many squares they move, and how to tell where they end up.
 ([Standard size](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/proof_of_concept.png), [One column added on right](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/one_new_column_on_right.png))


Layout Details
--------------

`cdc\Z14WWH\LEVELS\LEVEL3.txt`, level 3 in Jack O' Trade's store

```
C 01 00 00 1
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F BW  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F BW  F  F  F  F BW  F
 F BW BW  F  F  F  F  F BW  F  F BW BW
 F BW BW  F BW BW BW BW BW  F  F BW BW
 F  F  F  F  F  F YC  F BW  F  F  F  F
 F  F  F  F  F  F  F  F BW  F YT  F  F
 F  F BW  F  F BW  F  F  F  F  F BW BW
 
 ```

*Coming Soon.*

