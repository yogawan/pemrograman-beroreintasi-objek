class Team:
	def setTeam(self, team):
		self.team = team

	def showTeam(self):
		print("\nName: {}\nHealth: {}\nTeam: {}\nTipe: {}".format(
			self.name,
			self.health,
			self.team,
			self.tipe
			))

class Tipe:
	def setTipe(self,tipe):
		self.tipe = tipe

	def showTipe(self):
		print("\nName: {}\nHealth: {}\nTeam: {}\nTipe: {}".format(
			self.name,
			self.health,
			self.team,
			self.tipe
			))

class Hero(Team,Tipe):
	def __init__(self,name,health):
		self.name = name
		self.health = health

marksman1 = Hero("Lesly", 100)
marksman2 = Hero("Miya", 100)

marksman1.setTeam("Black")
marksman2.setTeam("White")

marksman1.setTipe("Marksman")
marksman2.setTipe("Marksman")

marksman1.showTeam()
marksman2.showTipe()