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

def ShowSolution(MyGame):
    solutionWindow = tkinter.Toplevel()
    solutionWindow.title(str(len(solutions)))
    solutionWindows.append(solutionWindow)

    for i in range(MyGame.BoardSize):
        for j in range(MyGame.BoardSize):
            # get coaster to display
            coast = MyGame.Board[i][j]
            # create coaster frame
            frame = tkinter.LabelFrame(solutionWindow)
            frame.grid(row=i, column=j, padx=5, pady=5)
            inFrame = tkinter.Frame(frame)
            inFrame.grid(row=1, column=0)
            tag0 = tkinter.Label(inFrame, text=coast.Pix[0])
            tag0.grid(row=0, columnspan=3, sticky="N")
            tag1 = tkinter.Label(inFrame, text=coast.Pix[1])
            tag1.grid(row=1, column=2, padx=5, pady=5, sticky="E")
            tag2 = tkinter.Label(inFrame, text=coast.Pix[2])
            tag2.grid(row=2, columnspan=3, sticky="S")
            tag3 = tkinter.Label(inFrame, text=coast.Pix[3])
            tag3.grid(row=1, column=0, padx=5, pady=5, sticky="W")
            tagN = tkinter.Label(inFrame, text=" ")
            tagN.grid(row=1, column=1, padx=5, pady=5)

def AddBoardToSolutions(MyGame):
    global solutions, dupes
    for solution in solutions:
        if MyGame.ToList(0) in solution:
            dupes += 1
            return

    solutions.append([MyGame.ToList(), 
        MyGame.ToList(90), 
        MyGame.ToList(180), 
        MyGame.ToList(270)])

    ShowSolution(MyGame)

def playGame(*args):
    global dupes
    try:
        root.config(cursor="watch")
        for solutionWindow in solutionWindows:
            solutionWindow.destroy()
        solutionWindows.clear()

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

    except ValueError:
        tkinter.messagebox.showinfo("exception", "Message")

    finally:
        root.config(cursor="")


class MainGui:

    def __init__(self, parent):
        self.parent = parent
        parent.title("The Dude coaster game")

        mainframe = ttk.Frame(parent, padding="7 7 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        character_entry = ttk.Entry(mainframe, width=4, textvariable=characters)
        character_entry.grid(column=2, row=1, sticky=(W, E))
        Radiobutton(mainframe, text="2", variable=characters, value=2).grid(row=0, column=1)
        Radiobutton(mainframe, text="3", variable=characters, value=3).grid(row=0, column=2)
        Radiobutton(mainframe, text="4", variable=characters, value=4).grid(row=0, column=3)
        ttk.Label(mainframe, text="# of characters").grid(row=0, column=0, sticky=E)

        Radiobutton(mainframe, text="2", variable=boardsize, value=2).grid(row=1, column=1)
        Radiobutton(mainframe, text="3", variable=boardsize, value=3).grid(row=1, column=2)
        Radiobutton(mainframe, text="4", variable=boardsize, value=4).grid(row=1, column=3)
        ttk.Label(mainframe, text="board size (x by x)").grid(row=1, column=0, sticky=E)
        ttk.Label(mainframe, textvariable=solutionCount).grid(row=2, column=1, sticky=(W, E))
        ttk.Label(mainframe, text="# of solutions").grid(row=2, column=0, sticky=E)
        ttk.Label(mainframe, textvariable=duplicateCount).grid(row=3, column=1, sticky=(W, E))
        ttk.Label(mainframe, text="# of duplicates").grid(row=3, column=0, sticky=E)
        ttk.Button(mainframe, text="Play Game", command=playGame).grid(columnspan=4, row=5)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        character_entry.focus()
        root.bind("<Return>", playGame)

if __name__ == '__main__':
    root = Tk()
    characters = IntVar()
    characters.set(3)
    boardsize = IntVar()
    boardsize.set(3)
    solutionCount = StringVar()
    duplicateCount = StringVar()
    solutions = []
    solutionWindows = []
    dupes = 0
    MyGame = Game(0)
    main = MainGui(root)
    root.mainloop()