class Hero:
    def __init__(self, name, hp, power, armor):
        self.name = name
        self.hp = hp
        self.power = power
        self.armor = armor

    def attack(self, enemy):
        print(self.name + " Attack " + enemy.name)
        enemy.attacked(self, self.power)

    def attacked(self, enemy, attackPowerLawan):
        print(self.name + " Attacked " + enemy.name)

        attackDiterima =  attackPowerLawan/self.armor
        print("Serangan terasa: " + str(attackDiterima))

        self.hp -= attackDiterima
        print("Hp" + self.name + " Tersisa " + str(self.hp))

marksman = Hero("Lesly", 500, 1000, 200)
fighter = Hero("Zilong", 500, 1000, 250)
# tank = Hero("Uranus", 500, 1000, 250)
# support = Hero("Nana", 500, 1000, 250)
# assassin = Hero("Gusion", 500, 1000, 250)

marksman.attack(fighter)
print("\n")
fighter.attack(marksman)