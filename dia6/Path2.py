from cgitb import text
from pathlib import Path

#base = Path.home()
#guia = Path(base,"Europa", "Catalunya",Path("Barcelona", "Sagrada_familia.txt")) #El constructor Path admite tanto cadenas como objetos de Path
# guia2 = guia.with_name("la_pedrera.txt")
# print(base)
#print(guia.parent.parent.parent.parent)

# print(guia2)

# guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
# en_europa = guia.relative_to(Path("Europa"))
# en_espaina = guia.relative_to(Path("Europa", "España"))
# print(en_europa)
# print(en_espaina)
guia = Path(Path.home(), "Europa")
for txt in Path(guia).iterdir():
    if txt.is_dir():
# for txt in Path(guia).glob("**/*.txt"): #Listar todos los archivos .txt en la carpeta y el parent
# for txt in Path(guia).glob("*.txt"): Listar todos los archivos .txt en la carpeta
        print(txt.name)