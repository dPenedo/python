class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El/la cliente {self.nombre} {self.apellido} de número de cuenta {self.numero_cuenta}, presenta el siguiente balance: \n ${self.balance}"
    
    def depositar(self, monto_depositar):
        self.balance += monto_depositar
        print("Deposito aceptado")
        # return Cliente(balance) += dinero_a_ingresar

    def retirar(self, monto_de_retiro):
        if self.balance>= monto_de_retiro:
            self.balance -= monto_de_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su Apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def comenzar():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input ()
        opcion= opcion.upper()
        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print('Gracias por operar en aquesta mogudeta')


comenzar()
