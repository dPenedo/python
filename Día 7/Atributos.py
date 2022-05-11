class Pajaro: #clase

    alas = True #Atributo de clase

    def __init__(self, color, especie): #Atributo clase  init es el constructor de la clase, establece los atributos que siempre se asignan
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan') #instancia / objeto

# palabra = 'hola'


print(mi_pajaro.especie)
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)#imprime el atributo de clase
print(mi_pajaro.alas) #imprime el atributo de clase en la instancia




#     def __init__(self, mi_parametro):
#         self.atributo = mi_parametro

# mi_pajaro = Pajaro('negro')

# # palabra = 'hola'

# print(mi_pajaro.atributo)
