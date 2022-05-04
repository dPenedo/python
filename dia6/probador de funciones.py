from pathlib import Path
import os
from re import A
ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas')

def mostrar_recetas():
    for txt in ruta_de_acceso.glob("**/*.txt"):
        print(txt.stem)
#Falta que incluya la categoria
def eliminar_receta():
    print('Estas son las recetas que hay: ')
    mostrar_recetas()
    receta = input('¿Qué receta quieres eliminar?\n (Escribe el nombre, respetando las minúsculas y mayúsculas y presiona enter para eliminar)')
    texto_receta = str(receta+".txt")
    Path('/home/dani/Documentos/python/dia6/Recetas/',*, texto_receta).unlink()

eliminar_receta()





# def crear_nombre_receta(categoria):
#     nombre = input('¿Cómo se llamará la receta?     ')
#     texto = nombre+".txt"
#     print(texto)
#     ubicacion = Path('/home/dani/Documentos/python/dia6/Recetas', categoria, texto)
#     nuevo = open(ubicacion, mode = "w")
#     nuevo.write("")
#     nuevo.close
#     print(f'La receta "{nombre}" ha sido creada')


# crear_nombre_receta('Carnes')




# def mostrar_categorias():
#     for txt in ruta_de_acceso.iterdir():
#         if txt.is_dir():
#             print(txt.name)

# def eliminar_categoria():
#     print('Estas son las categorías que hay: ')
#     mostrar_categorias()
#     categoria = input('¿Qué categoría quieres eliminar? (Escribe el nombre y presiona enter para eliminar)')
#     categoria_a_eliminar = categoria.capitalize()
#     os.rmdir(Path('/home/dani/Documentos/python/dia6/Recetas', categoria_a_eliminar))
    
# eliminar_categoria()

# def crear_contenido(categoria, receta):
#     ubicacion = Path("/home/dani/Documentos/python/dia6/Recetas/",categoria, receta)
#     archivo = open(ubicacion,'w')
#     texto_introducido = input("Escriba aquí el texto de la receta: ")
#     archivo.write(texto_introducido)
#     archivo.close()

# crear_contenido('Carnes', 'Matambre a la Pizza.txt')




# def leer_receta(a):
#     prueba = Path("/home/dani/Documentos/python/dia6/Recetas/Carnes/", a)
#     mi_archivo = open(prueba)
#     lectura = mi_archivo.read()
#     print(lectura)
# matambre = 'Matambre a la Pizza.txt'
# leer_receta(matambre)

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
