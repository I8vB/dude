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
    global dupes, solutions
    for solution in solutions:
        if MyGame.ToList(0) in solution:
            dupes += 1
            return

    solutions.append([MyGame.ToList(0), 
        MyGame.ToList(90), 
        MyGame.ToList(180), 
        MyGame.ToList(270)])

if __name__ == '__main__':

    characterCount = int(input("Enter number of cast members (2-5): "))
    gameSize = int(input("Enter number of coasters per row (2-5): "))

    solutions = []
    dupes = 0

    Coaster.SetCast(characterCount)
    print (f'The Cast: {Coaster.cast}')

    MyGame = Game(gameSize)
    MyGame.SetCoasters()
    print ('The Coasters')
    MyGame.ToString()

AddCoasterToBoard(0,0)

print ("Duplicates Found:", dupes)
print ("Solutions Found:", len(solutions))
print (*solutions, sep="\n")
