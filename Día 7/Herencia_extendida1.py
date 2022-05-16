class Padre:
    def hablar(self):
        print("Hola")
class Madre:
    def reir(self):
        print('jajajaj')


    def hablar(self):
        print("que tal  ")


class Hijo(Padre, Madre):               #Aquí se marca el orden de prioridad
    pass

class Nieto(Hijo):
    pass

mi_nieto=Nieto()

mi_nieto.reir()
print(Nieto.__mro__)            #Ver organización. Orden de resolución __mro__

mi_nieto.hablar()
