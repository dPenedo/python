import cv2
import face_recognition as fr
import os

# Crear base de datos

ruta ='Empleados'

mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)


for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)


# Codificar imagenes
def codificar(imagenes):
    #Crear una lista nueva
    lista_codificada = []
    # pasar imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a lista
        lista_codificada.append(codificado)
    # Devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

#Tomar una imagen de camara web

captura = cv2.VideoCapture(2, cv2.CAP_ANY)

# leer la imagen de la camara
print(captura)
exito, imagen = captura.read()

if not exito:
    print("No se pudo tomar la captura")
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    
    # Codificar la cara capturada

    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)


