class Hero():
    __jumplah = 0
    def __init__(object, name):
        object.__name = name
        Hero.__jumplah += 1

    # berlaku untuk objek
    def getJumplahObject(object):
        return Hero.__jumplah
    
    # berlaku untuk class, tanpa self
    def getJumplahClass():
        return Hero.__jumplah
    
    # method static nempel ke object dan class
    @staticmethod
    def getJumplahSM():
        return Hero.__jumplah
    
    @classmethod
    def getJumplahCM(cls):
        return cls.__jumplah
    
marksman = Hero("Lesly")
marksman = Hero("Claude")
marksman = Hero("Layla")
marksman = Hero("Miya")
marksman = Hero("Grager")

# output dari object
print(marksman.getJumplahObject())   
# output dari class
print(Hero.getJumplahClass())

print("\n")

# output dari class dan object
print(marksman.getJumplahSM())
print(Hero.getJumplahSM())

print("\n")
print(marksman.getJumplahCM())
print(Hero.getJumplahCM())