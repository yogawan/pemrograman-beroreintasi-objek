class Hero:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack
    
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    #setter
    def getAttack(self, attack):
        self.__health -= attack
    
# awal dari game
marksman = Hero("Lesly", 500, 5)

# output
print(marksman.getName())
print(marksman.getHealth())

# tidak bisa, karena ada argumen
# print(marksman.getAttack())

marksman.getAttack(5)
print(marksman.getHealth())