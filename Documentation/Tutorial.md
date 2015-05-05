# Building With Blocks #
Written by Triangle717, with information provided by [Xiron](http://www.youtube.com/user/Segatendo12)

### Warning: This tutorial is incomplete! ###

## Table of Contents ##
<table>
  <tr><th colspan="10">Course Sections</th></tr>
  <tr>
    <td><a href="#requirements">Requirements</a></td>
    <td><a href="#character-legend">Character Legend</a></td>
    <td><a href="#lesson-1-why-not-notepad">Lesson #1</a></td>
    <td><a href="#lesson-2-indentation-matters">Lesson #2</a></td>
    <td><a href="#task-1-adding-a-blocked-wall">Task #1</a></td>
    <td><a href="#lesson-3-making-sure-it-all-works">Lesson #3</a></td>
    <td><a href="#lesson-4-jumping-to-specific-levels">Lesson #4</a></td>
    <td><a href="#task-2-adding-a-blocked-wall-on-the-left-corner">Task #2</a></td>
    <td><a href="#task-3-adding-a-one-way-west-bound-red-cube">Task #3</a></td>
  </tr>
</table>

**Building With Blocks** is a basic tutorial on modding the _Island Xtreme Stunts_  _Trouble in Store_ minigame levels,
and will not cover everysingle detail.
Instead, it attempts to explain the basics of the level layout, and explain it in such a way that you will clearly understand the layout and improve your modding adventures.

## Requirements ##
You will need a few items to complete this tutorial:

* A copy of [_Island Xtreme Stunts_](http://en.wikipedia.org/wiki/Island_Xtreme_Stunts)
running [without the CD](http://www.rockraidersunited.org/topic/1301-)
[(video tutorial)](http://www.youtube.com/watch?v=yMGIu-BOrO8)
* The newest release of [**Blocks**](https://github.com/le717/Blocks/releases), or
* A source code editor, preferably [**Notepad++**](http://notepad-plus-plus.org) (never use Notepad!)
* The minigame level format details, available in [`Format-Details.md`](Format-Details.md)

## Character Legend ##
_Any color-cube or color-tile combination is acceptable (e.g. `RT`, `BC`, etc.). Water, free, wall, and `RB` are not assigned a color._

<table>
  <tr><th colspan="2">Character Legend</th></tr>
  <tr>
    <th>Color</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>Red</td>
    <td>R</td>
  </tr>
  <tr>
    <td>Green</td>
    <td>G</td>
  </tr>
  <tr>
    <td>Blue</td>
    <td>B</td>
  </tr>
  <tr>
    <td>Yellow</td>
    <td>Y</td>
  </tr>

  <tr>
    <th>Block Type</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>Tile</td>
    <td>T</td>
  </tr>
  <tr>
    <td>Cube</td>
    <td>C</td>
  </tr>
  <tr>
    <td>Free</td>
    <td>F</td>
  </tr>
  <tr>
    <td>Blocked Wall</td>
    <td>BW</td>
  </tr>
  <tr>
    <td>One way, west-bound Red Cube</td>
    <td>RB</td>
  </tr>

  <tr>
    <th>Water Type</th>
    <th>Code</th>
  </tr>
  <tr>
    <td>Top</td>
    <td>WI</td>
  </tr>
  <tr>
    <td>Left</td>
    <td>WJ</td>
  </tr>
  <tr>
    <td>Right</td>
    <td>WM</td>
  </tr>
  <tr>
    <td>Top Left</td>
    <td>WT</td>
  </tr>
  <tr>
    <td>Top Right</td>
    <td>WL</td>
  </tr>
  <tr>
    <td>Bottom Left</td>
    <td>WR</td>
  </tr>
  <tr>
    <td>Bottom Right</td>
    <td>WB</td>
  </tr>
  <tr>
  <tr>
    <td>Vertical</td>
    <td>WV</td>
  </tr>
    <td>Horizontal</td>
    <td>WH</td>
  </tr>
</table>

For the majority of this tutorial, we will be using level 3 of _Trouble in Store_, located at [`cdc\Z14WWH\LEVELS\LEVEL3.TXT`](about:blank)

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

From looking at our [Character Legend](#character-legend), we can see this level contains

 1. Free Tiles
 2. Blocked Walls
 3. a Yellow Tile
 4. a Yellow Cube

You may notice it also contains the code for the first and last lines of the file. We will not worry ourselves with them, and will instead
focus on the layout itself.

---

### Lesson #1: "Why Not Notepad?" ###
I need to address this before we begin. You may be wondering why I said to **never** use Notepad to mod the levels. Despite the claims of some
people, Notepad is **not** a good modding, programming, and sometimes even writing application.
During the writing of both this tutorial and **Blocks**, I was asked more than once why I advise against using Notepad. While I had a legitimate
point from the beginning, sure-fire evidence against its usage came in the form of a bug report.
Someone had tried to mod a level using Notepad, since the files are only plain text with an odd first line. In doing this, the level formatting
(which we will later discuss) broke, and any attempts to load the level would crash the game.
Moreover, when the same file was loaded in **Blocks** or **Notepad++**, the formatting would be correct, but it would still not load in-game. We
never solved the issue, much less figured out exactly how it happened. However, not one report has come back about **Blocks** or **Notepad++**
breaking the level layout and rendering it unplayable. That is why I strongly advise against any use of Notepad for modding.

Now you may be thinking

> "If Notepad++ does not break the levels like Notepad does, then why do I need to use Blocks?"

Honestly, there is no need! Using **Notepad++** instead of **Blocks** is your choice. I myself use **Notepad++** a good amount when modding!
However, **Blocks** contains safeguards that **Notepad++** does not.
These safeguards help ensure your level layout is valid and can be used in-game. Discussion of those safeguards is off-topic, but in the course of
this tutorial you will be taught about the areas that are most prone to breakage and what you can do to ensure your level is not invalid.
Though **Blocks** could be viewed as worthless for advanced modders or "a fancy text editor", it exists to help, not restrict, your modding.
If you feel it is limiting you,you are under no pressure to use it; but it is handy tool to have for both beginner and advanced modders alike.

### Lesson #2: Indentation Matters ###
Look carefully at our level layout. You will notice that the code for any non-free tile consists of two letters, rather than one.
Also, the first letter of the code is offset to the left of the free tile code. Except in special circumstances (as we will see later),
the codes for _any_ non-free cube/tile follow this pattern.

---

### Task #1: Adding a Blocked Wall ###
The first modding example we will do is add a Blocked Wall to the layout. We remember from the Character Legend a Blocked Wall is signified by a `BW`.
(If at any time you do not remember a code, fell free to peek back at the Character Legend. :wink:) To start, we are going to add a Blocked Wall on
the top row, at the 8th column, thus creating our first mod!

* Run **Blocks**, and open the level file (`<Ctrl + Shift + O>`), or  open it in **Notepad++** (`<Ctrl + o>`).
If you do not remember where it is located, the level we are editing is located at
[`cdc\Z14WWH\LEVELS\LEVEL3.TXT`](about:blank). If you are editing the level straight from Program Files,
be sure to run either program with Administrator rights, otherwise you will be unable to save your edit!
* Once the level is open in your editor of choice, find the square we want to edit (1st row, 8th column).
Start by removing the `F` that is currently sitting in that location, in addition to a single space (remember what we talked about in Lesson #2?).
* Now type `BW`, ensuring the `W` is lined up with the
`F` directly below it on the next row. Click Save (`<Ctrl + s>` in either program) to save your mod.

Before you started editing, the line looked like this:

` F  F  F  F  F  F  F  F  F  F  F  F  F`

but your edits should now have it looking like this:

` F  F  F  F  F  F  F BW  F  F  F  F  F`

* Open _Island Xtreme Stunts_, load your save game, make your way to Jack O' Trade's store (if you are not already there),
and load the _Trouble in Store_ minigame.
If you performed the editing correctly, the game will successfully load your modded level, and you will see a new Blocked Wall where you placed it!
If you didn't, then the game will crash. Even with this little bit of knowledge, you can mod all of the minigame levels,
since all Cubes and non-Free tiles alike work this way.

> **Recap:** You just learned why to never use Notepad when modding, indentation matters, how to open a level in **Blocks** or **Notepad++**, add a
> Blocked  Wall using the `BW` code, ensure it is properly indented to the left of the other codes, save and test it out! Applaud yourself! :clap:

Now we will dive into some lessons to learn a few things that will help us in your quest for successful modding.

[:arrow_up:](#building-with-blocks)

### Lesson #3: Making Sure It All Works ###
How do you know if your mod will work or not? I mean, if it is not properly created, it will not work, will it?

Correct, your mod will not work if is not properly created, but how do you know if it does works? _Island Xtreme Stunts_ has a pretty simple way of
telling you if your mod is not correct: it crashes! :stuck_out_tongue:

More specifically, the game will crash when you try to load a broken level if that level is the current level. If the broken level is one you have
already completed, it will not crash, but it would if you loaded that one.
If the broken level is ahead of the current level, then the game will crash when you reach that level.
Thus, ensuring you edit correctly really pays off in the long run!

### Lesson #4: Jumping to Specific Levels ###
_To be written._

---

### Task #2: Adding a Blocked Wall on the Left Corner ###
This is that special circumstance I mentioned in Lesson #2. Adding a Blocked Wall on the left side (1st column of any row)
of the level is not much harder than adding one anywhere else, it is just different.

To make this special edit a bit clearer, we will edit the same line from Task #1, including the Blocked Wall we added, but we'll include the second
line to show that indentation matters.

Recall I said in Lesson #2 that the first letter of a `BW` (or any non-Free tile) the code is offset to the left of the Free tile code directly
above or below it. To make that a bit clearer (if you are confused), here is a correct alignment:

```
 F  F  F  F  F  F  F BW  F  F  F  F  F
 F  F  F BW  F  F  F  F  F  F  F  F  F
```
In every instance, the `B` is offset one character to the left of an `F`, and the same goes all non-`F` characters. However, a cube on the left
side is indented to the right, so the `B` is aligned with the `F` on the top and bottom, like this:

```
 BW F  F  F  F  F  F BW  F  F  F  F  F
 F  F  F BW  F  F  F  F  F  F  F  F  F
```
Even more, this right indentation will continue until either the end of the line or the first free tile is reached.
An example of this indentation would look like:

```
 BW BW BW BW BW BW F BW  F  F  F  F  F
 F  F  F BW  F  F  F  F  F  F  F  F  F
```
So adding a cube on the left corner affects most (if not the entire) indentation of a line!

> **Recap:** You just learned how to add a cube on the left corner, the proper indentation for a  Cube, and the effects it has on a line! Good job! :thumbsup:

[:arrow_up:](#building-with-blocks)

### Task #3: Adding a one way, west-bound Red Cube ###
This one is loads of fun, and in a good way. :stuck_out_tongue:

You are probably wondering,

> "What on earth is a `One way, west-bound Red Cube`, and what is with that name??"

Let me tell you.
An `One way, west-bound Red Cube` is a unique cube in _Island Xtreme Stunts_. They are only found in Maggie Post's _Trouble in Store_ minigame
(that is, only in an unmodded copy), it only comes in Red, has a one-of-a-kind code, has an arrow on the top to visually remind you it is special,
validates any color Tile (not only Red) and even have special properties, since it only move ones direction, to the right of the layout.
If you think about the level in terms of a map, and have a standard NSEW compass, we can call the top of the level North, the bottom South, the
left side East, and the right side West, you will find this cube only moves West. You cannot push it North or South, and clearly not East, only West.
The only un-special-ness about the cube is that it can still be sunk in Water, it still follows all the indentation rules, and you cannot pull it
(exactly like all the other cubes, but since pulling is clearly not possible, why do I even mention it?).
As for the name of the cube: After I was told about this by Xiron, another modder, and was adding it into the Character Legend,
I was unable to write a better description for it. I asked around for a new name, to no avail, until I finally had this thought:

> Since this cube is so unique and one-of-a-kind, why can't it have a unique name to match?

And that's how it got the name `One way, west-bound Red Cube`. I'm sure if the _Island Xtreme Stunts_ developer who added this cube saw this,
they would probably laugh at the odd fan name. :P

Now that we take taken care of, we get to add this cube into our layout. Since it only moves West, we will be mindful of players and place it
where they can use it.
I said at the beginning we were using level 3 of _Trouble in Store_, from [`cdc\Z14WWH\LEVELS\LEVEL3.TXT`](about:blank),
but we are going to stray for a minute and use a fresh layout, containing nothing but Free tiles.

```
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
```

Start by placing a Red Tile (`RT`) at the 11th column of the 4th row (remember, indentation matters!). Lines 3 and 5 now look like this:

```
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F RT  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
```

Since we are adding an `One way, west-bound Red Cube`, it also must be located somewhere on the 4th row. Perhaps we should add it at...

> "Wait a second, le717! You have not said what the code for this cube is!"

Indeed I have not, have I? Thanks for pointing that out. ~~Did I mention it has a one-of-a-kind code?~~ Yes, I did. Well, I _could_ just tell you
to look at the Character Legend and get the code since it is listed there, but that would be laziness on my part. The code is `RB`, `R` meaning
Red, and `B` marking its distinctiveness from the other, normal cubes (`C`).

NOW that we have the code, We will place this cube on the 3rd column of the 4th row, so that the lines now look like:

```
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F RB  F  F  F  F  F  F  F RT  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
```

Just for fun, we will add some Blocked Walls and a Cube in the layout to make this level a bit less sparse...

```
 F  F BW BW BW BW  F  F BW  F BW  F BW
 F  F  F  F  F BW  F  F  F  F  F  F BW
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F RB  F  F BC  F  F  F  F RT  F  F
 F  F  F  F  F  F  F  F  F BW BW  F BW
 BW BW BW F BW  F  F  F  F  F  F  F  F
 F  F  F  F  F  F  F  F  F  F  F  F  F
 F  F BW BW BW  F  F  F  F  F  F  F  F
```

And finally, we test it. If the game loaded, and you can complete it, your mod works, and you have successfully added an `One way, west-bound Red Cube`!

> **Recap:** You leaned about a `One way, west-bound Red Cube`, the special properties it has (and does not have!), how it got it's unusual name, and how to
responsibly use it in a level layout. High five! :raised_hand:

[:arrow_up:](#building-with-blocks)
