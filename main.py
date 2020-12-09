"""
|------------------------------------|
|           Codigo __main__          |
|------------------------------------|
"""

import VIRUSTOTAL
import HASH
import CORREOS
import BANNER
import excepciones
import argparse
import sys
import os
import json
from prettytable import PrettyTable
from rich import print
import subprocess

#Importacion de los modulos requeridos para la ejecucion del codigo


logging_table = PrettyTable()    #Creamos el objeto PrettyTable
logging_table.field_names = ["Date", "Type Error", "Error Description"]


file = open("Error_logging.txt","a") #Cargamos en memoria el archivo del registro de 
                                   #errores en modo append

def cmd(comando):
    subprocess.run(comando, shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-links', dest='link_fp', help="Ruta a los links que quieres escanear", required=False)
    parser.add_argument('-output', dest='output_fp', help="Ruta a tu archivo de salida", required=False)
    parser.add_argument('-response', dest='response_fp', help='Ruta al archivo de respuesta que quieres guardar', required=False)
    parser.add_argument('-api_key', dest='api_key', help='Llave API de virus total', required=False)
    parser.add_argument("-path", dest="path", help="Ruta al archivo o directorio del que se desea el hash", required=False)
    parser.add_argument("-hsh", dest="hashAlg", help="Algoritmo en el que se desea hashear", required=False)#, default=argparse.SUPPRESS)
    parser.add_argument('-target', dest='target', help='Target IP / Dominio',required=False)
    parser.add_argument('-port', dest='port', help='numero de puerto',type=int,default=80)
    parser.add_argument('-busqueda', dest='busqueda', help='Palabra clave para la busqueda',required=False)
    parser.add_argument('-num', dest='num', help='Numero de busquedas',type=int,required=False)
    parser.add_argument('-encryptiontype', dest='encryptiontype', help='"e" para encriptar, "d" para desencriptar',required=False)
    parser.add_argument('-server', dest='server', help='Sitio donde iniciar sesion',required=False)
    parser.add_argument('-usr', dest='user', help='Usuario del remitente del mensaje',required=False)
    parser.add_argument('-pass', dest='password', help='Contrasenia de la cuenta del remitente',required=False)
    parser.add_argument('-subj', dest='subject', help='Asunto del correo',required=False)
    parser.add_argument('-body', dest='body', help='Cuerpo del mensaje',required=False)
    parser.add_argument('-file', dest='file', help='Archivo/Imagen a adjuntar',required=False)
    parser.add_argument('-add', dest='addressee', help='Destinatario del mensaje',required=False)
    parser.add_argument('-key', dest='key', help='Llave de encriptacion (1 al 26)',type=int,required=False)
    parser.add_argument('-msg', dest='msg', help='Mensaje a encriptar, DEBE ir en comillas',required=False)


    args = sys.argv[1:]


    i = 1

    try:

        while i == 1:
            
            # Funcion HASH
            if ("-path" in args) and ("-hsh" in args):	#Ejemplo de ejecucion
                params = parser.parse_args()		# python main.py -path C:\Users\eduar\Desktop\example.py -hsh SHA256
                filePath = params.path				# Los argumentos de -hsh pueden ser: 
                hashAlgorithm = params.hashAlg		# BLAKE2B, BLAKE2S, MD5, SHA1, SHA224, SHA256, SHA3_224, SHA3_256, 
                HASH.hash(filePath, hashAlgorithm)	# SHA3_384, SHA3_512, SHA512, SHAKE_128, SHAKE_256
                i = 0
            
            # ENVIO DE CORREOS
            # Envio de Correo (Texto y Archivo)
            if ('-server' in args) and ('-usr' in args) and ('-pass' in args) and ('-subj' in args) and ('-body' in args) and ('-file' in args) and ('-add' in args):
                params = parser.parse_args()

                # Iniciamos los parámetros del script
                data = {
                    'server':params.server,
                    'user': params.user,
                    'pass': params.password,
                    'subject':params.subject,
                    'body':params.body,
                    'file':params.file,
                    'addressee': params.addressee
                }

                serv = data['server']
                usr = data['user']
                passw = data['pass']
                subject = data['subject']
                body = data['body']
                filed = data['file']
                add = data['addressee']

                # Se crea el archivo de configuracion
                with open('pass.json', 'w') as file:
                    json.dump(data, file, indent=4)

                data = {}
                with open('pass.json') as file:
                    data = json.load(file)

                CORREOS.File_and_Text(serv,usr,passw,subject,body,filed,add)
                i = 0

            # CASO GMAIL
            # main.py -server gmail -usr example@gmail.com -pass password 
            # 				  -subj Subject -body Python -file file.* -add example@example.com

            # CASO OFFICE365
            # python3 main.py -server office365 -usr example@uanl.edu.mx -pass password 
            # 				  -subj Subject -body Python -file file.* -add example@example.com

            # Envio de Correo (Solo Archivo o Imagen)
            if ('-server' in args) and ('-usr' in args) and ('-pass' in args) and ('-subj' in args) and ('-file' in args) and ('-add' in args):
                params = parser.parse_args()

                # Iniciamos los parámetros del script
                data = {
                    'server':params.server,
                    'user': params.user,
                    'pass': params.password,
                    'subject':params.subject,
                    'body':params.body,
                    'file':params.file,
                    'addressee': params.addressee
                }

                serv = data['server']
                usr = data['user']
                passw = data['pass']
                subject = data['subject']
                body = data['body']
                filed = data['file']
                add = data['addressee']

                # Se crea el archivo de configuracion
                with open('pass.json', 'w') as file:
                    json.dump(data, file, indent=4)

                data = {}
                with open('pass.json') as file:
                    data = json.load(file)
        
                CORREOS.File(serv,usr,passw,subject,filed,add)
                i = 0

            #Ejemplo de ejecucion

            # Caso GMAIL
            # Envio de Correo (Solo Texto en un .txt o escrito desde Argumento "sinespacios")
            # main.py -server gmail -usr example@gmail.com -pass password -subj Subject
            # -file file.* -add example@example.com

            # CASO OFFICE365
            # main.py -server office365 -usr example@uanl.edu.mx -pass password -subj Subject
            #                 -file file.* -add example@example.com

            # Envio de Correo (Solo Texto en un archivo.txt o escrito desde Argumento "sinespacios")
            if ('-server' in args) and ('-usr' in args) and ('-pass' in args) and ('-subj' in args) and ('-body' in args) and ('-add' in args):
                params = parser.parse_args()

                # Iniciamos los parámetros del script
                data = {
                    'server':params.server,
                    'user': params.user,
                    'pass': params.password,
                    'subject':params.subject,
                    'body':params.body,
                    'file':params.file,
                    'addressee': params.addressee
                }

                serv = data['server']
                usr = data['user']
                passw = data['pass']
                subject = data['subject']
                body = data['body']
                filed = data['file']
                add = data['addressee']

                # Se crea el archivo de configuracion
                with open('pass.json', 'w') as file:
                    json.dump(data, file, indent=4)

                data = {}
                with open('pass.json') as file:
                    data = json.load(file)

                CORREOS.Text(serv,usr,passw,subject,body,add)
                i = 0

            #Ejemplo de ejecucion

            # Caso GMAIL
            
            # main.py -server gmail -usr example@gmail.com -pass password -subj Subject
            #                 -body Python -add example@example.com

            # CASO OFFICE365
            #  main.py -server office365 -usr example@uanl.edu.mx -pass password -subj Subject
            #                 -body Python -add example@example.com

            # VIRUSTOTAL
            if ("-links" in args) and ("-output" in args) and ("-response" in args) and ("-api_key" in args):
                params = parser.parse_args()
                linkFiles = params.link_fp
                outputFile = params.output_fp
                responseFile = params.response_fp
                API_KEY = params.api_key
                VIRUSTOTAL.virus_total(linkFiles, outputFile, responseFile, API_KEY)
                i = 0

            #BANNER DE SERVIDOR
            if ('-target' in args) or ('-port' in args):                # Ejemplo de ejecucion
                params = parser.parse_args()				# python main.py -target www.uanl.mx
                target = params.target			# El puerto puede ser especificado, en caso de no serlo, se le asigna
                port = params.port				# un valor por default
                BANNER.Get_Banner(target,port)
                i = 0

            #CIFRADO DE MENSAJES
            if ("-encryptiontype" in args) and ("-key" in args) and ("-msg" in args):
                params = parser.parse_args()								# Ejemplo de ejecucion
                encryption = params.encryptiontype		# python main.py -encryptiontype e -key 12 -msg "Hola como estas"
                message = params.msg				# Puede ser "e" para encriptar o "d" para desencriptar
                llave = params.key					# Puede ser del 1 al 26 y debe ser la misma en ambas ("e" y "d")
                comando = 'Powershell .\cifrado.ps1 -encryptiontype ' + encryption + ' -key ' + str(llave) + ' -msg ' + "'" + message + "'"
                cmd(comando)		# Se envia en mensaje cifrado o no cifrado
                i = 0

            if ("-h" in args) or ("--help" in args):
               params = parser.parse_args()

            if i == 1:
                raise Exception("Argumentos Erroneos")                    


    except Exception as e:
       excepciones.error_Logging(e, logging_table)
       print(f"[bold red]{e}[/bold red]")
       file.write("\n" + str(logging_table))
       file.close()


if __name__ == '__main__':
    main = main()