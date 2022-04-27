frase = input("Escribe una frase. Que tenga unas cuantas palabras, pero en una oración:")
letras = []
frase = frase.lower()

letras.append(input('Ingrese aquí la primera letra: ').lower())
letras.append(input('Ingrese aquí la segunda letra: ').lower())
letras.append(input('Ingrese aquí la tercera letra: ').lower())

print("Este es el análisis. Tiene 5 puntos:")
cantidad_letras1 = frase.count(letras[0])
cantidad_letras2 = frase.count(letras[1])
cantidad_letras3 = frase.count(letras[2])
print(f"1) En el texto aparecen {cantidad_letras1} veces la letra {letras[0]}, {cantidad_letras2} veces la letra {letras[1]} y  {cantidad_letras3} veces la letra {letras[2]}.")

palabras = frase.split()
print(f"2) Por otro lado, aparecen {len(frase)} letras en total y {len(palabras)} palabras." )
primera_letra = frase[0]
ultima_letra = frase[-1]
print(f"3) Además, la primera letra de la frase es: {primera_letra} y la última es: {ultima_letra}.")


palabras.reverse()
texto_invertido = ' '.join(palabras)

print(f"4) También, la frase en orden inverso sería escrita así: '{texto_invertido}'")
buscar_py = 'python' in frase
dic = {True: "sí", False: "no"}
print(f"5) Buscando la palabra python: La palabra 'Python' {dic[buscar_py]} se encuentra en el texto")

