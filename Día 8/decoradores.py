# Decoradores

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada('Python')










#  def cambiar_letras(tipo):
#     def mayuscula(texto):
#         print(texto.upper())

#     def minuscula(texto):
#         print(texto.lower())
#     if tipo == 'may':
#         return mayuscula
#     elif tipo == 'min':
#         return minuscula
# operacion = cambiar_letras('min')
# operacion('palabrA')


# def una_funcion(funcion):
#     return funcion

# una_funcion(mayuscula('probando'))
#mi_funcion = mayuscula   #La variable se convierte en función
#mi_funcion('python')

