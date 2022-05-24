
def buscador(texto):
    patron = r"N+\w{3}-\d{5}"
    busqueda = re.search(patron, texto)
    return 



# Impresión de tabla
def imprimir_tabla(lista_archivos):
    print('-'*50)
    print(f'Fecha de búsqueda:{fecha}'
    print('ARCHIVO\tNRO. SERIE')
    print('-------\t-----------')
    for arch, num in lista_archivos:
        print(f'{arch}\t{num}')
    print(f'Números encontrados:{len(lista_archivos)}')
    print(f'Duración de la búsqueda: {segundos} segundos')

def imprimir_fecha():
    print()
