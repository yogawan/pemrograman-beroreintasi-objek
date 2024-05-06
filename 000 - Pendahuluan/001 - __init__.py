class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputDefense):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.defense = inputDefense

hero1 = Hero("Kadita", 100, 1000, 500)
hero2 = Hero("Kagura", 100, 950, 500)
hero3 = Hero("Guinevere", 100, 720, 450) 
hero4 = Hero("Change", 300, 560, 230)

print(hero1.name)
print(hero2.health)
print(hero3.power)
print(hero4.defense)