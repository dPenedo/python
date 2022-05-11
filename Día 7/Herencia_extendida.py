class Animal:
    def __init__(self,edad, color):
        self.edad =edad
        self.color =color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def__init__(self, edad, color, altura_vuela)
    super().__init__(edad, color)
    #Como se han heredado, con la llamada super() no hace falta escribir:
    # self.edad = edad          
    # self.color = color
    self.altura_vuela = altura_vuela

    def hablar(self):
        print("pío")
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")


piolin = Pajaro(3, "amarillo", 60)
mi_animal = Animal(5, "negro")
piolin.volar(100)


piolin.hablar()
piolin.volar(100)