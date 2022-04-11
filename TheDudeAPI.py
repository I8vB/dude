# To Start:
# $ export FLASK_APP=TheDudeAPI.py
# $ flask run

from glob import glob
from flask import Flask, request, jsonify
from coaster import Coaster
from game import Game

app = Flask(__name__)
solutions = []
MyGame = Game(0)

@app.get("/solutions/")
@app.get("/solutions/<int:characterCount>")
@app.get("/solutions/<int:characterCount>/<int:boardSize>")
def get_solutions(characterCount = 2, boardSize = 2):
    global solutions

    Coaster.SetCast(characterCount)
    solutions.clear()
    MyGame = Game(boardSize)
    MyGame.SetCoasters()

    AddCoasterToBoard(MyGame,0,0)

    if len(solutions) == 0:
        return "No Solutions Found", 404
    return jsonify(solutions)

def AddCoasterToBoard(MyGame, x, y):
    todo = MyGame.GetCoastersToDo()

    # found possible solution
    if len(todo) == 0:
        AddBoardToSolutions(MyGame)
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
                AddCoasterToBoard(MyGame, newX, newY)
    ## pull coaster from board
    del MyGame.Board[x][y]

def AddBoardToSolutions(MyGame):
    global solutions
    for solution in solutions:
        if MyGame.ToList(0) in solution:
            return #duplicate solution

    solutions.append([MyGame.ToList(), 
        MyGame.ToList(90), 
        MyGame.ToList(180), 
        MyGame.ToList(270)])
