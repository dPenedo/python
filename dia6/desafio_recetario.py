from os import system
from pathlib import Path
import os
ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas') def contar_recetas(): cuenta = 0 for txt in ruta_de_acceso.glob("**/*.txt"): cuenta +=1 return(cuenta) def comenzar(): system('clear') contar_recetas()
    total_recetas = contar_recetas()
    print('*'*50)
    print('*'*10 +"¡Bienvenido/a al recetario!"+'*'*10)
    print('*'*50)
    print(f"La ubicación de las recetas en el ordenador es \n{ruta_de_acceso} ")
    print(f"¡¡Hay un total de {total_recetas} recetas!!")
    print("¿Qué deseas hacer?")
    
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('''Elige una opción:
        [1] Leer una Receta
        [2] Crear una Receta
        [3] Crear una categoría
        [4] Eliminar una Receta
        [5] Eliminar una Categoría
        [6] Finalizar programa
        ''')
        eleccion_menu = input()
    return int(eleccion_menu)


def enseñar_categorias(ruta):
    print("Categorias: ")
    ruta_de_acceso = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_de_acceso.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] -{carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1
    return lista_categorias


def escoger_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range (1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoría: ")
    return lista[int(eleccion_correcta) - 1]



def enseñar_recetas(ruta):
    print("Recetas: ")
    ruta_de_acceso = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_de_acceso.glob("**/*.txt"):
        receta_srt = str(receta.name)
        print(f"[{contador}] - {receta_srt}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def escoger_receta(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\n Elija una receta: ")

    return lista[int(eleccion_receta) -1 ]


def leer_receta(receta):
    print(Path.read_text(receta))




def crear_receta(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria (ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de la nueva categoría: ')
        nombre_categoría = input() 
        ruta_nueva = Path(ruta, nombre_categoría)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu receta {nombre_categoría} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")        


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"Un link la recera {receta.name} ha sido eliminada ")




def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n Presiona V para volver al menú:  ")


finalizar_programa = False
while not finalizar_programa:
    menu = comenzar()
    if menu == 1:
        mis_categorias = enseñar_categorias(ruta_de_acceso)
        mi_categoria = escoger_categoria(mis_categorias)
        mis_recetas = enseñar_recetas(mi_categoria)
        mi_receta = escoger_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = enseñar_categorias(ruta_de_acceso)
        mi_categoria = escoger_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(ruta_de_acceso)
        volver_inicio()
    elif menu == 4:
        mis_categorias = enseñar_categorias(ruta_de_acceso)
        mi_categoria = escoger_categoria(mis_categorias)
        mis_recetas = enseñar_recetas(mi_categoria)
        mi_receta = escoger_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = enseñar_categorias(ruta_de_acceso)
        mi_categoria = escoger_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()     
    elif menu == 6:
        finalizar_programa = True
