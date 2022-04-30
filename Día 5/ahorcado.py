from multiprocessing.sharedctypes import Value
from random import shuffle

palabras_posibles = ['probar', 'programa', 'abril', 'maple', 'radio']

#funcion para comenzar
def comienzo():
    print(f'Bienvenido/a al juego del ahorcado,tiene 6 oportunidades para acertar. Por cada intento se le marcarán las letras contenidas y ganará cuando haya acertado todas ellas')
    shuffle(palabras_posibles)
    palabra_aleatoria = palabras_posibles[0]
    numero_huecos= len(palabra_aleatoria)
    huecos = ' _ '*numero_huecos 
    print(f'La palabra a adivinar es la siguiente: {huecos}')
    return(palabra_aleatoria)

palabra_de_la_partida = comienzo()
intentos = 6


# # Función para pedir letra
def pedir_letra():
    letra_elegida = ''
    while intentos <= 6:
        while letra_elegida not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x', 'y', 'z']:
            letra_elegida = input('Prueba con una letra: ')
        return letra_elegida
    print('Se te acabaron los intentos, madafoka')

letra_a_comprobar = pedir_letra()

# Función de comprobación de si la letra en la palabra




def comprobar_si_esta(letra, palabra):
    letra = letra_a_comprobar
    palabra = list(palabra_de_la_partida)
    if letra not in palabra:
        print('La letra no está en la palabra')
        intentos-=1
        return(pedir_letra())
    else:
        print('Sí que está')
        return chequear_letra(letra_a_comprobar,palabra_de_la_partida)


def chequear_letra(letra, palabra):
    lista = list(palabra)
    palabro: []
    for element in lista:
        if element == letra:
            palabro.append(letra)
        else:
            palabro.append('_')
    print(palabro)


# Chequea la letra y devuelve la palabra con las letras acertadas



    
    