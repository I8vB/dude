import random
class Coaster(object):
	cast = []
	pictureCount = 0

	@staticmethod
	def SetCast(characterCount):
		Coaster.pictureCount = characterCount
		Coaster.cast.clear()
		for i in range(1, characterCount + 1):
			Coaster.cast.append(i)
			Coaster.cast.append(-i)

	def __init__(self, name):
		self.Name = name
		self.Pix = []
		self.SetPix()

	def SetPix(self):
		for i in range(4):
			self.Pix.append(Coaster.cast[random.randint(0, Coaster.pictureCount*2-1)])

	def Rotate(self):
		temp = self.Pix[0]
		self.Pix[0] = self.Pix[1]
		self.Pix[1] = self.Pix[2]
		self.Pix[2] = self.Pix[3]
		self.Pix[3] = temp

	def GetName (self):
		return self.Name

	def Copy (self):
		ret = Coaster(self.Name)
		ret.Pix = self.Pix.copy()
		return ret

	def __str__(self):
		return f'Coaster: {self.Name}, Pix: {self.Pix}'