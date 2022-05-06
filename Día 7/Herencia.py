class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print('jajaj')
    def hablar(self):
        print('Qué tal?')


class Hijo(Padre, Madre): #Aquí es donde se decide el orden por el cual se heredará
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar() #lo hereda de Padre
mi_nieto.reir() #lo hereda de Madre

print(Nieto.__mro__)   # MRO: Method order resolution. Imprime el orden en el que se resuelve la herencia de los métodos
