import datetime
from datetime import datetime #Para combinar fecha y hora
from datetime import date #


despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 35)

vigilia = duerme - despierta #

print(vigilia)




# nacimiento = date(1995, 3, 3)
# defuncion = date (2200, 4, 1)
# vida = defuncion - nacimiento
# print(vida.days)






# mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)

# mi_fecha = mi_fecha.replace(month=11)

# print(mi_fecha)





# mi_dia = datetime.date(2025, 10, 17)
# print(mi_dia.today())

# mi_hora = datetime.time(17, 35, 50, 1500)
# print(mi_hora)
