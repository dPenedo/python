import cv2
import face_recognition as fr

# Cargar imagenes

foto_control = fr.load_image_file('prueba2.jpg')
foto_prueba = fr.load_image_file('prueba4.jpg')

# Pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control

lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara prueba

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]


# Mostrar rentangulos

cv2.rectangle(foto_control,
            (lugar_cara_A[3], lugar_cara_A[0]),
            (lugar_cara_A[1], lugar_cara_A[2]),
            (0,255,0),
            2)

cv2.rectangle(foto_prueba,
            (lugar_cara_B[3], lugar_cara_B[0]),
            (lugar_cara_B[1], lugar_cara_B[2]),
            (0,255,0),
            2)
# Realizar comparacion

resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

# Medida de la distancia

distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# Mostrar Resultado

def resultado_color():
    verde = (0,255,0)
    rojo = (0,0,255)
    if resultado == [True]:
        return verde
    if resultado == [False]:
        return rojo
color_resultado = resultado_color()

cv2.putText(foto_prueba,
        f'El resultado es: {resultado} La distancia es de un{(distancia*100).round(0)}%',
        (50, 50),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        color_resultado,
        2)

# Mostrar imagenes

cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)


# Mantener programa abierto

cv2.waitKey(0)
