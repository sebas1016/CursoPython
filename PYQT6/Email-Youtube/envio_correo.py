import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv() #Carga las variables de entorno desde el archivo .env

emisor = os.getenv('USER')
receptor = 'sebas16berrio@gmail.com'
asunto = 'test'

msg = MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = emisor
msg['To'] = receptor

with open('PYQT6\Email-Youtube\email.html', 'r',encoding='utf-8' ) as archivo:
    html = archivo.read()

#Adjuntar el contenido HTML
msg.attach(MIMEText(html, 'html'))

#representa una conexión con un servidor de correo saliente (SMTP server)
server = smtplib.SMTP('smtp.gmail.com',587)
#Conexión segura
server.starttls()
server.login(emisor,os.getenv('PASS'))

#eNVIAR CORREO ELECTRONICO
server.sendmail(emisor,receptor,msg.as_string())

server.quit()
