Modding Tutorial
================
**Written by [Triangle717](https://github.com/le717)**

### Warning: This tutorial is incomplete!

## Table of Contents
<table>
<td>[Requirements](#requirements)</td>
<td>[Legend](#legend-incomplete)</td>
<td>[Task #1](#task-1-adding-a-blocked-wall</td>
<td>[Lesson #1](#lesson-1-alignment)</td>
<td>[Task #2](#task-2-adding-a-blocked-wall-on-the-left-corner)</td>
</table>

This is a tutorial on modding the *Island Xtreme Stunts* minigame levels. It is a basic tutorial, and will not cover every single detail. 
Instead, it attempts to explain the basics of the level layout, and advise you on what to and not to do in your modding.

## Requirements

You will need a few items to complete this tutorial
* A copy of [*Island Xtreme Stunts*](http://en.wikipedia.org/wiki/Island_Xtreme_Stunts), running [without the CD](http://www.rockraidersunited.org/topic/1301-)
* The newest release of **Blocks**, available in the [Downloads](https://github.com/le717/Blocks#downloads), or
* A source code editor, preferably [Notepad++](http://notepad-plus-plus.org)
* The minigame level format details, available in [Format-Details.md](Format-Details.md)

### Legend (Incomplete)

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

From looking at our [Legend](#legend-incomplete), we can see this level contains
 1. Free Tiles
 2. Blocked Walls
 3. a Yellow Tile
 4. a Yellow Cube
 
You may notice it also contains the code for the first and last lines of the file. We will not worry ourselves with them, 
and will instead focus on the layout itself. 

Sometimes, it is better to teach by example, rather than explanations. I feel this tutorial will go much more smoothly 
if I do not purely use explanations, but use examples in addition to explaining why we do what we do. :smile:

### Task #1: Adding a Blocked Wall 

The first modding example we will do is add a Blocked Wall to the layout. We remember from our Legend a Blocked Wall is signified by a `BW`.
(If you don't remember, fell free to peek back at the Legend any time you need to. :wink:) To start, we are going to add a Blocked Wall on 
the top row, on the 8th column. However, before we add our wall, we need to speak a bit on alignment.

#### Lesson #1: Alignment

Look carefully at the level layout. You will notice that the code for any non-free tile or block consists of two letters, rather than one. 
Also, the first letter of the code is offset to the left of the free tile code. Except in special circumstances (as we will see later), 
the codes for *any* non-free block/tile follow this pattern.

Well, now that we know a bit about alignment, let's add our Blocked Wall!

* Open **Blocks**, and open the level file (`<Ctrl> + <q>`), or by opening it in Notepad++ (`<Ctrl> + <o>`). If you don't remember where it is located, 
the level we are editing is located at [`cdc\Z14WWH\LEVELS\LEVEL3.TXT`](about:blank).

*Coming Soon.*

### Task #2: Adding a Blocked Wall on the Left Corner

And you thought modding was going to be easy. :stuck_out_tongue:

This is that special circumstance I mentioned in Lesson #1.

*Coming Soon.*

[Back To The Top](#modding-tutorial)