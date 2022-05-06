class Pajaro: 

    alas = True 

    def __init__(self, color, especie): 
        self.color = color
        self.especie = especie

    def piar(self): #método
        print('pio, mi color es {}'.format(self.color)) #Se le añade self porque es el color de la instancia que ejecuta el metodo
    
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")

piolin = Pajaro('amarillo', 'canario')

piolin.piar()
piolin.volar(59)




mi_pajaro = Pajaro('negro', 'Tucan') #instancia / objeto

# palabra = 'hola'
