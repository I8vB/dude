from modules import *
from coaster import Coaster
from game import Game

def AddCoasterToBoard(x, y):
    todo = MyGame.GetCoastersToDo()

    # found possible solution
    if len(todo) == 0:
        AddBoardToSolutions()
        return

    newX = 0
    newY = 0
    ## loop thru all coasters to do
    for c in todo:
        ## loop thru each side of coaster
        for i in range(4):
            if i == 0:
                MyGame.AddToBoard(x, y, c)
            else:
                c.Rotate()
            ## try the coaster for picture matches
            if MyGame.TestCoaster(x,y):
                if y < MyGame.BoardSize - 1:
                    newX = x
                    newY = y + 1
                else:
                    newX = x + 1
                    newY = 0
                AddCoasterToBoard(newX, newY)
    ## pull coaster from board
    del MyGame.Board[x][y]

def AddBoardToSolutions():
    global dupes
    if len(solutions) == 0 or IsUniqueSolution():
        solutions.append([MyGame.ToList(0), 
            MyGame.ToList(90), 
            MyGame.ToList(180), 
            MyGame.ToList(270)])
    else:
	    dupes += 1

def IsUniqueSolution():
    for solution in solutions:
        if MyGame.ToList(0) in solution:
            return False
    return True

## start
characterCount = 4
gameSize = 2
solutions = []
dupes = 0

Coaster.pictureCount = characterCount
for i in range(1, characterCount + 1):
    Coaster.cast.append(i)
    Coaster.cast.append(-i)

MyGame = Game(gameSize)
MyGame.SetCoasters()
MyGame.ToString()

AddCoasterToBoard(0,0)

print ("Duplicates Found:", dupes)
print ("Solutions Found:", len(solutions))
print (*solutions, sep="\n")
