# Este archivo contiene las funciones
from numeros import perfumeria
from numeros import farmacia
from numeros import cosmetica 
from os import system


def comenzar():
    print('Bienvenidos/as al sistema de turnos de la Farmacia\n ¿De qué sección desea tomar un turno?\n[1]Perfumería \n[2] Farmacia\n[3]Cosmética\n[4]Finalizar\n')
    seccion=input('(Presione el número de la sección y la tecla Enter)\n')
    return int(seccion)

def mostrar_turno(x):
    print(f'su número de turno es el {x}')

fin = False
while not fin:
    eleccion = comenzar()

if eleccion == 1:
    num_perfume = perfumeria()
    nn = next(num_perfume)
    print(f'Su número de turno es el {nn}')
    
elif eleccion == 2:
    farmacia()
elif eleccion == 3:
    cosmetica()
else:
    fin=True


#def mostrar_numero(turno)
#    print(turno)
#mostrar_numero(turno)
