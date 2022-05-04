from os import system
from pathlib import Path
import os


ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas')


def crear_nombre_receta(categoria):
    nombre = input('¿Cómo se llamará la receta?     ')
    texto = nombre+".txt"
    print(texto)
    ubicacion = Path('/home/dani/Documentos/python/dia6/Recetas', categoria, texto)
    nuevo = open(ubicacion, mode = "w")
    nuevo.write("")
    nuevo.close
    print(f'La receta "{nombre}" ha sido creada')    

crear_nombre_receta('Carnes')