# Este archivo contiene las funciones


def comenzar():
    print('Bienvenidos/as al sistema de turnos de la Farmacia\n ¿De qué sección desea tomar un turno?\n[1]Perfumería \n[2] Farmacia\n[3]Cosmética\n[4]Finalizar\n')
    seccion=input('(Presione el número de la sección y la tecla Enter)\n')
    return int(seccion)


    #if seccion == 1:
    #    return int(seccion)
    #elif seccion ==2:
    #    return int(seccion)
    #elif seccion == 3:
    #    return 3

#finalizar=False
#while not finalizar:
eleccion = comenzar()
if eleccion == 1:
    perfumeria()
elif eleccion == 2:
    farmacia()
elif eleccion == 3:
    cosmetica()
elif eleccion ==4:
    finalizar=True
        

