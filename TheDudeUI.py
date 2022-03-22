from ast import Global
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from coaster import Coaster
from game import Game

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
    global solutions, dupes
    for solution in solutions:
        if MyGame.ToList(0) in solution:
            dupes += 1
            return

    solutions.append([MyGame.ToList(0), 
        MyGame.ToList(90), 
        MyGame.ToList(180), 
        MyGame.ToList(270)])

def playGame(*args):
    try:
        characterCount = int(characters.get())
        boardSize = int(boardsize.get())

        Coaster.SetCast(characterCount)
        solutions.clear()
        dupes = 0
        MyGame = Game(boardSize)
        MyGame.SetCoasters()

        AddCoasterToBoard(MyGame,0,0)

        solutionCount.set(int(len(solutions)))
        duplicateCount.set(int(dupes))

#        tkinter.messagebox.showinfo("Title", "Message")
    except ValueError:
        pass

class MainGui:

    def __init__(self, parent):
        self.parent = parent
        parent.title("The Dude coaster game")

        mainframe = ttk.Frame(parent, padding="7 7 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

     #   characters = IntVar()
        character_entry = ttk.Entry(mainframe, width=4, textvariable=characters)
        character_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, text="# of characters").grid(column=1, row=1, sticky=E)

     #   boardsize = IntVar()
        boardsize_entry = ttk.Entry(mainframe, width=4, textvariable=boardsize)
        boardsize_entry.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(mainframe, text="board size (x by x)").grid(column=1, row=2, sticky=E)

#        solutionCount = StringVar()
        ttk.Label(mainframe, textvariable=solutionCount).grid(column=2, row=3, sticky=(W, E))
        ttk.Label(mainframe, text="# of solutions").grid(column=1, row=3, sticky=E)
#        duplicateCount = StringVar()
        ttk.Label(mainframe, textvariable=duplicateCount).grid(column=2, row=4, sticky=(W, E))
        ttk.Label(mainframe, text="# of duplicates").grid(column=1, row=4, sticky=E)

        ttk.Button(mainframe, text="Play Game", command=playGame).grid(column=3, row=5, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        character_entry.focus()
        root.bind("<Return>", playGame)

root = Tk()

characters = IntVar()
boardsize = IntVar()
solutionCount = StringVar()
duplicateCount = StringVar()
solutions = []
dupes = 0
MyGame = Game(0)

MainGui(root)

root.mainloop()