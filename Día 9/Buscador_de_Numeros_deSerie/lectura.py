import os
import re


ruta = '/home/dani/Documentos/python/Día 9/Mi_Gran_Directorio/'

patron = 'cinco'
patron = r"w{5}"

def buscador(documento):
    archivo = open(documento, 'r')
    texto = archivo.readlines()
    texto_str = str(texto)
    archivo.close()
    if patron in texto_str:
        print(patron)
        print(f"Y este es el textote{texto_str} en {documento}")
    else:
        print("No se encuentra disponiblot")
        print(f"Y este es el textote{texto_str} en {documento}")



buscador('text.txt')






#docu = 'text.txt'
#def leer(documento):
#    archivo = open(documento, 'r')
#    texto = archivo.readlines()
#    archivo.close()
#    return texto
#
#print(leer('text.txt'))
