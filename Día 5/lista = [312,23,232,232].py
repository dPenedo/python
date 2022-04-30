from random import randint

def lanzar_moneda():
    moneda = randint(1,2)
    if moneda == 1:
        return 'Cara'
    else:
        return 'Cruz'
        
tirada = lanzar_moneda()
print(tirada)

def probar_suerte(tirada, lista_numeros):
    if tirada == 'Cara':
        print('La lista se autodestruirá')
        lista_numeros = []
        return lista_numeros
    else: 
        print('La lista fue salvada')
        return lista_numeros
listota = [123,13,23]
resultado = probar_suerte(tirada, listota)
print(resultado)
# lista_numeros = [23,34,54,64,46,46,46,10000]
# def reducir_lista(lista_numeros):
#     lista_numeros = list(set(lista_numeros))
#     lista_numeros.remove(max(lista_numeros))
    
#     return lista_numeros


# resultado = reducir_lista(lista_numeros)
# print(resultado)

# def promedio(lista_numeros):
#     total = len(lista_numeros)
#     suma = 0
#     for n in lista_numeros:
#         suma += n
#     return suma/total


# lista = [312,23,232,232]
# def duplicatos(lista):
#     lista = list(set(lista))
#     listota = []
#     for n in lista:
#         if n > 50:
#             listota.append(n)
#         else:
#             pass
#     return listota

# resultado = duplicatos(lista)
# print(resultado)
