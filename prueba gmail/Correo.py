import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random


class Correo:
    def __init__(self, correo, numeroSesion):
        self.su_correo = 'proyecto3davidscoorpos@gmail.com'
        self.contraseña = 'ComputadoresJason05'
        self.destinatario = correo
        self.asunto = 'Envío de Factura N° '+str(numeroSesion)

        self.EnviarCorreo()
        
    def EnviarCorreo(self):
        mensaje = MIMEMultipart()
        mensaje['De'] = self.su_correo
        mensaje['Para'] = self.destinatario
        mensaje['Subject'] = self.asunto
        nombre_del_archivo='Tarea 8 semana 12 Luis David Delgado Jiménez.pdf'# Aquí pone el nombre de su pdf
        adjunto = open(nombre_del_archivo,'rb')
        Contenido_de_Texto = "Gracias por utilizar el servicio de Davids' & Oscar's coorp. \n <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"
        mensaje.attach(MIMEText(Contenido_de_Texto,'plain'))

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

Correo("lujimenez2000@gmail.com", 5000000+random.randint(1,100000)) # correo y número de facturación aleatorio
