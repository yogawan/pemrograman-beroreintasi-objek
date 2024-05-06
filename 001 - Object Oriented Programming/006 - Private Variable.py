class Hero():

    # class variabel
    jumplah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variabel instance private
        self.__private = "private"

        # variabel instance private
        self._protected = "protected"

hero = Hero("Lina", 100)

print(hero.__dict__)
print(hero._protected)
hero._protected = "Testing"

print(hero.__dict__)
print(hero.__rotected)