Editing Tutorial
----------------
**Written by [Triangle717](https://github.com/le717)**

### Warning: This tutorial is incomplete!

This is a basic tutorial to modding the *Island Xtreme Stunts* minigame levels, and it will not cover every single detail. 
Rather, it attempts to explain the basics of the level layout, and advise you on what to and not to do in your modding.

### Requirements

You will need a few items to complete this tutorial
* A copy of [*Island Xtreme Stunts*](http://en.wikipedia.org/wiki/Island_Xtreme_Stunts), running [without the CD](http://www.rockraidersunited.org/topic/1301-)
* The newest release of **Blocks**, available in the [Downloads](https://github.com/le717/Blocks#downloads), or
* A source code editor, preferably [Notepad++](http://notepad-plus-plus.org/)

#### Legend (Incomplete)

```
Legend:
  F = Free Tile, BW = Blocked Wall, YC = Yellow Cube,  YT = Yellow Tile, 
  RC = Red Cube, RT = Red Tile, BC = Blue Cube, BT = Blue Tile
```

For this tutorial, we will be using level 3 of *Trouble in Store*, located at [`cdc\Z14WWH\LEVELS\LEVEL3.TXT`](about:blank)

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
\r\n 
```

* From looking at our [Legend](#legend-incomplete), we can see this level contains
 1. Free Tiles
 2. Blocked Walls
 3. a Yellow Tile
 4. a Yellow Cube

It also contains the code for the first and last lines of the file. We will not worry ourselves with them, 
and will instead focus on the layout itself. 

*Notice*: Sometimes, it is better to teach by example, rather than explanations. I feel this tutorial will go much more smoothly 
 if I do not purely use explanations, but use examples in addition to explaining why we do what we do. :smile:

#### Task #1 - Adding a Blocked Wall 

* The first modding example we will do is add a Blocked Wall to the layout. We remember from our Legend a Blocked Wall is signified by a `BW`.
(If you don't remember, fell free to peek back at the Legend any time you need to. :wink:)

*Coming Soon.*
