class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Client (Persona):
    def__init__(self, nombre, apellido, numero_cuenta, balance = 0):
