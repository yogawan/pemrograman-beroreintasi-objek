class Hero:
    pass

hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "tank"
hero2.health = 500

hero3.name = "fighter"
hero3.health = 300

print(hero1)
print(hero1.__dict__)