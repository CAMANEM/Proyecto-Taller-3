from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["From"]="asd@yopmail.com"
mensaje["To"]= "lujimenez2000@gmail.com"
mensaje["Subject"] ="Correo de prueba desde Python 3"
adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("hola.txt","rb").read())
adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.gmail.com:535")
smtp.starttls()
smtp.login("proyecto3DavidsCoorpos@gmail.com","ComputadoresJason05")
smtp.sendmail("proyecto3DavidsCoorpos@gmail.com","lujimenez2000@gmail.com",mensaje.as_string())
smtp.quit()
