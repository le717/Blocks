Minigame Level Format Details
=============================

File Details
------------

### Known For Sure

* The levels are nothing more than plain text written with [`ANSI (Windows-1252)`](http://en.wikipedia.org/wiki/Windows-1252) encoding, and can be changed to use [`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding. Any other encodings will crash the game.
* They are located in `cdc\Z14WPO`, `cdc\Z14WPO\LEVELS`, `cdc\Z14WWH` and `cdc\Z14WWH\LEVELS`. They do not exist in any  other folders.
* They are named according to the level number in-game: `LEVEL1.TXT`, located in `Z14WWH\LEVELS`, is the first level for *Trouble in Store*.
* They consist of `10` (ten) lines: the first is a letter, followed by the Hex values `01 00 00`, and a number. 
  The next `9` (nine) lines are the level itself (laid out in a 13x8 grid). The last line ends with ```\r\n``` and a space.
* All blocks must be indented to the left, that is, the first letter must be to the left of the other letter in a blank area. However, blocks on the left corner must be indented to the right,
 with the second letter offset to the right of the other letter, also in a blank area (more on that in the
 [Editing Tutorial](#editing-tutorial))
* If a barrier block is on the left corner, and a block is added directly to its right, the game will crash.
* It is possible to place any type of block where Pepper spawns at the beginning of the level. He always starts on the seventh square on the 
 bottom row - directly in the middle of the row. If you put a barrier block there, he'll just spawn on it.
* It is impossible to add new rows to a level from the level file alone.

### Needs More Research

* What folders and files go to what location in-game
* Creating new level slots
* The letter and number combonation on the first line identify something, but what.
* You can add new colored blocks, but unless they were already in the level, they cannot be used. Adding new ones and pushing only one to it's proper location 
will complete the level.
* If a new column is added on either the left or right, the entire layout shifts, using different values. Find out exactly how many squares they move, and how 
to tell where they end up. ([Standard size](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/proof_of_concept.png), 
[One column added on right](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/one_new_column_on_right.png))


Editing Tutorial
----------------

This is a basic tutorial to modding the *Island Xtreme Stunts* minigame levels. It will not cover every detail. 
Rather, it attempts to explain the basics, and advice you on what to and not to do.

### Legend (Incomplete)

```
Legend:
  F = free block, BW = Blocked Wall, YC = Yellow Cube,  YT = Yellow Tile, 
  RC = Red Cube, RT = Red Tile, BC = Blue Cube, BT = Blue Tile
```

For this tutorial, we will use level 3 of *Trouble in Store*, located at `cdc\Z14WWH\LEVELS\LEVEL3.TXT` 

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

