class Hero:
    def __init__(object, name, health):
        object.name = name
        object.health = health

class hero_intelegent(Hero):
    pass

class hero_streengh(Hero):
    pass

fighter = Hero("Argus", 100)
techies = hero_intelegent("Techies", 50)
axe = hero_streengh("Axe", 10)

print(fighter.name)
print(techies.name)
print(axe.name) 