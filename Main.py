from Servicios import servicios
from Generador_Factura_PDF import Factura
from reconocimiento import camara
from tkinter import *
import os
#from recognition import Login

class Menu():

    #ventana = es el Tk()
    #canvas = el canvas donde se dibujará todo

    def __init__(self,ventana,canvas):
        self.ventana = ventana
        self.canvas = canvas
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
        C_botones.place(x=55,y=200)

        C_factura = Button(C_botones,text = "REALIZAR FACTURA",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.RealizarFactura)
        C_factura.grid(row=0,column = 0,padx = 15, pady = 15)

        B_factura = Button(C_botones,text = "BUSCAR FACTURA",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.BuscarFactura)
        B_factura.grid(row=1,column = 0,padx = 15, pady = 15)

        G_informe = Button(C_botones,text = "GENERAR INFORME",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.GenerarInforme)
        G_informe.grid(row=2,column = 0,padx = 15, pady = 15)

        A_servicio = Button(C_botones,text = "AGREGAR SERVICIO",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.AgregarServicio)
        A_servicio.grid(row=0,column = 1,padx = 15, pady = 15)

        M_servicio = Button(C_botones,text = "MODIFICAR SERVICIO",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.ModificarServicio)
        M_servicio.grid(row=1,column = 1,padx = 15, pady = 15)

        A_PDF = Button(C_botones,text = "ARCHIVOS PDF",bg = "medium turquoise",fg = "black",font=("fixedsys", "20"), command = self.ArchivosPDF)
        A_PDF.grid(row=2,column = 1)

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

        B_añadir = Button(G_canvas,text = "AÑADIR",bg = "CadetBlue2",fg = "black", command = lambda: servicios.Agregar_Servicios_a_Facturar([Var_descripcion.get(), cantidad.get()]))
        B_añadir.grid(row=4,column=2,padx = 5, pady= 10)

        B_crear = Button(G_canvas,text = "CREAR",bg = "CadetBlue2",fg = "black", command = lambda: Factura([Nombre.get(), cedula.get(), Residencia.get(), Correo.get()], servicios.Obtener_Servicios_a_Facturar()))
        B_crear.grid(row=5,column=2,padx = 5, pady= 10)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "CadetBlue2",fg = "black", command = self.Menu)
        B_atras.place(x = 370,y = 520)

    def BuscarFactura(self):

        #PANTALLA BUSCAR Y ELIMINAR FACTURAS
        
        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "aquamarine",fg = "black", command = self.Menu)
        B_atras.place(x = 650,y = 550)

    def GenerarInforme(self):

        #PANTALLA PARA GENERAR EL INFORME

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "aquamarine",fg = "black", command = self.Menu)
        B_atras.place(x = 650,y = 550)

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

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "aquamarine",fg = "black", command = self.Menu)
        B_atras.place(x = 650,y = 550)


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
