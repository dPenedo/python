from pathlib import Path, PureWindowsPath

carpeta = Path("/home/dani/Documentos/python/dia6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
print(carpeta)

# if not carpeta.exists():
#     print('Este archivo no existe')
# else:
#     print('Genial, existee')


# print
# print(carpeta.stem) #Prueba
# print(carpeta.suffix) #.txt
# print(carpeta.name) #prueba.txt
# print(carpeta.read_text()) #read
