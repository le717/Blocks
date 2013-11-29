Minigame Level Format Details
=============================

File Details
------------

### Known For Sure ###

* The levels are nothing more than plain text written with [`ANSI (Windows-1252)`](http://en.wikipedia.org/wiki/Windows-1252) encoding, and can be changed to use
[`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding. Any other encodings will crash *Island Xtreme Stunts*.

* The files are located in [`cdc\Z14WPO`](about:blank), [`cdc\Z14WPO\LEVELS`](about:blank), [`cdc\Z14WWH`](about:blank), and [`cdc\Z14WWH\LEVELS`](about:blank).
They do not exist in any other folders.

* [`cdc\Z14WPO\LEVELS`](about:blank) contains the levels for the *Trouble in Store* minigame at the Post Office, and [`cdc\Z14WWH\LEVELS`](about:blank) the levels in Jack O'Trade's store.

* They are named according to the level number in-game. For example, `LEVEL1.TXT`, located in [`cdc\Z14WWH\LEVELS`](about:blank), is the first level for Jack O' Trades store.

* They consist of `10` (ten) lines: the first is a letter, followed by the Hex values `01 00 00`, and a number.
The next `9` (nine) lines are the level itself (laid out in a 13x8 grid). The last line ends with ```\r\n``` and a space.

* The first and last lines of the files can be safely removed without the game crashing.

* Files with a lowercase `.txt` will be loaded and used.

* All blocks must be indented to the left, that is, the first letter must be to the left of the other letter in a blank area.
However, blocks on the left corner must be indented to the right, with the second letter offset to the right of the other letter, also in a blank area
(more on that in [**Building With Blocks**](Tutorial.md))

* If a barrier wall is on the left corner, another barrier wall can be added directly to its right, provided the second follows the same indention.
This is possible until either the end of the row or the first block indented to the left is reached.

* It is possible to place any type of block where Pepper spawns at the beginning of the level. He always starts on the seventh square on the
 bottom row - directly in the middle of the row. If you put a barrier block there, he'll just spawn on it.

* It is impossible to add new rows to a level from the level file alone.

* If an already completed level file is broken, and the minigame is loaded, *Island Xtreme Stunts* won't crash, as it apparently does not attempt to load the level.

* If a level that has not yet been completed is broken, and that level is reached, the game will crash, as it cannot read the level file properly.

* You can add new colored blocks, but unless they were already in the level, they cannot be used. Adding new ones and pushing only the original number of blocks
to their proper location will complete the level.

* There is a special block, `RB`, that is present only in Red, and moves only to the right of the level.

* The line length for every line in a file must at least 38 characters, including spaces, but some levels in the Post Office have lines that are 39 characters,
also including spaces.

### Needs More Research ###

* What do the folders and files in the non-LEVELS folders go to in-game?
* New level slots can be added using `LEVELS.TXT`?
* The letter and number combination on the first line might identify something, but what?
* Is there a separate file that controls the number of blocks that must be moved to complete a level?
* If a new column is added on either the left or right, the entire layout shifts, using different values. Find out exactly how many squares they move, and how
to tell where they end up. ([Standard size](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/proof_of_concept.png),
[One column added on right](http://www.brickshelf.com/gallery/le717/IXS/Minigame-Modding/Jack-O-Trades/Level-3/one_new_column_on_right.png))
