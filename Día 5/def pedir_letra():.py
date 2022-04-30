

def chequear_letra(letra, palabra):
    lista = list(palabra)
    palabro: []
    for element in lista:
        if element == letra:
            palabro.append(letra)
        else:
            palabro.append('_')
    print(palabro)
letra='a'
palabra='iguana'
chequear_letra(letra,palabra)