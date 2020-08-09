from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import json

class Correo:
    def __init__(self, n_factura):
        self.n_factura = n_factura
        self.su_correo = 'proyecto3DavidsCoorpos@gmail.com'
        self.contraseña = 'ComputadoresJason05'
        self.destinatario = self.Get_Correo()
        self.Enviar()


    # Retorna el correo del usuario
    def Get_Correo(self):
        registro = json.load(open("Servicios/Facturas.json"))
        for factura in registro["Facturas"]:
             if factura["N°_Factura"] == self.n_factura:
                 return factura["Correo"]

    def Enviar(self):
        try:
            asunto = 'Envío de PDF'

            mensaje = MIMEMultipart()
            mensaje['De'] = self.su_correo
            mensaje['Para'] = self.destinatario
            mensaje['Subject'] = asunto

            Contenido_de_Texto = '<><><><><><><><><><><><><><><><><><><><><><><><><><> \n    Por este medio se le facilita su factura, gracias por preferirnos. \n <><><><><><><><><><><><><><><><><><><><><><><><><><>'
            mensaje.attach(MIMEText(Contenido_de_Texto,'plain'))

            nombre_del_archivo="Servicios/Invoices/" + self.n_factura +".pdf"# Aquí pone el nombre de su pdf
            adjunto  =open(nombre_del_archivo,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((adjunto).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+nombre_del_archivo)

            mensaje.attach(part)
            mensaje_completo = mensaje.as_string()
            servidor = smtplib.SMTP('smtp.gmail.com',587)
            servidor.starttls()
            servidor.login(self.su_correo, self.contraseña)


            servidor.sendmail(self.su_correo, self.destinatario, mensaje_completo)
            servidor.quit()
        except:
            print("No se envió")

