cliente = {'nombre': 'Fein',
           'edad':98798,
           'ocupacion': 'el catacroker'}
pelicula = {'pelicula': 'Matrix',
           'ficha':{'protagonista': 'el loko kolo', 'director': 'el que tu ya sabes'}}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case{'nombre': nombre,
             'edad': edad,
             'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case{'pelicula': pelicula,
             'ficha': {'protagonista':protagonista, 'director':director}}:
            print('Esto es una película')
            print(pelicula, protagonista, director)
        case _:
            print('No se ni lo que es')






# serie = 'N-02'
#
# match serie:
#     case 'N-01':
#         print('Serie1')
#     case 'N-02':
#         print('Serie2')
#     case 'N-03':
#         print('Serie3')
#     case 'N-04':
#         print('Serie4')
#     case _:
#         print('la movida')