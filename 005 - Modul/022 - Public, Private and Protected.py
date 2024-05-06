class treePi:
    def __init__(self, fullName, fammilyName, cityFrom):
        self.fullName = fullName # Public
        self.__fammilyName = fammilyName # Private
        self.__cityForm = cityFrom # Private

    def showInfo(self):
        print("Name {}\nFammily Name: {}\nCity From: {}".format(
            self.fullName,
            self.__fammilyName, # Cara memanggil Private Variable
            self.__cityForm # Cara memanggil Private Variable
        ))

Name = treePi("Yogawan Aditya Pratama Soegito", "Soegito", "Klaten")
Name.showInfo()