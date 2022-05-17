import time
import timeit




declaracion = '''
prueba_for(10)

'''
mi_setup = '''

def prueba_for(numero):
    lista = []
    for num in range(1, numero +1):
        lista.append(num)
    return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number = 10000000)
print(duracion)


#timeit.timeit()


declaracion2 = '''
prueba_while(10)

'''
mi_setup2 = '''

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista
'''


duracion2 = timeit.timeit(declaracion2, mi_setup2, number = 10000000)
print(duracion2)
 

#timeit.timeit()




# Haciéndolo con time (medir antes y después el tiempo)
# inicio = time.time() 
# prueba_for(1000000)
# final = time.time()
# print(final-inicio)
# # print(prueba_for(15))
# # print(prueba_while(15))

# inicio = time.time()
# prueba_while(1000000)
# final = time.time()
# print(final-inicio)
