import bs4
import requests


#crear url sin numero

url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista con 4 o 5 estrellas

titulos_rating_alto = []
# Iterar paginas

for pagina in range (1, 51):
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina) 
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:
        #cheqeuar esterllas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')) !=0:
            #Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            #agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

# Ver libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)

