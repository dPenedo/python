lista_numeros = [123,-12,121212]
suma = 0

def suma_menores (lista):
    for numero in lista:
        if numero > 0 and numero <1000:
            suma += numero
        else:
            continue
    return suma

suma_menores(lista_numeros)
print(suma)