- An explanation of the high-level design
(which file contains which functions and what do they
collectively do)

The project is separated into two files. the "main.py" contains
all the logical functions which are required to run the game.
the "test.py" files includes test function for the functions
in main.py

The general idea for the design is to create a board with the turtle
object. Using random method to generate 2s and 4s on the board.
Then using functions to merge the numbers. When two same numbers
appears to be together, add them up.

The test.py file contains test functions that run tests on
the non-helper function in main.py to ensure each function
runs as expected

- Instructions on how to run the program.
This includes which keys can be used by the player,
and what they do.

When user runs the program, they should be expecting a 2048 game.
by simply using the arrow keys on their keyboard, they are
providing input to the program. Program runs by generating
random 2s and 4s, and merging the numbers as user wanted. Users
will only be able to press the arrow keys, and will be notified if
they provide a invalid input. User will also be notified whether
they reached the game object, or they are lost. Other instructions
regarding restarting and quitting the game are showed to them
on the interface.

- A bullet point list of all the features in your
 program that work (including any extra credit items).

 - draws the board
 - generate 2s and 4s at random board grid
 - displays instruction
 - determines valid user inputs
 - merges the numbers
 - checks if a number is in the board
 - checks game status
 - determines whether game is over or not
 - BONUS: highlight when cells merge using a different color