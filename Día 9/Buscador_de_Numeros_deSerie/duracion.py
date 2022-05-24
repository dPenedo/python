import timeit

stmt = '''

leer('text.txt')

'''
setup = '''

def leer(documento):
    archivo = open(documento, 'r')
    texto = archivo.readlines()
    archivo.close()
    return texto

'''

duracion = int(timeit.timeit(stmt, setup))
print(duracion)
