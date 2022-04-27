# lista ['a']


# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# for indice, nombre in enumerate(lista_nombres):
#     print(f'{nombre} se encuentra en el índice {indice}')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,item in list(enumerate(lista_nombres)):
    if item[0] == 'M':
        print(indice)


#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#indice = 1
#for nombre in lista_nombres:
 #   print(f'{nombre} se encuentra en el índice {indice}')
 #   indice+=1
# palabra = "Python"
# palabra = list(palabra)
# lista_indices = list(enumerate(palabra))
# print(lista_indices)
# #
# lista = ['a', 'b', 'c']
# mis_tuples = list(enumerate(lista))
# print(mis_tuples)
# print(type(mis_tuples))






#for indice, item in enumerate(range(50,55)):
#    print(indice, item)