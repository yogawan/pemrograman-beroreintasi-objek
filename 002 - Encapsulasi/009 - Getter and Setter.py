class Hero:
    def __init__(object, name, health, armor):
        object.__name = name
        object.__health = health
        object.__armor = armor
        object.__info = "name: {} \nhealth: {}".format(object.__name, object.__health)

    @property
    def info(object):
        return object.__info
    
    @property
    def armor(object):
        pass
    
    @armor.getter
    def armor(object):
        return object.__armor
    
    @armor.setter
    def armor(object, input):
        object.__armor = input

    @armor.deleter
    def armor(object):
        print("armor deleted")
        object.__armor = None

marksman = Hero("Lesly", 500, 25)
print(marksman.info)
print("\n")

# change name
marksman.__name = "Granger"
print(marksman.info)
print("\n")

# getter
print("getter")
print(marksman.armor)
print("\n")

# setter
print("setter")
marksman.armor = 50
print(marksman.armor)
print("\n")

# deleter
print("deleter")
del marksman.armor
print(marksman.armor)