# Este modulo contiene los generadores y decoradores
def perfumeria():
    for n in range(1,1000):
        yield f'P -{n}'
def farmacia():
    for n in range(1,1000):
        yield f'F -{n}'
def cosmetica():
    for n in range(1,1000):
        yield f'C -{n}'
