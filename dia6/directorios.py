from pathlib import Path

carpeta = Path("/home/dani/Descargas/Alternativo/") / 'archivo.txt'
# carpeta = Path("/home/dani/Descargas/Alternativo/")
# archivo = carpeta / 'archivo.txt'


mi_archivo = open(carpeta)
print(mi_archivo.read())




# import os


# otro_archivo = open('/home/dani/Descargas/Alternativo/archivo.txt')
# print(otro_archivo.read())

# os.rmdir('/home/dani/Descargas/Alternativo/Guajalotes')

# ruta = ("/home/dani/Documentos/python/dia6/prueba.txt")

# elemento = os.path.split(ruta) #Imprime una tupla con el nombre del directorio y del archivo

# elemento = os.path.split(ruta) #Imprime una tupla con el nombre del directorio y del archivo
# elemento = os.path.dirname(ruta)
# elemento = os.path.basename(ruta)
# print(elemento)

# ruta = os.makedirs("/home/dani/Descargas/Alternativo/otra")

# ruta = os.chdir("/home/dani/Descargas/Alternativo")

# archivo = open('archivo.txt')

# print(archivo.read())