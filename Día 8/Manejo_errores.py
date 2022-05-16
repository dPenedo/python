# Código para que sólo se puedan ingresar números:
def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")
pedir_numero()
#
pedir_numero()
#
def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" +n1)


'''try:
    # Codigo que queremos probar
    suma()
except TypeError: # Codigo a ejecutar si hay un error
    print("La has liado concatenando distintos tipos. Hay algo que va mal")
except ValueError:
    print("Ese no es un númerro")
else:
    # Código a ejecutar si no hay error
    print("Hiciste todo bien")
finally:
    # Código que se ejecuta de todos modos
    print("Eso fue todo.")'''