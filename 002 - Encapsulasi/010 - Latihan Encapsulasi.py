class Hero:
    __jumplah = 0
    def __init__(object, heroName, heroHealth, heroAttack, heroArmor):
        object.__heroName = heroName
        object.__heroHealth = heroHealth
        object.__heroAttack = heroAttack
        object.__heroArmor = heroArmor

        object.__level = 1
        object.__exp = 0

        object.__heroHealthMax = object.__heroHealth * object.__level
        object.__heroAttackMax = object.__heroAttack * object.__level
        object.__heroArmorMax = object.__heroArmor * object.__level

        object.__health = object.__heroHealthMax

        Hero.__jumplah += 1

    @property
    def info(object):
        return "name: {}\nlevel: {}\nhealth: {}/{}\nattack: {}\narmor: {}".format(object.__heroName, object.__level, object.__heroHealth, object.__heroHealthMax, object.__heroAttackMax, object.__heroArmorMax)
    
    @property
    def gainExp(object):
        pass

    @gainExp.setter
    def gainExp(object, addExp):
        object.__exp += addExp
        if (object.__exp >= 100):
            print(object.__heroName, "Level Up!")
            object.__level += 1
            object.__exp -= 100

            object.__heroHealthMax = object.__heroHealth * object.__level
            object.__heroAttackMax = object.__heroAttack * object.__level
            object.__heroArmorMax = object.__heroArmor * object.__level

    def attack(object, enemy):
        object.gainExp = 50
    
marksman = Hero("Lesly", 100, 5, 15)
fighter = Hero("Zilong", 100, 5, 15)
tank = Hero("Uranus", 100, 5, 15)
support = Hero("Nana", 100, 5, 15)
assassin = Hero("Gusion", 100, 5, 15)

marksman.attack(fighter)
marksman.attack(fighter)
print(marksman.info)

# marksman.gainExp = 101
# fighter.gainExp = 101
# tank.gainExp = 101
# support.gainExp = 101
# assassin.gainExp = 101

# print(marksman.info)
# print("\n")
# print(fighter.info)
# print("\n")
# print(tank.info)
# print("\n")
# print(support.info)
# print("\n")
# print(assassin.info)
