class Hero:
    def __init__(object, name, health):
        object.name = name
        object.health = health

    def showInfo(object):
        print("name: {}\nhealth: {}".format(object.name, object.health))

class heroIntelligent(Hero):
    def __init__(object, name):
        # Hero.__init__(object, name, 100)
        super().__init__(name, 150)
        super().showInfo()

class heroStrength(Hero):
    def __init__(object, name):
        # Hero.__init__(object, name, 200)
        super().__init__(name, 300)
        super().showInfo()

lina = heroIntelligent("Lina")
axe = heroStrength("Axe")

print("\n")
print(lina.name, lina.health)
print(axe.name, axe.health)