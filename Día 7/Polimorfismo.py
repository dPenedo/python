class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice MuUUUUUuuuuUUu")

    

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beeeEEeeEeEEE")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('nube')

 #vaca1.hablar()
 #oveja1.hablar()

 
#animales =  [vaca1, oveja1]
#
#for animal in animales:
    #animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)
