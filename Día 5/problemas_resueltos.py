'''contar primos'''

def contar_primos(numero):

    count = [2]
    iteracion = 3
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        for n in range(3,iteracion,2):

            if iteracion % n ==0:
                iteracion +=2
                break
        else:
            count.append(iteracion)
            iteracion += 2
    
    print(count)
    return(len(count))


print(contar_primos(50))


'''buscar ceros contiguos'''
# def busca_ceros(*args):
#     contador = 0
        
#     for element in args:
#         if contador + 1 == len(args):
#             return False
#         elif args[contador] == 0 and args[contador +1] == 0:
#             return True
#         else:
#             contador +=1
#     return False

# print(busca_ceros(0,2,23,0, 4,6,45,0))





# def buscar_unicas(palabra):
    
#     mi_set = set()
    
#     for letra in palabra:
#         mi_set.add(letra)
    
#     mi_lista = list(mi_set)
#     mi_lista.sort()
#     return mi_lista

# print(buscar_unicas('enrtetenido'))



# def buscar_unicas(palabra):
#     lista = list(palabra)
#     lista_sin_duplicados = list(set(lista))
#     lista_sin_duplicados.sort()
#     return lista_sin_duplicados

# print(buscar_unicas('perretdodoojda'))

