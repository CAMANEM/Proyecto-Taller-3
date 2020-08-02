from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from datetime import timedelta
from datetime import datetime
import json

"""
# formato de variable usuario:
usuario = [nombre, cedula, direccion, correo]

# formato variable Servicios

[{"ID": ID, "tipo": descripcion, "cant": cant},
 {"ID": ID, "tipo": descripcion, "cant": cant},
 ...                                            ]
"""

# Modificar para facturar cada 10 servicios


class Factura:
    def __init__(self, usuario, servicios):
        self.facturas = json.load(open("Servicios/Facturas.json"))
        #print(self.facturas)
        self.pdf = canvas.Canvas("Servicios/Invoices/" + self.facturas["N°_Factura"] + ".pdf")
        self.costo = json.load(open("Servicios/Servicios_y_Costos.json"))
        self.usuario = usuario
        self.servicios = servicios
        self.guard_servicios = self.servicios[:10]
        self.fecha = datetime.now().strftime("%d/%m/%Y")
        self.vence = (datetime.now() + timedelta(days=3)).strftime("%d/%m/%Y")
        self.subtotal = 0
        self.precio = 0
        self.total = 0
        self.y = 500
        self.contador = 0
        self.crear_plantilla()
        self.facturar()
        self.guardar_factura()

    #  Crea la plantilla del pdf
    def crear_plantilla(self):
        pdfmetrics.registerFont(TTFont('abc', 'NewStandard-Regular.ttf'))
        #Figuras
        self.pdf.setStrokeColorRGB(0, 0.8, 0.9)
        self.pdf.setFillColorRGB(0, 0.8, 0.9)
        self.pdf.rect(325, 680, 180, 15, fill=True)
        self.pdf.rect(325, 635, 180, 15, fill=True)
        self.pdf.rect(85, 635, 180, 15, fill=True)
        self.pdf.rect(85, 520, 420, 15, fill=True)
        self.pdf.rect(85, 304, 240, 15, fill=True)
        self.pdf.rect(440, 264, 65, 55, fill=True)
        self.pdf.setStrokeColorRGB(0.77, 0.87, 0.97)
        self.pdf.setFillColorRGB(0.77, 0.87, 0.97)
        self.pdf.rect(325, 264, 115, 55, fill=True)
        self.pdf.setStrokeColorRGB(0, 0, 0)
        self.pdf.setFillColorRGB(0, 0, 0)
        self.pdf.setFont('abc', 30)
        for i in range(0, 10):
            self.pdf.line(85, self.y, 505, self.y)
            self.y -= 20
        self.pdf.line(325, self.y + 20, 325, 520)
        self.pdf.line(372, self.y + 20, 372, 520)
        self.pdf.line(440, self.y + 20, 440, 520)
        # Texto
        self.pdf.drawString(90, 740, "3C")
        self.pdf.drawString(400, 740, "Factura")
        self.pdf.setFont('abc', 10)
        self.pdf.drawString(90, 705, "Ubicación: Cartago, Costa Rica")
        self.pdf.drawString(90, 685, "Tel: 911")
        self.pdf.drawString(90, 638, "FACTURAR A")
        self.pdf.drawString(90, 575, "506")
        self.pdf.drawString(90, 523, "DESCRIPCIÓN")
        self.pdf.drawString(340, 684, "N°FACTURA")
        self.pdf.drawString(440, 684, "FECHA")
        self.pdf.drawCentredString(365, 638, "VENCE")
        self.pdf.drawString(433, 638, "TÉRMINOS")
        self.pdf.drawCentredString(455, 620, "DAO´s Coorp")
        self.pdf.linkURL("https://tecdigital.tec.ac.cr/dotlrn/file-storage/view/dotlrn_fs_77630404_root_folder/dotlrn_fs_77630404_shared_folder/pagina/index.html", (420, 610, 480, 630), relative=1)
        self.pdf.drawString(333, 523, "CANT.")
        self.pdf.drawString(385, 523, "COSTO U.")
        self.pdf.drawString(450, 523, "TOTAL")
        self.pdf.drawString(333, 308, "SUBTOTAL")
        self.pdf.drawString(333, 290, "I.V.A")
        self.pdf.drawString(333, 272, "TOTAL")
        self.pdf.drawCentredString(300, 225, "Para resolver cualquier duda relacionada a esta factura, póngase en contancto con:")
        self.pdf.drawCentredString(300, 200, "Allan Brito Delgado, 8899-1199, proyecto3DavidsCoorpos@gmail.com")
        self.pdf.setFont("Times-Roman", 10)
        self.pdf.setFillColorRGB(0, 0, 0)
        self.pdf.drawString(150, 309, "Gracias por su confianza")

    #  Escribe las respectivas variables de usuarios y servicios y crea el pdf
    def facturar(self):
        # iNFO DEL CLIENTE
        self.pdf.drawCentredString(365, 667, self.facturas["N°_Factura"])
        self.pdf.drawCentredString(455, 667, self.fecha)  # Fecha
        self.pdf.drawString(90, 620, self.usuario[0])  # Nombre
        self.pdf.drawCentredString(365, 620, self.vence)  # # Vecha de vencimiento
        self.pdf.drawString(90, 605, self.usuario[1])  # Cédula
        self.pdf.drawString(90, 590, self.usuario[2])  # Dirección
        self.pdf.drawString(90, 560, self.usuario[3])  # Correo
        #  Montos
        self.y = 505
        for servicio in self.servicios:
            if self.contador < 10:
                #print(servicio)
                self.pdf.drawString(90, self.y, servicio["tipo"])  # Cual servicio
                self.pdf.drawCentredString(350, self.y, servicio["cant"])  #Cantidad
                self.pdf.drawRightString(437, self.y, self.costo["Servicios"][servicio["ID"]]["costo"])  # Costo Uni.
                self.precio = int(servicio["cant"]) * int(self.costo["Servicios"][servicio["ID"]]["costo"])  # Costo x Cant.
                self.pdf.drawRightString(505, self.y, str(self.precio))
                self.subtotal += self.precio
                self.y -= 20
                self.servicios = self.servicios[1:]
                self.contador += 1
            else:
                break
        self.pdf.drawRightString(505, 308, str(self.subtotal))
        self.precio = self.subtotal * 13 / 100 # i.v.a
        self.pdf.drawRightString(505, 288, str(self.precio))
        self.total = self.subtotal - self.precio # Monto total
        self.pdf.drawRightString(505, 268, str(self.total))
        self.pdf.save()

    #  Guarda los datos importantes de la factura en un archivo aparte para control de facturas
    def guardar_factura(self):
        self.facturas["Facturas"] += [{"N°_Factura": self.facturas["N°_Factura"],  # N° de factura
                                       "Fecha": self.fecha,
                                       "Vencimiento": self.vence,
                                       "Cliente": self.usuario[0],
                                       "Cedula": self.usuario[1],
                                       "Direccion": self.usuario[2],
                                       "Correo": self.usuario[3],
                                       "Servicios": self.guard_servicios,
                                       "Costos": self.costo,  # Costos de los servicios en el momento de efecturar la factura
                                       "Subtotal": self.subtotal,
                                       "Total": self.total
                                       }]
        self.facturas["N°_Factura"] = str(int(self.facturas["N°_Factura"]) + 1)
        info = json.dumps(self.facturas, indent=1)
        with open("Servicios/Facturas.json", "w") as file:
            file.write(info)
            file.close()
        if  self.servicios != []:
            Factura(self.usuario, self.servicios)



class Cambio_Moneda(Factura):

    def __init__(self, precio_dolar, n_factura):
        data = json.load(open("Servicios/Facturas.json"))
        for i in data["Facturas"]:
            if i["N°_Factura"] == n_factura:
                self.facturas = {"N°_Factura": n_factura}
                self.pdf = canvas.Canvas("Servicios/Invoices/" + self.facturas["N°_Factura"] + ".pdf")
                self.costo = i["Costos"]
                self.usuario = [i["Cliente"], i["Cedula"], i["Direccion"], i["Correo"]]
                self.servicios = i["Servicios"]
                #self.guard_servicios = self.servicios[:10]
                self.fecha = i["Fecha"]
                self.vence = i["Vencimiento"]
                self.subtotal = 0
                self.precio = 0
                self.total = 0
                self.y = 500
                self.contador = 0
                break


        self.cambia_costos(precio_dolar)
        self.crear_plantilla()
        self.facturar()


    def cambia_costos(self, precio_dolar):
        for i in self.costo["ID_existentes"]:
            self.costo["Servicios"][i]["costo"] = str(int(self.costo["Servicios"][i]["costo"]) * precio_dolar)

    def sobreescribir_factura(self, n_factura):
        self.facturas = json.load(open("Servicios/Facturas.json"))
        self.facturas["Facturas"] += [{"N°_Factura": self.facturas["N°_Factura"],  # N° de factura
                                       "Fecha": self.fecha,
                                       "Vencimiento": self.vence,
                                       "Cliente": self.usuario[0],
                                       "Cedula": self.usuario[1],
                                       "Direccion": self.usuario[2],
                                       "Correo": self.usuario[3],
                                       "Servicios": self.guard_servicios,
                                       "Costos": self.costo,
                                       # Costos de los servicios en el momento de efecturar la factura
                                       "Subtotal": self.subtotal,
                                       "Total": self.total
                                       }]
        info = json.dumps(self.facturas, indent=1)
        with open("Servicios/Facturas.json", "w") as file:
            file.write(info)
            file.close()

#a = Cambio_Moneda(100, "1")
