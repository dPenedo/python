from os import system
from pathlib import Path
import os
from re import A
ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas')

def leer_receta(a):
    receta_elegida = Path("/home/dani/Documentos/python/dia6/Recetas/Carnes/", 'Matambre a la Pizza.txt')
    mi_archivo = open(prueba)
    lectura = mi_archivo.read()
    print("Matambre a la Pizza.txt")

leer_receta()
    mi_archivo = open(prueba)
receta_elegida = Path("/home/dani/Documentos/python/dia6/Recetas/Carnes/", 'Matambre a la Pizza.txt')
leer_receta(receta_elegida)

# def contar_recetas():
#     cuenta = 0
#     for txt in ruta_de_acceso.glob("**/*.txt"):
#         cuenta +=1
#     return(cuenta)



# def mostrar_categorias():
#     for txt in ruta_de_acceso.iterdir():
#         if txt.is_dir():
#             print(txt.name)


# mostrar_categorias()





# ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas/')
# def crear_categoria():
#     carpeta = input("¿Cómo se llamará la nueva categoría?")
#     ruta_carpeta = ruta_de_acceso / carpeta
#     os.makedirs(ruta_carpeta)

#     return ruta_carpeta.resolve()


# print(crear_categoria())
