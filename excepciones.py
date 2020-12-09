"""
|------------------------------------|
|        Manejo de excepciones       |
|------------------------------------|
"""
import time 
from time import strftime, localtime

def error_Logging(e: Exception, logging_table): #Funcion que recibe de argumentos la excepcion a manejar
											  # y el objeto PrettyTable
	logging_table.add_row([strftime("%H:%M:%S, %a %d %b %Y", localtime()), str(type(e)), str(e)])
	#Agrega al registro de errores la excepcion


