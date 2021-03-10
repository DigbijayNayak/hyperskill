'''
Description
Our game is almost ready! Now let's combine what we’ve learned in the previous stages to make a game of tic-tac-toe that two players can play from the beginning (with an empty grid) through to the end (until there is a draw, or one of the players wins).

The first player has to play as X and their opponent plays as O.

Objectives
In this stage, you should write a program that:

Prints an empty grid at the beginning of the game.
Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
Ends the game when someone wins or there is a draw.
You need to output the final result at the end of the game.

Good luck!

The project was changed. Now the coordinates start from the upper left corner. Look closely at the examples.
Example
The example below shows how your program should work.
Notice that after Enter the coordinates: comes the user input.

---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
'''


#Answer
def board(n):
    print("---------")
    print(f"| {' '.join(n[0])} |")
    print(f"| {' '.join(n[1])} |")
    print(f"| {' '.join(n[2])} |")
    print("---------")

def move(player):
    global matrix, crosses, noughts
    while True:
        y, x = input("Enter coordinate: ").split()
        if y.isdigit() is False or y.isdigit() is False:
            print("You should enter numbers!")
            continue
        if int(y) not in range(1, 4) or int(x) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        if matrix[int(y) - 1][int(x) - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        matrix[int(y) - 1][int(x) - 1] = player
        crosses = [n for row in matrix for n in row if n == "X"]
        noughts = [n for row in matrix for n in row if n == "O"]
        board(matrix)
        break


def data_set():
    global matrix
    ds = [{i for i in row} for row in matrix]
    ds.append({matrix[0][0], matrix[1][0], matrix[2][0]})
    ds.append({matrix[0][1], matrix[1][1], matrix[2][1]})
    ds.append({matrix[0][2], matrix[1][2], matrix[2][2]})
    ds.append({matrix[0][0], matrix[1][1], matrix[2][2]})
    ds.append({matrix[2][0], matrix[1][1], matrix[0][2]})
    return ds


matrix = [[" " for i in range(3)] for j in range(3)]
crosses = []
noughts = []

board(matrix)
while True:
    move("X")
    data_set()
    if any([{"X"} in data_set(), {"O"} in data_set(), sum((len(crosses), len(noughts))) == 9]):
        print("X wins" if {"X"} in data_set() else "O wins" if {"O"} in data_set() else "Draw")
        break
    move("O")
    data_set()
    if any([{"X"} in data_set(), {"O"} in data_set(), sum((len(crosses), len(noughts))) == 9]):
        print("X wins" if {"X"} in data_set() else "O wins" if {"O"} in data_set() else "Draw")
        break
