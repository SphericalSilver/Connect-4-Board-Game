# Connect-4
Connect 4 Group Project

Fully functional version of the game Connect-4, with a couple of twists:
- Players are able to customize their board size, as well as the amount of discs that need to be connected to win.
- There is a "pop-out" option. Instead of dropping in a piece, players may remove one of their own pieces currently on the bottom row of the game board, thus moving all the pieces above it down a level. 
- Choose to play against a friend, or against the computer!

## How to play

Simply run the code on Python 3! The IDE Spyder is recommended. The game will be playable in the iPython console. 

The messages in the console will prompt you to enter certain integers that will give the game the commands it needs to understand your actions, like so:

![iPython console](https://i.gyazo.com/edb241fa3bec81b17f06a4f17634299e.png)

The board is represented by a numpy array, with numbers corresponding to the player number representing the discs.

In the below example, notice how player 1 won by connecting 4 diagonal pieces!

![player 1 victory](https://i.gyazo.com/45d2f1ab497c285dd75a2491377eb564.png)
