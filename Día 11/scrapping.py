import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2022/05/la-recursividad-paso-paso.html')



sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title')[0].getText())

parrafo_especial = sopa.select('p')[6].getText()
print(parrafo_especial)
#print(resultado.text)

