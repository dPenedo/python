
def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuacion(clase)
print('la media de la clase es', media)

clase = [1,4,9,6]
media = puntuacion(clase)
print('la media de la clase es', media)


# lista_numeros = [123,12,32,23,35,53,35,35,35]
# lista_numeros1 = []
# def reducir_lista(lista)):
#     for numero in lista_numeros:
#         if numero not in lista_numeros:
#             lista_numeros1.append(numero)
#         else:
#             continue
    
# reducir_lista(lista_numeros)
# print(lista_numeros1)



#  import random

# def lanzar_dados():
#     return random.randint(1,6), random.randint(1,6)    


# def evaluar_jugada(a,b):
#     suma_dados = a + b
#     if suma_dados <= 6:
#         return f'La suma de tus dados es {suma_dados}. Lamentable'
#     elif suma_dados > 6 and suma_dados < 10:
#         return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
#     else:
#         return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
        

