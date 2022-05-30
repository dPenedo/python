from tkinter import *

# iniciar tkinter
aplicacion = Tk()


#Tamaño de la ventana

aplicacion.geometry('1020x630+0+0')

# Evitar maximizar

aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title('Mi restaurante - Sistema de facturación')

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side= TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text = 'Sistema de Facturacion', fg= 'azure4', font=('Dosis', 38), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd = 1, relief= FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd = 1,relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel Comidas

panel_comidas= LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)


panel_bebidas= LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

panel_postres= LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# Panel derecha

panel_derecha = Frame(aplicacion, bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel Caluladora

panel_calculadora= Frame(panel_derecha, bd=1, relief=FLAT, bg=('burlywood'))
panel_calculadora.pack()

#Panel de recibo

panel_de_recibo= Frame(panel_derecha, bd=1, relief=FLAT, bg=('burlywood'))
panel_de_recibo.pack()

#Panel de botones

panel_de_botones= Frame(panel_derecha, bd=1, relief=FLAT, bg=('burlywood'))
panel_de_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'Maccarronnni']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']



# Generar items comida
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
                        font=('Ubuntu light', 19, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_comida[contador] )
    comida.grid(row=contador, 
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                font=('Ubuntu condensed', 16, 'bold'), 
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
                        font=('Ubuntu light', 19, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_bebida[contador] )
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    #Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    cuadros_bebida[contador] = Entry(panel_bebidas, 
                                font=('Ubuntu condensed', 16, 'bold'), 
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
                        font=('Ubuntu light', 19, 'bold'), 
                        onvalue = 1, 
                        offvalue=0, 
                        variable = variables_postre[contador] )
    postre.grid(row=contador, column=0, sticky=W)
    #Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    cuadros_postres[contador] = Entry(panel_postres, 
                                font=('Ubuntu condensed', 16, 'bold'), 
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                column=1)
    contador +=1




# evitar que la pantalla se cierra

aplicacion.mainloop()
