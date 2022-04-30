def prueba(num1, num2, *args, **kwargs):

    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f'{clave} ={valor}')


args = [100,232,23233,322]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15,50,*args, **kwargs)
# def suma(**kwargs):

#     total = 0
#     for clave, valor in kwargs.items():
#         print(f'{clave} es igual a {valor}')
#         total += valor
    
#     return total

# print(suma(x=3, y =5, z=3))