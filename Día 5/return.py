def multiplicar (numero1,numero2):
    total = numero1 * numero2

    return total

resultado = multiplicar(5,10)
# print(resultado)
# '''palabra = 'oaor'
# palabra = palabra[::-1]
# print(palabra)'''

def invertir_palabra(x):
    x=x[::-1]
    return x.upper()

palabra = invertir_palabra('yeahh')
print(palabra)