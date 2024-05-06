class Hero:
    # class variabel
    jumplah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputDefense):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.defense = inputDefense
        Hero.jumplah += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("Nama Hero: " + self.name)

    # method dengan argumen, tanpa return
    def regen(self, up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("Kadita", 100, 1000, 500)
# hero2 = Hero("Kagura", 100, 950, 500)
# hero3 = Hero("Guinevere", 100, 720, 450) 
# hero4 = Hero("Change", 300, 560, 230)

hero1.siapa()

hero1.regen(20)
print(hero1.health)

print(hero1.getHealth)