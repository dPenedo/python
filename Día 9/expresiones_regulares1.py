import re

patron = r"\N+\w{3}+-+\d{5}"


patron = r''#La r antes de las comillas indica que es un patron regular
patron = r'\d\d\d-\d\d\d-\d\d\d\d' #Tres dígitos al comienzo, guión, tres dígitos más, guión y cuatro dígitos
patron = r'\d{3}-\d{3}-\d{4}' #Igual que el anterior

Carácteres_especiales = {
'\d': 'Dígito numérico',
'\w': 'Caracter alfanumérico',
'\s': 'espeacio en blanco',
'\D': 'Dígito NO numérico',
'\W': 'Caracter NO alfanumérico, es decir, signos',
'\S': 'SIN espacio en blanco',
}
Cuantificadores = {
'+': 'Aparece una o más veces',
'*': 'Aparece 0 o más veces',
'{n}': 'Se repite n veces',
'{n,m}': 'Se repite de n a m veces',
'{n,}': 'Desde n hacia arriba',
'?': 'Un caracter aparece una vez o ninguna'
}

email_com = '\w+@\w+.com'



texto = "Si necesitas ayuda llama al 644-554-3543 las 24 horas al servicio de ayuda online"
patron = r'\d\d\d-\d\d\d-\d\d\d\d'

spatron = 'Si'
buscar = re.st
print(buscar)

# search busca un patron en un objeto
# findall busca todos los patrones en un objeto
# span escribe la ubicación del patron en un objeto
# start escribe la ubicación del comienzo
# end escribe la ubicación del final
'''
busqueda = re.search(patron, texto)
if busqueda:
    print('La movida')
else:
    print('ohmaygooooot')'''
