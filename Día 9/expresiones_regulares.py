import re


texto = "No atendemos los martes por la tarde."
texto1 = "No atendemos los martes por la tarde en la casa."

#buscar = re.search(r'[^\s]', texto)
buscar = re.findall(r'[^\s]+', texto)##

print(''.join(buscar))


#buscar = re.search(r'lunes|martes', texto)
#buscar1 = re.search(r'casa|casas', texto1)
#buscar2 = re.search(r'...demos...|casas', texto1)
#print(buscar)
#print(buscar1)
#print(buscar2)




#clave = input('Clave:')
#patron = r'\D{1}\w{7}'
#
#chequear = re.search(patron, clave)
#
#print(chequear.)



#texto = "Si necesitas ayuda llama al (643)-554-34543 las 24 horas al servicio de ayuda online"
#texto = "llama al 929-454-3453 ya mismo"


#patron = r'\d\d\d-\d\d\d-\d\d\d\d'
#patron = r'\d{3}-\d{3}-\d{4}'

#patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

#resultado = re.search(patron, texto)
#print(resultado.group(0))



# patron = 'ayuda'
# busqueda = re.findall(patron, texto)
# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())


#print(len(busqueda))
#palabra = 'ayuda' in texto
#print(palabra)
