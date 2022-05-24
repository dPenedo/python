import os
import re


ruta = '/home/dani/Documentos/python/Día 9/Buscador_de_Numeros_deSerie/Mi_Gran_Directorio/'

patron = r"N+\w{3}-\d{5}"

#Buscador
def buscador(documento):
    arch = open(documento, 'r')
    texto = arch.readlines()
    texto_str = str(texto)
    busqueda = re.search(patron, texto_str)
    if busqueda:
        return(str(busqueda.group(0)))
    else:
        pass


def recorrer_archivos():
    for root, dirs, archivo in os.walk(ruta):
        print(archivo)
#buscador('text.txt')

recorrer_archivos()




#docu = 'text.txt'
#def leer(documento):
#    archivo = open(documento, 'r')
#    texto = archivo.readlines()
#    archivo.close()
#    return texto
#
#print(leer('text.txt'))
