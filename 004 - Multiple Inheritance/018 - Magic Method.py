class Jawir:
    def __init__(self, name, skin):
        self.name = name
        self.skin = skin

    def __repr__(self):
        return "\nRapr\nName: {}\nSkin: {}".format(
            self.name,
            self.skin
        )
    
    def __str__(self):
        return "\nStr\nName: {}\nSkin: {}".format(
            self.name,
            self.skin
        )

    def __add__(self, object):
        return self.name + object.name
    
    def showJawir(self):
        print("Normal\nName: {}\nSkin: {}".format(
            self.name,
            self.skin
        ))
        print(repr(jawirOne))
        print(str(jawirOne))
        print("\n")
        print(jawirOne + jawirTwo)

jawirOne = Jawir("Tito", "Hitam")
jawirTwo = Jawir("Tama", "Hitam")
jawirOne.showJawir()