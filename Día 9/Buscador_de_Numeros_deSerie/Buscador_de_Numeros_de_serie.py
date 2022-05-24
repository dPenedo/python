import os
import datetime
import time
import re
from pathlib import Path
import math

ruta = '/home/dani/Documentos/python/Día 9/Buscador_de_Numeros_deSerie/Mi_Gran_Directorio/'
#patron = r"\N+\w{3}+-+\d{5}"
patron = r"N\D{3}-\d{5}"

# Fecha actual con un buen formato:
mi_dia = datetime.date(2025, 10, 17)
hoy = mi_dia.today()
def imprimir_fecha():
    hoy_form = hoy.strftime("%d/%m/%y")
    print(hoy_form)

#Tiempo de inicio, para restar con el del final
inicio = time.time()
numeros_encontrados = []
archivos_encontrados = []

#Busca el patron en el archivo y devuelve el patrón y el archivo


def buscador(documento, patron):
    archivo = open(documento, 'r')
    texto = archivo.read()
    archivo.close()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def recorrer_archivos():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscador(Path(carpeta, a), patron)
            if resultado != '':
                numeros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

# Impresión de tabla
def imprimir_tabla():
    indice = 0
    fecha=imprimir_fecha()
    print('-'*50)
    print(f'Fecha de búsqueda:{fecha}')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t-----------')
    for arch in archivos_encontrados:
        print(f'{arch}\t\t{numeros_encontrados[indice]}')
        indice +=1
    print('\n')    
    print(f'Números encontrados: {len(numeros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-'*50)




recorrer_archivos()
imprimir_tabla()




