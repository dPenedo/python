import os
import datetime
import time
import re


ruta = '/home/dani/Documentos/python/Día 9/Mi_Gran_Directorio/'
patron = r"\N+\w{3}+-+\d{5}"

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


def buscador():
    texto = archivo
    busqueda = re.search(patron, texto)
    if busqueda:
        return si #Hay que sacar el archivo y patron 
    else:
        return no



def crear:lista

def  mostrar #contiene fin:time

crearlis()
mostr()





