

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

lala = [123,123,23,23,]
for l in lala:
    print(f"numerro {l}")
