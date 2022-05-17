#from collections import Counter 
# from collections import defaultdict
from collections import namedtuple


Persona= namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 78)

print(ariel[2])





# mi_tupla = (500, 18, 65)
# print(mi_tupla[1])





#serie = Counter([1,1,2,31,3,3,32,21,1,1,12,21,12,1,1,1])
# mi_diccio = defaultdict(lambda:'nada')


# mi_diccio['uno']= 'verde'
# print(mi_diccio['d'])
# print(mi_diccio)


# mi_diccio= {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
#print(mi_diccio['cuatro'])



#print(serie.most_common(3))
#print(list(serie))

#frase = 'Al pan pan y al vino wine'
#numeros = [7,213,3,3,4,5,56,67,]

#print(Counter(frase.split()))
#print(Counter(numeros))
#
#print(Counter("missisisipi"))
