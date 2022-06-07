from tkinter import *
import random
import datetime

operador=''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x+=1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x+=1
    x = 0
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x+=1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p+=1
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p+=1
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p+=1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'${round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'${round(sub_total_postres, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 52 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 60 + '\n')
    
    x=0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                    f'${int(comida.get())* precios_comida[x]}\n')
        x+=1
    x=0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                    f'${int(bebida.get())* precios_bebida[x]}\n')
        x+=1
    x=0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                    f'${int(postres.get())* precios_postres[x]}\n')
        x+=1
    

    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los Postres:\t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n')


# iniciar tkinter
aplicacion = Tk()


#Tamaño de la ventana

aplicacion.geometry('1140x600+0+0')

# Evitar maximizar

aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Mi restaurante - Sistema de facturación')

# Color de fondo de la ventana
aplicacion.config(bg='#1f1f28')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side= TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text = 'Sistema de Facturacion', fg= 'white', font=('Cambria', 38, 'bold'), bg='#1f1f28', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd = 1, relief= FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd = 1,relief=FLAT , bg='#14141b', padx=20)
panel_costos.pack(side=BOTTOM)

# Panel Comidas

panel_comidas= LabelFrame(panel_izquierdo, text='Comida', font=('Cambria', 15, 'bold'), bd = 1, relief=FLAT, fg='#14141b')
panel_comidas.pack(side=LEFT)


panel_bebidas= LabelFrame(panel_izquierdo, text='Bebidas', font=('Cambria', 15, 'bold'), bd = 1, relief=FLAT, fg='#14141b')
panel_bebidas.pack(side=LEFT)

panel_postres= LabelFrame(panel_izquierdo, text='Postres', font=('Cambria', 15, 'bold'), bd = 1, relief=FLAT, fg='#14141b')
panel_postres.pack(side=LEFT)


# Panel derecha

panel_derecha = Frame(aplicacion, bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel Caluladora

panel_calculadora= Frame(panel_derecha, bd=1, relief=FLAT, bg=('#1f1f28'))
panel_calculadora.pack()

#Panel de recibo

panel_de_recibo= Frame(panel_derecha, bd=1, relief=FLAT, bg=('#1f1f28'))
panel_de_recibo.pack()

#Panel de botones

panel_de_botones= Frame(panel_derecha, bd=1, relief=FLAT, bg=('#1f1f28'))
panel_de_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']



# generar items comida
variables_comida = []
cuadros_comida= []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                        text= comida.title(), 
                        font=('Cambria', 13, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_comida[contador],
                        command=revisar_check)
    comida.grid(row=contador, 
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                font=('Cambria', 13, 'bold'), 
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                column=1)
    contador +=1

# Generar items bebida
variables_bebida = [] 
cuadros_bebida= []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:
    
    #Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                        text= bebida.title(), 
                        font=('Cambria', 13, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_bebida[contador],
                        command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    #Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                font=('Cambria', 13, 'bold'), 
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                column=1)
    contador +=1
# Generar items postre
variables_postre = [] 
cuadros_postres= []
texto_postres = []
contador = 0
for postre in lista_postres:

    #crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                        text= postre.title(), 
                        font=('Cambria', 13, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_postre[contador],
                        command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)
    #Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, 
                                font=('Cambria', 13, 'bold'), 
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                column=1)
    contador +=1



var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()
# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                                text='Costo comida',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1)
etiqueta_costo_bebida = Label(panel_costos,
                                text='Costo bebida',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1)

etiqueta_costo_postres = Label(panel_costos,
                                text='Costo postres',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1)

etiqueta_subtotal = Label(panel_costos,
                                text='Subtotal',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                                text='Impuestos',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_impuestos.grid(row=1, column=2)
texto_impuestos = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_impuestos)
texto_impuestos.grid(row=1,column=3, padx=41)

etiqueta_total = Label(panel_costos,
                                text='Total',
                                font=('Cambria', 12, 'bold'),
                                bg= '#14141b',
                                fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                    font=('Cambria', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)

#botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados= []
columnas = 0
for boton in botones:
    boton = Button(panel_de_botones,
            text= boton.title(),
            font = ('Cambria', 12, 'bold'),
            fg='white',
            bg= '#14141b',
            bd=1,
            width=9)
    boton.grid(row=0,
            column=columnas)
    columnas += 1
    botones_creados.append(boton)
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)


# Area de recibo
texto_recibo = Text(panel_de_recibo,
                font=('Cambria',12, 'bold'),
                bd=1,
                width=42,
                height=10)
texto_recibo.grid(row=0,
            column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                            font=('Cambria', 13, 'bold'),
                            width=32,
                            bd=1)
visor_calculadora.grid(row=0,
                    column=0,
                    columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                    '1', '2', '3', 'x', '=', 'del', '0', '/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                    text=boton.title(),
                    font=('Cambria',
                        13,
                        'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=6)
    botones_guardados.append(boton)
    boton.grid(row=fila, 
            column=columna)

    if columna == 3:
        fila += 1
    columna += 1

    if columna ==4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# evitar que la pantalla se cierra
aplicacion.mainloop()
