class Pajaro: 

    alas = True 
#Metodos de instancia
    def __init__(self, color, especie): 
        self.color = color
        self.especie = especie

    def piar(self): #método
        print('pio, mi color es {}'.format(self.color)) #Se le añade self porque es el color de la instancia que ejecuta el metodo
    
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pájaro es {self.color}')
#Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False #cambia desde la clase un método de atributo
        print(Pajaro.alas)

# Método estático

    @staticmethod
    def mirar(): #No puede cambiar atributos de instancia ni de clase
        print("El pájaro mira")                          # self.color = 'rojo' No funcionaria
                                                       # cls.alas = 2 No funciona      


Pajaro.mirar()

Pajaro.poner_huevos(3)



# piolin = Pajaro('amarillo', 'canario')
# piolin.piar()
# piolin.alas = False
# print(piolin.alas)
# piolin.pintar_negro()
# piolin.volar(50)