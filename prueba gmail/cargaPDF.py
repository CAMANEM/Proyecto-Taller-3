import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys

su_correo = 'proyecto3davidscoorpos@gmail.com'
contraseña = 'ComputadoresJason05'
destinatario = 'Lujimenez2000@gmail.com'

asunto = 'Envío de PDF' 

mensaje = MIMEMultipart()
mensaje['De'] = su_correo
mensaje['Para'] = destinatario
mensaje['Subject'] = asunto

Contenido_de_Texto = 'Frase del día: más vale tarde que nunca... \n <><><><><><><><><><><><><><><><>'
mensaje.attach(MIMEText(Contenido_de_Texto,'plain'))

nombre_del_archivo='git.pdf'# Aquí pone el nombre de su pdf
adjunto  = open(nombre_del_archivo,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((adjunto).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+nombre_del_archivo)

mensaje.attach(part)
mensaje_completo = mensaje.as_string()
servidor = smtplib.SMTP('smtp.gmail.com',535)
servidor.starttls()
servidor.login(su_correo, contraseña)

try:
    servidor.sendmail(su_correo, destinatario, mensaje_completo)
    print("sent")
except:
    print("Unexpected error")
servidor.quit()
