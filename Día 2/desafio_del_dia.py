# nombre= input("Nombre del trabajador: ")
# sueldo= int(input("Sueldo: "))
# print(f"Aplicando el 13%, el resultado será {sueldo*13/100}, para {nombre}")


nombre1 = input("¿Nombre?")
ventas = input("¿Ventas?")
ventas = int(ventas)
comision = ventas *13/100
comision=round(comision)
print(f"Hola {nombre1}, tu comisión es de {comision}$")