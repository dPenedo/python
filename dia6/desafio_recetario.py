from os import system
from pathlib import Path
import os

total_recetas = contar_recetas()

ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas')

def comenzar():
    system('clear')
    print("¡Bienvenido/a al recetario!")
    print(f"La ubicación de las recetas en el ordenador es \n{ruta_de_acceso} ")
    print(f"¡¡Hay un total de {total_recetas} recetas!!")
    print("¿Qué deseas hacer?")
    print('''
    [1] Leer una Receta
    [2] Crear una Receta
    [3] Crear una categoría
    [4] Eliminar una Receta
    [5] Eliminar una Categoría
    [6] Finalizar programa
    ''')
    input("Selecciona uno de los numeros y presiona la 'Enter'")

def contar_recetas():
    cuenta = 0
    for txt in ruta_de_acceso.glob("**/*.txt"):
        cuenta +=1
    return(cuenta)

def mostrar_categorias():
    for txt in ruta_de_acceso.iterdir():
        if txt.is_dir():
            print(txt.name)

def elegir_categoría():
    print('Estas son las categorías que hay: ')
    mostrar_categorias()
    categoria = input('¿Qué categoría quieres elegir? \n(Escribe aquí el nombre): ')
    categoria_c = categoria.capitalize()
    return categoria_c

def mostrar_recetas():
    for txt in ruta_de_acceso.glob("**/*.txt"):
        print(txt.stem)

def elegir_receta():
    print('Estas son las recetas que hay: ')
    mostrar_recetas()
    receta = input('¿Qué receta quieres elegir? \n(Escribe aquí el nombre): ')
    receta_c = receta.capitalize()
    return receta_c


def leer_receta(categoria, receta):
    ubicacion = Path("/home/dani/Documentos/python/dia6/Recetas/", categoria, receta)  
    mi_archivo = open(ubicacion)
    lectura = mi_archivo.read()
    print(lectura)
    
def crear_nombre_receta(categoria):
    nombre = input('¿Cómo se llamará la receta?     ')
    texto = nombre+".txt"
    print(texto)
    ubicacion = Path('/home/dani/Documentos/python/dia6/Recetas', categoria, texto)
    nuevo = open(ubicacion, mode = "w")
    nuevo.write("")
    nuevo.close
    print(f'La receta "{nombre}" ha sido creada')    
    

def crear_contenido(categoria, receta):
    ubicacion = Path("/home/dani/Documentos/python/dia6/Recetas/",categoria, receta)
    archivo = open(ubicacion,'w')
    texto_introducido = input("Escriba aquí el texto de la receta: ")
    archivo.write(texto_introducido)
    archivo.close()

def crear_categoria():
    ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas/')
    def crear_categoria():
    carpeta = input("¿Cómo se llamará la nueva categoría?")
    ruta_carpeta = ruta_de_acceso / carpeta
    os.makedirs(ruta_carpeta)

    return ruta_carpeta.resolve()



def eliminar_receta():

def eliminar_categoria():
    print('Estas son las categorías que hay: ')
    mostrar_categorias()
    categoria = input('¿Qué categoría quieres eliminar?\n (Escribe el nombre y presiona enter para eliminar)')
    categoria_a_eliminar = categoria.capitalize()
    os.rmdir(Path('/home/dani/Documentos/python/dia6/Recetas', categoria_a_eliminar))

def finalizar_programa():



