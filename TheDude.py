from modules import *
from coaster import Coaster
from game import Game

def AddCoasterToBoard(x, y):
    todo = MyGame.GetCoastersToDo()
    ##print(x,y, todo)
    if len(todo) == 0:
        MyGame.FoundSolution()
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


## start
Coaster.pictureCount = 4
gameSize = 2

for i in range(1, 5):
    Coaster.cast.append(i)
    Coaster.cast.append(-i)

MyGame = Game(gameSize)
MyGame.SetCoasters()
MyGame.ToString()

AddCoasterToBoard(0,0)

print ("Solutions Found:", Game.Solutions)
