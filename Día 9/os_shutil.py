import os
# import send2trash
#print(os.getcwd()) #Donde estoy
import shutil
#print(os.walk('/home/dani/Documentos/python/'))

ruta = '/home/dani/Documentos/python/'
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

def movida():
    for l in rule:
        

# send2trash.send2trash('curso.txt')





# shutil.move('curso.txt', '/home/dani/Documentos/python/') #mover archivos
# shutil.


# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()

# print(os.listdir())
 
