import re
import os


ruta = '/home/dani/Documentos/python/Día 9/Mi_Gran_Directorio/'

def recorrer_archivos():
    for archivo in os.walk(ruta):
        resultado = buscador(archivo)
        if resultado == si:
            return archivo, patron
        else:
            pass

def buscador(texto):
    patron = r"N+\w{3}-\d{5}"
    texto = 'La movida está en la casa, oh yewhh Nryu-12365'
    busqueda = re.search(patron, texto)
    if busqueda:
        return si #Hay que sacar el archivo y patron 
    else:
        return no


for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')
for sub in subcarpeta:
    print(f'\t {sub}')
    print('Los archivos son: ')
for arch in archivo:
    if arch.startswith('2015'):
        print(f'\t{arch}')
print('\n')



