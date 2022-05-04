from pathlib import Path
# base = Path.home()

guia = Path("Europa", "Catalunya", "Barcelona", "Sagrada_Familia.txt")
en_Europa = guia.relative_to(Path("Europa"))
en_Catalunya = guia.relative_to(Path("Europa", "Catalunya"))
print(en_Europa)
print(en_Catalunya)


# guia = Path(Path.home(), "Europa")

# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)


# guia = Path(base, "Europa", "Catalunya", Path("Barcelona", "Sagrada_Familia.txt"))
# guia2 = guia.with_name("La_Pedrera,txt")
# print(base)
# print(guia.parent.parent.parent)