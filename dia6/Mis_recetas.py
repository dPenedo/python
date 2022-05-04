import os
from pathlib import Path
from os import system

ruta_de_acceso = Path('/home/dani/Documentos/python/dia6/Recetas')

def contar_recetas():
    cuenta = 0
    for txt in ruta_de_acceso.glob("**/*.txt"):
        cuenta +=1
    return cuenta

def comenzar():
    system('clear')
    contar_recetas()
    total_recetas = contar_recetas()
    print('*'*50)
    print('*'*10 +"¡Bienvenido/a al recetario!"+'*'*10)
    print('*'*50)
    print(f"La ubicación de las recetas en el ordenador es \n{ruta_de_acceso} ")
    print(f"¡¡Hay un total de {total_recetas} recetas!!")
    print("¿Qué deseas hacer?")
    
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('''"Elige una opción:
        1] Leer una Receta
        [2] Crear una Receta
        [3] Crear una categoría
        [4] Eliminar una Receta
        [5] Eliminar una Categoría
        [6] Finalizar programa
        "''')
        eleccion_menu = input()
    return int(eleccion_menu)

    
    
    print('')

    # [1] Leer una Receta
    # [2] Crear una Receta
    # [3] Crear una categoría
    # [4] Eliminar una Receta
    # [5] Eliminar una Categoría
    # [6] Finalizar programa
comenzar()

# Mostrar menu inicio
'''
menu = 0

if menu == 1:
    # mostrar categorias
    # elegir categoría
    # mostrar recetas
    # elegir recetas
    # leer receta
    # volver inicio
    pass

elif menu == 2:
    # mostrar categorias
    # elegir categoria
    # crear receta nueva
    # volver inicio
elif menu == 3:
    #crear categoria
    #volver iniicio
    pass

elif menu == 4:
    # mostrar categorias
    # elegir categoría
    # mostrar recetas
    # elegir recetas
    # eliminar receta
    # volver inicio
    pass

elif menu == 5:
    #mostrar categorias
    # elegir categoria
    # eliminar categoria
    #volver inicio
    pass
elif menu == 6
    #finalizar programa
    pass
'''