from pickle import TRUE
from coaster import Coaster
class Game(object):
	BoardSize = 0
	Solutions = 0

	def __init__ (self, boardSize):
		self.BoardSize = boardSize
		self.Board = []
		self.Coasters = []

	def SetCoasters(self):
		for i in range(self.BoardSize * self.BoardSize):
			self.Coasters.append(Coaster(i))

	def GetCoastersToDo(self):
		ret = []
		for c in self.Coasters:
			found = False
			for r in self.Board:
				for c2 in r:
					if c2.GetName() == c.GetName():
						found = True
						break
				if found: break
			if found == False: ret.append(c.Copy())
		return ret

	def TestCoaster(self, row, col):
		sumTop = 0
		sumLeft = 0
		if row > 0:
			sumTop = self.Board[row][col].Pix[0] + self.Board[row-1][col].Pix[2]
		if col > 0:
			sumLeft = self.Board[row][col].Pix[3] + self.Board[row][col-1].Pix[1]
		return sumTop == 0 and sumLeft == 0

	def AddToBoard(self, row, col, coasterToAdd):
		if row + 1 > len(self.Board):
			self.Board.append([])
		if col + 1 > len(self.Board[row]):
			self.Board[row].append(coasterToAdd)
		else:
			self.Board[row][col] = coasterToAdd

	def ToString(self):
		for r in self.Board:
			for c in r:
				c.ToString()

	def ToList(self, rotation):
		retList = []
		if rotation == 0:
			for r in self.Board:
				for c in r:
					retList.append(c.Name)
		elif rotation == 90:
			for c in range(self.BoardSize-1, -1, -1):
				for r in range(self.BoardSize):
					retList.append(self.Board[r][c].Name)
		elif rotation == 180:
			for r in range(self.BoardSize-1, -1, -1):
				for c in range(self.BoardSize-1, -1, -1):
					retList.append(self.Board[r][c].Name)
		else: #rotation = 270
			for c in range(self.BoardSize):
				for r in range(self.BoardSize-1, -1, -1):
					retList.append(self.Board[r][c].Name)
		return retList

	def FoundSolution(self):
		Game.Solutions += 1
		print ("Solution #", self.Solutions)
		self.ToString()
