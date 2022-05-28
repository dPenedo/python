import bs4
import requests

url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')
#print(len(sopa.select('.product_pod')))


ejemplo = libros[0].select('a')[1]['title']

print(ejemplo)
#for n in range(1,11):
#    print(url_base.format(n))


