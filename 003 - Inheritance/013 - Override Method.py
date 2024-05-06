class Hero:
    def __init__(object, name, health):
        object.name = name
        object.health = health

    def showInfo(object):
        print("name: {}\nhealth: {}".format(
            object.name,
            object.health
            )
        )

class heroIntelligent(Hero):
    def __init__(object, name):
        # Hero.__init__(object, name, 100)
        super().__init__(name, 150)

    def showInfo(object):
        print("name: {}\ntype: Intelligent\nhealth: {}".format(
            object.name,
            object.health
            )
        )

class heroStrength(Hero):
    def __init__(object, name):
        # Hero.__init__(object, name, 200)
        super().__init__(name, 300)

    def showInfo(object):
        print("name: {}\ntype: Strength`\nhealth: {}".format(
            object.name,
            object.health
            )
        )

lina = heroIntelligent("Lina")
axe = heroStrength("Axe")

lina.showInfo()
axe.showInfo()