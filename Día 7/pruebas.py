class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        self.nombre = nombre
        self.apellido = apellido  # super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        print(nombre)
            #f"El/la cliente {nombre} {apellido} de número de cuenta {numero_cuenta}, presenta el siguiente balance: \n {balance}")

    def depositar(self, balance):
        # dinero_a_ingresar = input("¿Cuánto dinero quieres ingresar? (ingresa la cifra y presiona Enter)")
        # balance = 12
        print(balance)
        # return Cliente(balance) += dinero_a_ingresar


cliente1 = Cliente('Daniel', 'Penedo', 21312, 999)

# cliente1.depositar()
