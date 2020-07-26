from tkinter import *
from recognition import camara
import os
#from recognition import Login

class Menu():

    #ventana = es el Tk()
    #canvas = el canvas donde se dibujará todo

    def __init__(self,ventana,canvas):

        self.ventana = ventana
        self.canvas = canvas
        self.MenuLogin()

    def MenuLogin(self):

        #PANTALLA DE LOGIN Y RESGISTRO

        self.canvas.config(bg= "White",highlightbackground="White")

        B_login = Button(self.canvas,text = "LOGIN",bg = "aquamarine",fg = "black",font=("fixedsys", "40"),width=13, command = self.LoginReconocer)
        B_login.place(x=100,y=100)

        B_registrar = Button(self.canvas,text = "REGRISTRARSE",bg = "aquamarine",fg = "black",font=("fixedsys", "40"), command = self.Registro)
        B_registrar.place(x=100,y=250)

    def LoginReconocer(self):
        datosLogin = camara.InicioSesion()
        if datosLogin[0]:
            self.usuairo = datosLogin[1]
            self.Menu()

    def Login(self):

        #lUIS AQUI BORRE ESTO SI QUIERE Y QUE DE AQUI MANDE A EL ESCANEO DE LA CARA PERO CUANDO INGRESA MANDELO A MENÚ Y SI QUIERE PUEDE METER UN BOTON QUE LO MANDE A MENULOGIN

        #PANALLA DE LOGIN
        
        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "Black",highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        
        Foto = Button(self.canvas,text = "MENU",bg = "black",fg = "gold", command = self.Menu)
        Foto.place(x=500,y=490)

    def Registro(self):

        #EL BOTON "FOTO" LO QUE HACE ES MANDARME AL MENU, LUEGO USTED LO CONFIGURA PARA QUE TOME LA FOTO Y LO MANDE AL MENU

        #PATANTALLA DE REGISTRO

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White")
        self.canvas.place(x=-5, y=0)

        C_datos = Canvas(self.canvas,bg= "White",highlightbackground="White")
        C_datos.place(x=250,y=200)

        L_nombre = Label(C_datos,text = "Nombre:",bg="white",fg = "black",font=("fixedsys"))
        L_nombre.grid(row=0,column = 0)

        E_nombre = Entry(C_datos,bg = "aquamarine",fg = "black",font=("fixedsys"))
        E_nombre.grid(row=0,column = 1)
        
        foto = Button(self.canvas,text = "Tomar Foto",bg = "aquamarine",fg = "black", command = camara.RegistrarCara)
        foto.place(x=330,y=300)

    def Menu(self):

        #MENU PRINCIPAL

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        C_botones = Canvas(self.canvas,bg= "White",highlightbackground="White")
        C_botones.place(x=250,y=200)

        C_factura = Button(C_botones,text = "REALIZAR FACTURA",bg = "aquamarine",fg = "black", command = self.RealizarFactura)
        C_factura.grid(row=0,column = 0,padx = 5, pady = 5)

        B_factura = Button(C_botones,text = "BUSCAR FACTURA",bg = "aquamarine",fg = "black", command = self.BuscarFactura)
        B_factura.grid(row=1,column = 0,padx = 5, pady = 5)

        G_informe = Button(C_botones,text = "GENERAR INFORME",bg = "aquamarine",fg = "black", command = self.GenerarInforme)
        G_informe.grid(row=2,column = 0,padx = 5, pady = 5)

        A_servicio = Button(C_botones,text = "AGREGAR SERVICIO",bg = "aquamarine",fg = "black", command = self.AgregarServicio)
        A_servicio.grid(row=0,column = 1,padx = 5, pady = 5)

        M_servicio = Button(C_botones,text = "MODIFICAR SERVICIO",bg = "aquamarine",fg = "black", command = self.ModificarServicio)
        M_servicio.grid(row=1,column = 1,padx = 5, pady = 5)

        A_PDF = Button(C_botones,text = "ARCHIVOS PDF",bg = "aquamarine",fg = "black", command = self.ArchivosPDF)
        A_PDF.grid(row=2,column = 1)

    def RealizarFactura(self):

        #PANTALLA DE FACTURAS

        self.canvas = Canvas(self.ventana, width=755, height=600,bg= "White",highlightbackground="White") 
        self.canvas.place(x=-5, y=0)

        B_atras = Button(self.canvas,text = "ATRÁS",bg = "aquamarine",fg = "black", command = self.Menu)
        B_atras.place(x = 650,y = 550)

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

        C_modificar = Button(self.canvas,text = "CREAR",bg = "light steel blue",fg = "black", command = self.Menu) #LLAMADA AL CREAR SERVICIO
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

        lista_id_servicios = [1,2,3,4] #LLAMAR AL MODULO QUE SAQUE LOS IDS DE LOS SERVICIOS

        M_descripcion = Text(D_canvas, width = 20, height= 5)
        M_descripcion.place(x=250,y=100)

        M_costo = Entry(D_canvas)
        M_costo.place(x=210,y= 250)

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

        B_modificar = Button(self.canvas,text = "MODIFICAR",bg = "skyblue4",fg = "black", command = self.Menu) #LLAMADA AL MODIFICAR SERVICIO
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
