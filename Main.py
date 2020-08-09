from Generador_Factura_PDF import Cambio_Moneda
from Generador_Factura_PDF import Factura
from Administrar_Facturas import Facturas
from tipo_de_cambio import tipoDeCambio
from reconocimiento import camara
from Servicios import servicios
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter import *
import os
#from recognition import Login

class Menu():

    #ventana = es el Tk()
    #canvas = el canvas donde se dibujará todo

    def __init__(self,ventana,canvas):
        self.ventana = ventana
        self.canvas = canvas
        self.seleccion = ""
        self.ventana.bind("<F3>", lambda event: self.Menu())
        self.usuario = ""
        self.MenuLogin()


    def MenuLogin(self):

        #PANTALLA DE LOGIN Y RESGISTRO

        self.canvas = Canvas(ventana, width=755, height=600,bg= "White",highlightbackground="White")

        self.canvas.config(bg= "White",highlightbackground="White")
        self.canvas.place(x=0,y=0)

        L_texto = Label(self.canvas,text = "DAO´S COORP",font=("fixedsys", "50"),bg="white")
        L_texto.place(x=160,y=30)

        B_login = Button(self.canvas,text = "LOGIN",bg = "salmon",fg = "black",font=("fixedsys", "40"),width=13, command = self.Login)
        B_login.place(x=175,y=250)

        B_registrar = Button(self.canvas,text = "REGRISTRARSE",bg = "salmon",fg = "black",font=("fixedsys", "40"), command = self.Registro)
        B_registrar.place(x=173,y=400)

    def Login(self):

        """Reconocimiento facial para inicio de sesión"""

        datosLogin = camara.InicioSesion()
        if datosLogin[0]:
            self.usuario = datosLogin[1]
            self.Menu()

    def RegistroDeCara(self, nombre):

        """Registra una nueva cara con un nuevo usuario"""

        datosRegistro = camara.RegistrarCara(nombre)
        if datosRegistro[0]:
            self.usuario = datosRegistro[1]
            self.MenuLogin()

    def Registro(self):

        #EL BOTON "FOTO" LO QUE HACE ES MANDARME AL MENU, LUEGO USTED LO CONFIGURA PARA QUE TOME LA FOTO Y LO MANDE AL MENU

        #PATANTALLA DE REGISTRO

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White")
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "REGRISTRO",font=("fixedsys", "50"),bg="white")
        L_texto.place(x=205,y=30)

        C_datos = Canvas(self.canvas,bg= "White",highlightbackground="White")
        C_datos.place(x=180,y=200)

        L_nombre = Label(C_datos,text = "Nombre:",bg="white",fg = "black",font=("fixedsys","30"))
        L_nombre.grid(row=0,column = 0,pady=10)

        E_nombre = Entry(C_datos,bg = "cyan",fg = "black",font=("fixedsys","30"))
        E_nombre.grid(row=1,column = 0,pady=10)
        
        foto = Button(C_datos,text = "Tomar Cara",bg = "cyan",fg = "black",font=("fixedsys","30"), command = lambda: self.RegistroDeCara(E_nombre.get()))
        foto.grid(row=2,column = 0,pady=30)

    def Menu(self):

        #MENU PRINCIPAL

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        Label(self.canvas, text = "Bienvenido, " + self.usuario, bg="white",fg = "black",font=("fixedsys")).place(x=20, y=10)

        L_texto = Label(self.canvas,text = "MENU",font=("fixedsys", "50"),bg="white")
        L_texto.place(x=285,y=30)

        C_botones = Canvas(self.canvas,bg= "White",highlightbackground="White")
        C_botones.place(x=50,y=170)

        C_factura = Button(C_botones,text = "REALIZAR FACTURA",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.RealizarFactura)
        C_factura.grid(row=0,column = 0,padx = 15, pady = 15)

        B_factura = Button(C_botones,text = "BUSCAR FACTURA",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.BuscarFactura)
        B_factura.grid(row=1,column = 0,padx = 15, pady = 15)

        G_informe = Button(C_botones,text = "GENERAR INFORME",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.GenerarInforme)
        G_informe.grid(row=2,column = 0,padx = 15, pady = 15)

        A_servicio = Button(C_botones,text = "AGREGAR SERVICIO",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.AgregarServicio)
        A_servicio.grid(row=0,column = 1,padx = 15, pady = 15)

        M_servicio = Button(C_botones,text = "MODIFICAR SERVICIO",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.ModificarServicio)
        M_servicio.grid(row=1,column = 1,padx = 15, pady = 15)

        A_PDF = Button(C_botones,text = "ARCHIVOS PDF",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"),width = 18, command = self.ArchivosPDF)
        A_PDF.grid(row=2,column = 1)

        Eliminar = Button(C_botones, text="ELIMINAR FACTURA", bg="medium turquoise", fg="black", font=("fixedsys", "20"),width = 18, command = self.EliminarFactura)
        Eliminar.grid(row=3, column=0,padx = 15, pady = 15)

        TipoCambio = Button(C_botones, text="Tipo Cambio", bg="medium turquoise", fg="black", font=("fixedsys", "20"),width = 18, command=self.TipoCambio)
        TipoCambio.grid(row=3, column=1,padx = 15, pady = 15)


    def TipoCambio(self):
        
        self.canvas = Canvas(self.ventana, width=755, height=600, bg="White", highlightbackground="White")
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "REALIZAR TIPO DE CAMBIO",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=20,y=30)

        D_canvas = Canvas(self.canvas,width=500, height=300, bg= "cyan3",highlightbackground="Black")
        D_canvas.place(x=130,y=150)

        self.seleccion = ""
        encabezados = ["N°", "Cliente"]
        datos = Facturas.Mostrar_Todas()

        tabla = ttk.Treeview(columns=encabezados, show="headings")
        tabla.place(x=180, y=185)

        for encabezado in encabezados: # Escribe los encabezados de la tabla
            tabla.heading(encabezado, text=encabezado.title())
        for dato in datos:  # Escribe los datos de la tabla
            tabla.insert('', 'end', values=dato)

        #  Almacena el valor seleccionado en la tabla   #
        def seleccionar(seleccionado):
            self.seleccion = seleccionado.widget.selection()

        tabla.bind('<<TreeviewSelect>>', seleccionar) # Al ser seleccionado un elemento de la tabla se llama a la funcion seleccionar (ver arriba)

        # Retorna el numero de factura de la columna seleccionada en la tabla
        def N_PDF(tabla):
            if self.seleccion != "":
                print(tabla.item(self.seleccion[0])['values'][0])
                return(str(tabla.item(self.seleccion[0])['values'][0]))

        B_cambio = Button(self.canvas, text="RELIZAR CAMBIO DE MONEDA", bg="cyan3", fg="black", command=lambda: Cambio_Moneda(tipoDeCambio.ObtenerTipoDeCambio(), N_PDF(tabla))) #Realiza el cambio de moneda
        B_cambio.place(x=250, y=500)

        B_atras = Button(self.canvas, text="ATRÁS", bg="cyan3", fg="black", command=self.Menu)
        B_atras.place(x=450, y=500)
        
    # E: una variable
    # S: Un valor booleano, True si la variable es un entero
    # uso: Sirve como restriccion para entradas de tkiter, para que el usuario solo pueda ingresar numeros
    def Validar_Cant(self, cant):
        return cant.isdigit()

    def RealizarFactura(self):

        servicios.Limpia_Servicios_a_Facturar()

        #PANTALLA DE FACTURAS

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "CREAR FACTURA",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=185,y=30)

        D_canvas = Canvas(self.canvas,width=500, height=400, bg= "CadetBlue2",highlightbackground="Black")
        D_canvas.place(x=130,y=100)

        G_canvas = Canvas(D_canvas,bg= "CadetBlue2",highlightbackground="CadetBlue2")
        G_canvas.place(x=120,y=70)

        Var_descripcion = StringVar(G_canvas)

        lista_descripcion = servicios.Recorre_Servicios_Descripcion()

        Nombre = Entry(G_canvas)
        Nombre.grid(row=0,column=1,padx = 5, pady= 10)

        L_nombre = Label(G_canvas,text = "Nombre:",bg= "CadetBlue2")
        L_nombre.grid(row=0,column=0,padx = 5, pady= 10)

        Residencia = Entry(G_canvas)
        Residencia.grid(row=1,column=1,padx = 5, pady= 10)

        L_residencia = Label(G_canvas,text = "Residencia:",bg= "CadetBlue2")
        L_residencia.grid(row=1,column=0,padx = 5, pady= 10)
        
        Correo = Entry(G_canvas)
        Correo.grid(row=2,column=1,padx = 5, pady= 10)

        L_correo = Label(G_canvas,text = "Correo:",bg= "CadetBlue2")
        L_correo.grid(row=2,column=0,padx = 5, pady= 10)

        cedula = Entry(G_canvas)
        cedula.grid(row=3,column=1,padx = 5, pady= 10)

        L_cedula = Label(G_canvas,text = "Cedula:",bg= "CadetBlue2")
        L_cedula.grid(row=3,column=0,padx = 5, pady= 10)

        menu_id_descripcion = OptionMenu(G_canvas,Var_descripcion,*lista_descripcion)
        menu_id_descripcion.config(width=5,bg="CadetBlue2",highlightbackground="CadetBlue2")
        menu_id_descripcion.grid(row=4,column=1,padx = 5, pady= 10)

        L_descripcion = Label(G_canvas,text = "Servicio:",bg= "CadetBlue2")
        L_descripcion.grid(row=4,column=0,padx = 5, pady= 10)

        cantidad = Entry(G_canvas)
        cantidad.grid(row=5,column=1,padx = 5, pady= 10)
        validacion = G_canvas.register(self.Validar_Cant)
        cantidad.config(validate="key", validatecommand=(validacion, '%S'))

        L_cantidad = Label(G_canvas,text = "Cantidad:",bg= "CadetBlue2")
        L_cantidad.grid(row=5,column=0,padx = 5, pady= 10)

        B_añadir = Button(G_canvas,text = "AÑADIR",bg = "CadetBlue2",fg = "black", command = lambda: servicios.Agregar_Servicios_a_Facturar([Var_descripcion.get(), cantidad.get()])) # Añade un servicio a facturar
        B_añadir.grid(row=4,column=2,padx = 5, pady= 10)

        B_crear = Button(G_canvas,text = "CREAR",bg = "CadetBlue2",fg = "black", command = lambda: Factura([Nombre.get(), cedula.get(), Residencia.get(), Correo.get()], servicios.Obtener_Servicios_a_Facturar())) # Crea una factura según los servicios dados
        B_crear.grid(row=5,column=2,padx = 5, pady= 10)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "CadetBlue2",fg = "black", command = self.Menu)
        B_atras.place(x = 370,y = 520)

    def BuscarFactura(self):

        #PANTALLA BUSCAR Y ELIMINAR FACTURAS
        
        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "white",highlightbackground="White")
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "BUSCAR FACTURA",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=170,y=30)

        D_canvas = Canvas(self.canvas,width=300, height=150, bg= "PaleVioletRed1",highlightbackground="Black")
        D_canvas.place(x=230,y=350)

        C_datos= Canvas(D_canvas, bg= "PaleVioletRed1",highlightbackground="PaleVioletRed1")
        C_datos.place(x=37,y=20)

        DE = Label(C_datos, text = "De",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="#d5cee9")
        DE.grid(row=1, column = 0)

        dia_inicial = Entry(C_datos, width = 2)
        dia_inicial.grid(row=1, column = 1)
        L_DI = Label(C_datos, text = "Dia",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_DI.grid(row=0, column = 1)

        mes_inicial = Entry(C_datos, width = 2)
        mes_inicial.grid(row=1, column = 2)
        L_MI = Label(C_datos, text = "Mes", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_MI.grid(row=0, column = 2)

        año_inicial = Entry(C_datos, width = 4)
        año_inicial.grid(row=1, column = 3)
        L_AI = Label(C_datos, text = "Año", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_AI.grid(row=0, column = 3)

        A = Label(C_datos, text = "a", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="#d5cee9")
        A.grid(row=1, column = 4)

        dia_final = Entry(C_datos, width = 2)
        dia_final.grid(row=1, column = 5)
        L_DF = Label(C_datos, text = "Dia",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_DF.grid(row=0, column = 5)

        mes_final = Entry(C_datos, width = 2)
        mes_final.grid(row=1, column = 6)
        L_MF = Label(C_datos, text = "Mes",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_MF.grid(row=0, column = 6)

        año_final = Entry(C_datos, width = 4)
        año_final.grid(row=1, column = 7)
        L_AF = Label(C_datos, text = "Año", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_AF.grid(row=0, column = 7)

        entradas = [dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final]  # Almacena las entradas de dias, meses y años en una lista para facilitar sus manipulacio
        for i in entradas: # Restringe los valores ingresable es las entradas a unicamente enteros
            validacion = self.canvas.register(self.Validar_Cant)
            i.config(validate="key", validatecommand=(validacion, '%S'))

        B_buscar = Button(D_canvas, text="BUSCAR", bg="white", fg="black", command= lambda: mostrar()) # Muestra las facturas que se encuentran en el rango de fechas dado
        B_buscar.place(x=70, y=100)

        B_atras = Button(D_canvas,text = "ATRÁS", bg = "white",fg = "black", command = self.Menu)
        B_atras.place(x = 200,y = 100)

        #  Despliega la lista de facturas que se encuentran en el rango de fechas dadas
        def mostrar():
            try:
                # Obietene los datos de las tablas y el monto total de sumarlas
                datos, total = Facturas.Buscar_por_Fechas([int(año_inicial.get()), int(mes_inicial.get()), int(dia_inicial.get())], [int(año_final.get()), int(mes_final.get()), int(dia_final.get())])

                encabezados = ["N°", "Cliente", "Monto a pagar", "Vencimiento"] # Encabezados de la listbox (tabla)

                tabla = ttk.Treeview(columns=encabezados, show="headings", height=4) # Crea la listbox (tabla)
                tabla.place(x=0, y=100)  # Posiciona la tabla

                for encabezado in encabezados:  # Escribe los encabezados de la listbox
                    tabla.heading(encabezado, text=encabezado.title())
                for dato in datos:  # Escribe los datos que contiene la listbox
                    tabla.insert('', 'end', values=dato)

                encabezados_2 = ["TOTAL"] # Encabezado de la tabla2

                tabla2 = ttk.Treeview(columns=encabezados_2, show="headings", height=1) # Crea la tabla 2
                tabla2.place(x=280, y=250) # Posiciona la tabla 2

                for encabezado in encabezados_2:  # Escribe los encabezados_2 de la tabla2
                    tabla2.heading(encabezado, text=encabezado.title())
                tabla2.insert('', 'end', values=total)  # Escribe el total de sumar el precio de las facturas mostradas


            except:
                messagebox.showinfo("Error de datos", "Hay un error en los datos ingresados")


    def EliminarFactura(self):
        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        self.seleccion = ""  # reinicia el valor seleccionado en la tabla

        L_texto = Label(self.canvas,text = "ELIMINAR FACTURA",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=140,y=30)

        D_canvas = Canvas(self.canvas,width=675, height=300, bg= "PaleVioletRed1",highlightbackground="Black")
        D_canvas.place(x=40,y=150)

        encabezados = ["N°", "Cliente", "Monto"]
        datos = Facturas.Mostrar_Todas()

        tabla = ttk.Treeview(columns=encabezados, show="headings")
        tabla.place(x=75, y=185)

        # For de listbox
        for encabezado in encabezados:
            tabla.heading(encabezado, text=encabezado.title())
        for dato in datos:
            tabla.insert('', 'end', values=dato)

        def seleccionar(seleccionado): # Almacena el dato seleccionado de la tabla
            self.seleccion = seleccionado.widget.selection()

        def Eliminar(tabla): # Si se ha seleccionado una factura en la tabla, la elimina
            if self.seleccion != "":
                #print(tabla.item(self.seleccion[0])['values'][0])
                Facturas.Eliminar([str(tabla.item(self.seleccion[0])['values'][0])])
                self.EliminarFactura() # usar esto para refrescar ó hacer de de la tabla un atributo

        tabla.bind('<<TreeviewSelect>>', seleccionar)

        B_eliminar = Button(self.canvas, text="ELIMINAR", bg="PaleVioletRed1", fg="black", command= lambda: Eliminar(tabla))  #  Elimina la factura seleccionada
        B_eliminar.place(x=275, y=500)

        B_atras = Button(self.canvas, text="ATRÁS", bg="PaleVioletRed1", fg="black", command=self.Menu)
        B_atras.place(x=400, y=500)



    def GenerarInforme(self):

        #PANTALLA PARA GENERAR EL INFORME

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White")
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "GENERAR INFORME",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=140,y=30)

        D_canvas = Canvas(self.canvas,width=675, height=300, bg= "PaleVioletRed1",highlightbackground="Black")
        D_canvas.place(x=40,y=150)

        C_datos= Canvas(D_canvas, bg= "PaleVioletRed1",highlightbackground="PaleVioletRed1")
        C_datos.place(x=220,y=140)

        DE = Label(C_datos, text = "De",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="#d5cee9")
        DE.grid(row=1, column = 0)

        dia_inicial = Entry(C_datos, width = 2)
        dia_inicial.grid(row=1, column = 1)
        L_DI = Label(C_datos, text = "Dia",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_DI.grid(row=0, column = 1)

        mes_inicial = Entry(C_datos, width = 2)
        mes_inicial.grid(row=1, column = 2)
        L_MI = Label(C_datos, text = "Mes", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_MI.grid(row=0, column = 2)

        año_inicial = Entry(C_datos, width = 4)
        año_inicial.grid(row=1, column = 3)
        L_AI = Label(C_datos, text = "Año", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_AI.grid(row=0, column = 3)

        A = Label(C_datos, text = "a", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="#d5cee9")
        A.grid(row=1, column = 4)

        dia_final = Entry(C_datos, width = 2)
        dia_final.grid(row=1, column = 5)
        L_DF = Label(C_datos, text = "Dia",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_DF.grid(row=0, column = 5)

        mes_final = Entry(C_datos, width = 2)
        mes_final.grid(row=1, column = 6)
        L_MF = Label(C_datos, text = "Mes",font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_MF.grid(row=0, column = 6)

        año_final = Entry(C_datos, width = 4)
        año_final.grid(row=1, column = 7)
        L_AF = Label(C_datos, text = "Año", font=("fixedsys"), anchor="center", bg= "PaleVioletRed1",fg ="white")
        L_AF.grid(row=0, column = 7)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "white",fg = "black", command = self.Menu)
        B_atras.place(x = 340,y = 400)

        entradas = [dia_inicial, mes_inicial, año_inicial, dia_final, mes_final, año_final]
        for i in entradas: # Restringe los valores ingresables  de las entradas a unicamente enteros
            validacion = self.canvas.register(self.Validar_Cant)
            i.config(validate="key", validatecommand=(validacion, '%S'))

        def Informe(datos):
            try:

                encabezados = ["Monto Total", "Impuestos"]

                tabla = ttk.Treeview(columns=encabezados, show="headings", height = 1)
                tabla.place(x=175, y=200)

                for encabezado in encabezados:
                    tabla.heading(encabezado, text=encabezado.title())
                for dato in datos:
                    tabla.insert('', 'end', values=dato)
            except:
                messagebox.showinfo("Error de datos", "Hay un error en los datos ingresados")

        B_Informe = Button(self.canvas, text="INFORME GENERAL", bg="White", fg="black", command= lambda: Informe([Facturas.Informe_General()]))
        B_Informe.place(x=430, y=400)

        B_Informe2 = Button(self.canvas, text="INFORME", bg="White", fg="black", command=lambda: Informe([Facturas.Informe_Fechas([año_inicial.get(), mes_inicial.get(), dia_inicial.get()], [año_final.get(), mes_final.get(), dia_final.get()])]))
        B_Informe2.place(x=230, y=400)



    def AgregarServicio(self):

        #AGREGAR UN SERVICIO

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        L_texto = Label(self.canvas,text = "AGREGAR SERVICIO",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=135,y=30)

        D_canvas = Canvas(self.canvas,width=500, height=300, bg= "light steel blue",highlightbackground="black")
        D_canvas.place(x=130,y=125)

        descripcion = Text(D_canvas, width = 20, height= 5)
        descripcion.place(x=175,y=65)

        costo = Entry(D_canvas)
        costo.place(x=190,y= 200)

        L_descripcion = Label(D_canvas,text = "Descripción:",bg= "light steel blue")
        L_descripcion.place(x=220,y=40)

        L_precio = Label(D_canvas,text = "Costo:",bg= "light steel blue")
        L_precio.place(x=230,y=170)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "light steel blue",fg = "black", command = self.Menu)
        B_atras.place(x = 450,y = 500)

        C_modificar = Button(self.canvas,text = "CREAR",bg = "light steel blue",fg = "black", command = lambda: servicios.Validar_Nuevo_Servicio(descripcion.get("1.0","end-1c"), costo.get())) #LLAMADA AL CREAR SERVICIO
        C_modificar.place(x = 270,y = 500)

    def ModificarServicio(self):

        #PANTALLA PARA MODIFICAR EL SERVICIO

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        D_canvas = Canvas(self.canvas,width=500, height=300, bg= "skyblue4",highlightbackground="black")
        D_canvas.place(x=130,y=125)

        L_texto = Label(self.canvas,text = "MODIFICAR SERVICIO",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=115,y=30)

        Var_id = StringVar(D_canvas)

        lista_id_servicios = servicios.Recorre_Servicios() #LLAMAR AL MODULO QUE SAQUE LOS IDS DE LOS SERVICIOS

        M_descripcion = Text(D_canvas, width = 20, height= 5)
        M_descripcion.place(x=250,y=100)

        M_costo = Entry(D_canvas)
        M_costo.place(x=240,y= 250)

        menu_id_servicios = OptionMenu(D_canvas,Var_id,*lista_id_servicios)
        menu_id_servicios.config(width=5,bg="skyblue4",highlightbackground="skyblue4")
        menu_id_servicios.place(x=250,y=30)

        L_id = Label(D_canvas,text = "ID del servicio:",bg= "skyblue4")
        L_id.place(x=160,y=30)

        L_descripcion = Label(D_canvas,text = "Descripción:",bg= "skyblue4")
        L_descripcion.place(x=170,y=95)

        L_precio = Label(D_canvas,text = "Costo:",bg= "skyblue4")
        L_precio.place(x=195,y=250)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "skyblue4",fg = "black", command = self.Menu)
        B_atras.place(x = 450,y = 500)

        B_modificar = Button(self.canvas,text = "MODIFICAR",bg = "skyblue4",fg = "black", command = lambda: servicios.Modificar_Servicio(Var_id.get(), M_descripcion.get("1.0","end-1c"), M_costo.get())) #LLAMADA AL MODIFICAR SERVICIO
        B_modificar.place(x = 270,y = 500)


    def ArchivosPDF(self):

        #PANTALLA PARA CONTROLAR LOS PDF´S

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)
        self.seleccion = ""
        encabezados = ["N°", "Cliente"]
        datos = Facturas.Mostrar_Todas()

        L_texto = Label(self.canvas,text = "ARCHIVOS PDF",font=("fixedsys", "40"),bg="white")
        L_texto.place(x=190,y=30)

        D_canvas = Canvas(self.canvas,width=500, height=300, bg= "skyblue1",highlightbackground="Black")
        D_canvas.place(x=130,y=150)

        tabla = ttk.Treeview(columns=encabezados, show="headings")
        tabla.place(x=175, y=190)

        for encabezado in encabezados:
            tabla.heading(encabezado, text=encabezado.title())
        for dato in datos:
            tabla.insert('', 'end', values=dato)

        def seleccionar(seleccionado):
            self.seleccion = seleccionado.widget.selection()


        tabla.bind('<<TreeviewSelect>>', seleccionar)

        def Abrir(tabla):
            if self.seleccion != "":
                print(tabla.item(self.seleccion[0])['values'][0])
                Facturas.Mostrar_PDF(str(tabla.item(self.seleccion[0])['values'][0]))

        B_abrir = Button(self.canvas, text="ABRIR", bg="skyblue1", fg="black", command=lambda: Abrir(tabla))
        B_abrir.place(x=300, y=490)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "skyblue1",fg = "black", command = self.Menu)
        B_atras.place(x = 400,y = 490)


# CREAR VENTANA DEL PROGRAMA
ventana = Tk()
ventana.title("Proyecto número 3")
ventana.minsize(750,600)
ventana.resizable(width=NO,height=NO)
ventana.config( bg= "Black")
os.environ['SDL_VIDEO_CENTERED'] = '1'

#CREAR CANVAS DEL PROGRAMA
canvas = Canvas(ventana, width=755, height=600,bg= "White",highlightbackground="White")
canvas.place(x=-5, y=0)

#CREAR EL OBJETO DE LA INTERFAZ
Menu(ventana,canvas)

ventana.mainloop()
