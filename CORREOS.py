import smtplib, email, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
import re
import os
import sys
import excepciones


def Valid_File(filed):
	patron = '[.txt]$'
	return bool(re.search(patron,filed))

# Envio de Correo (Texto y Archivo)
def File_and_Text(serv,usr,passw,subject,body,filed,add):
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()

    # Establecemos los atributos del mensaje
    mensaje['From'] = usr
    mensaje['To'] = add
    mensaje['Subject'] = subject

    try:
        if Valid_File(body) == True:
            with open(body, 'r+') as file:
                file.seek(0)
                message = file.read()
                # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
                mensaje.attach(MIMEText(message, 'plain'))
            try:
                if os.path.exists(filed) == True:
                    with open(filed, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename= {filed}"
                        )
                        mensaje.attach(part)
                        context = ssl.create_default_context()
                    try:
                        # Creamos la conexión con el servidor
                        if serv.lower() == 'gmail':
                            with smtplib.SMTP_SSL('smtp.'+serv+'.com', 465, context=context) as server:
                                # Iniciamos sesión en el servidor
                                server.login(usr, passw)
                                # Convertimos el objeto mensaje a texto
                                text = mensaje.as_string()
                                # Enviamos el mensaje
                                server.sendmail(usr, add, text)
                                print("Successfully sent email to %s" % (mensaje['To']))
                        elif serv.lower() == 'office365':
                            context = ssl.create_default_context()
                            with smtplib.SMTP('smtp.'+serv+'.com', 587) as server:
                                server.ehlo()
                                server.starttls(context=context)
                                server.login(usr, passw)
                                text = mensaje.as_string()
                                server.sendmail(usr, add, text)
                                print("Successfully sent email to %s" % (mensaje['To']))
                    except:
                        raise
            except:
                raise
        # Si no es Archivo .txt, tomará la cadena 'sinespacios' que el usr introduzca en -body
        else:
            message = body
            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(message, 'plain'))
            with open(filed, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filed}"
                )
                mensaje.attach(part)
                context = ssl.create_default_context()
            try:
                # Creamos la conexión con el servidor
                if serv.lower() == 'gmail':
                    with smtplib.SMTP_SSL('smtp.'+serv+'.com', 465, context=context) as server:
                        # Iniciamos sesión en el servidor
                        server.login(usr, passw)
                        # Convertimos el objeto mensaje a texto
                        text = mensaje.as_string()
                        # Enviamos el mensaje
                        server.sendmail(usr, add, text)
                        print("Successfully sent email to %s" % (mensaje['To']))
                elif serv.lower() == 'office365':
                    context = ssl.create_default_context()
                    with smtplib.SMTP('smtp.'+serv+'.com', 587) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(usr, passw)
                        text = mensaje.as_string()
                        server.sendmail(usr, add, text)
                        print("Successfully sent email to %s" % (mensaje['To']))
            except:
                raise   
    except:
        raise

# Envio de Correo (Solo Archivo o Imagen)
def File(serv,usr,passw,subject,filed,add):
	# Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = usr
    mensaje['To'] = add
    mensaje['Subject'] = subject

    try:
        if os.path.exists(filed) == True:
            with open(filed, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filed}"
                )
                mensaje.attach(part)
                context = ssl.create_default_context()
            try:
                # Creamos la conexión con el servidor
                if serv.lower() == 'gmail':
                    with smtplib.SMTP_SSL('smtp.'+serv+'.com', 465, context=context) as server:
                        # Iniciamos sesión en el servidor
                        server.login(usr, passw)
                        # Convertimos el objeto mensaje a texto
                        text = mensaje.as_string()
                        # Enviamos el mensaje
                        server.sendmail(usr, add, text)
                        print("Successfully sent email to %s" % (mensaje['To']))
                elif serv.lower() == 'office365':
                    context = ssl.create_default_context()
                    with smtplib.SMTP('smtp.'+serv+'.com', 587) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(usr, passw)
                        text = mensaje.as_string()
                        server.sendmail(usr, add, text)
                        print("Successfully sent email to %s" % (mensaje['To']))
            except:
                raise
    except:
        raise


# Envio de Correo (Solo Texto .txt o escrito desde Argumento "sinespacios")
def Text(serv,usr,passw,subject,body,add):
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = usr
    mensaje['To'] = add
    mensaje['Subject'] = subject

    if Valid_File(body) == True:
            with open(body, 'r+') as file:
                file.seek(0)
                message = file.read()
                # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
                mensaje.attach(MIMEText(message, 'plain'))
                context = ssl.create_default_context()
    else: 
        message = body
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(message, 'plain'))
        context = ssl.create_default_context()
    try:
        # Creamos la conexión con el servidor
        if serv.lower() == 'gmail':
            with smtplib.SMTP_SSL('smtp.'+serv+'.com', 465, context=context) as server:
                # Iniciamos sesión en el servidor
                server.login(usr, passw)
                # Convertimos el objeto mensaje a texto
                text = mensaje.as_string()
                # Enviamos el mensaje
                server.sendmail(usr, add, text)
                print("Successfully sent email to %s" % (mensaje['To']))
        elif serv.lower() == 'office365':
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.'+serv+'.com', 587) as server:
                server.ehlo()
                server.starttls(context=context)
                server.login(usr, passw)
                text = mensaje.as_string()
                server.sendmail(usr, add, text)
                print("Successfully sent email to %s" % (mensaje['To']))
    except:
        raise