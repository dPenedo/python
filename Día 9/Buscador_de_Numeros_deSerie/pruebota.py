def buscador(documento):
    archivo = open(documento, 'r')
    texto = archivo.readlines()
    texto_str = str(texto)
    archivo.close()
    if patron in texto_str:
        print(patron)
        print(f"Y este es el textote{texto_str} en {documento}")
    else:
        print("No se encuentra disponiblot")
