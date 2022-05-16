#!/usr/bin/python3
from pathlib import Path

ubicacion = Path('/home/dani/Documentos/python/')
print("Este es el creador de carpetas de cada día")

def elegir_dia(): 
    dia = input(f"Presiona el número del día del que quieres crear la carpeta y se creará en: \n {ubicacion} Día:   ")
    dia_str = str(dia)
    return dia_str

def crear_carpeta(dia):
    nombre = "Día " +dia
    ruta_carpeta = Path(ubicacion, nombre)
    Path.mkdir(ruta_carpeta)
    print(f"La carpeta de nombre {ruta_carpeta} ha sido creada")
# dia_para_carpeta = 'x'
#while not dia_para_carpeta.isnumeric() or int(dia_para_carpeta) not in range (1,17): 
dia_para_carpeta = elegir_dia()
crear_carpeta(dia_para_carpeta)
#int(dia_para_carpet)
