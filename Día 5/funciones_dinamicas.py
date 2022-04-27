# def chequear_3_cifras(lista):
#     lista_3_cifras = []
#
#     for n in lista:
#         if n in range(100, 1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras
#
#
#
#
# suma = 585 + 402
#
# resultado = chequear_3_cifras([125,15,113])
# print(resultado)

lista_numeros = [1,50,343,340,750,600]

def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n > 0:
            return True
        else:
            pass
    return False
print(lista_numeros)

