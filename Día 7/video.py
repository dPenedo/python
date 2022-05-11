class Drink:
    def __init__(self,name):
        self.__name = name
    def getDetail(self):
        return "la bebida es: " + self.__name

class Beer(Drink):
    def__init__(self, name, brand, alcohol):
        super().__init__(name)
        self.__brand= brand
        self.__alcohol= alcohol 



beer1 = Beer("Pale Ale", "Minerva", 4.5)
print(beer1.getDetail())

