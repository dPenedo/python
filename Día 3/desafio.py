frase = input("Escribe una frase. Que tenga unas cuantas palabras, pero en una oración:")
frase_minus = frase.lower()
letras = input("Escribe 3 letras:")
letra1 = letras[0]
letra2 = letras[1]
letra3 = letras[2]
cuenta1 = str(frase_minus.count(letra1))
cuenta2 = str(frase_minus.count(letra2))
cuenta3 = str(frase_minus.count(letra3))

print("Este es el análisis. Tiene 5 puntos:")
print("1) En el texto aparecen "+ cuenta1 +" veces la letra "+ letra1 +", "+ cuenta2 + " veces la letra "+ letra2+ " y "+ cuenta3+ " veces la letra " + letra3 + ".")
frase_en_lista = list(frase_minus)
recuento = str(len(frase_en_lista))
recuento_palabras = str(frase_en_lista.count(" ")+1)
print("2) Por otro lado, aparecen "+ recuento + " letras en total y " + recuento_palabras + " palabras." )
primera_letra = frase_minus[0]
ultima_letra = frase_minus[-1]
print("3) Además, la primera letra de la frase es: "+ primera_letra +" y la última es: "+ ultima_letra +".")

inverso = frase_en_lista[::-1]
inverso_string = str(inverso)
unir = inverso_string.replace("'" ,"")
unir2 = unir.replace(",","")
unir3 = unir2.replace(" ", "")
print("4) También, la frase en orden inverso sería escrita así: " + unir3)

python_texto = "python" in frase_minus
if python_texto == True :
    print("5) Por último, decir que la palabra Python sí que aparece en el texto.")

else :
    print("5) Por último, decir que la palabra Python no aparece en el texto.")



