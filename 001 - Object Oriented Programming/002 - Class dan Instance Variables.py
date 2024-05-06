class Hero:
    jumplah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputDefense):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.defense = inputDefense
        Hero.jumplah += 1
        print("Membuat hero dengan nama: " + inputName)

hero1 = Hero("Kadita", 100, 1000, 500)
print(hero1.jumplah)
hero2 = Hero("Kagura", 100, 950, 500)
print(hero2.jumplah)
hero3 = Hero("Guinevere", 100, 720, 450) 
print(hero3.jumplah)
hero4 = Hero("Change", 300, 560, 230)
print(hero4.jumplah)
