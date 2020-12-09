"""
|------------------------------------|
|  Generación de hashes de ficheros  |
|------------------------------------|
"""

# Importamos los módulos
import argparse
import os
import hashlib
import sys
from prettytable import PrettyTable


def hash(filePath, hashAlgorithm):

    tableFormat = PrettyTable()
    tableFormat.field_names = ["FILE", "HASH"]

    def blake2b(fl: str):
        hashing = hashlib.blake2b(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def blake2s(fl: str):
        hashing = hashlib.blake2s(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def md5(fl: str):
        hashing = hashlib.md5(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha1(fl: str):
        hashing = hashlib.sha1(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha224(fl: str):
        hashing = hashlib.sha224(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha256(fl: str):
        hashing = hashlib.sha256(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha3_224(fl: str):
        hashing = hashlib.sha3_224(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha3_256(fl: str):
        hashing = hashlib.sha3_256(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha3_384(fl: str):
        hashing = hashlib.sha3_384(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha3_512(fl: str):
        hashing = hashlib.sha3_512(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def sha512(fl: str):
        hashing = hashlib.sha512(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def shake_128(fl: str):
        hashing = hashlib.shake_128(bytes(fl, "utf-8")).hexdigest()
        return hashing

    def shake_256(fl: str):
        hashing = hashlib.shake_256(bytes(fl, "utf-8")).hexdigest()
        return hashing

    switch_case = {
        1: blake2b,
        2: blake2s,
        3: md5,
        4: sha1,
        5: sha224,
        6: sha256,
        7: sha3_224,
        8: sha3_256,
        9: sha3_384,
        10: sha3_512,
        11: sha512,
        12: shake_128,
        13: shake_256
    }
    

    def switch(numberGivenToHash,file):
        return switch_case.get(numberGivenToHash)(file)

    with open("Hash_files.txt", "a") as archive:
        if os.path.exists(filePath) == True:			
            if os.path.isdir(filePath) == True:
                if hashAlgorithm == "BLAKE2B":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(1, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "BLAKE2S":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(2, file)
                        tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "MD5":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(3, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA1":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(4, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA224":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(5, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(6, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_224":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(7, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(8, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_384":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(9, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_512":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(10, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA512":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(11, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHAKE_128":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(12, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHAKE_256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    for file in os.listdir(filePath):
                        parsedCommand = switch(13, file)
                        tableFormat.add_row([file, parsedCommand])
                    archive.write(str(tableFormat))
                else:
                    raise Exception("Algoritmo indicado erróneo")
                    
                    
            elif os.path.isfile(filePath) == True:
                if hashAlgorithm == "BLAKE2B":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(1,filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "BLAKE2S":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(2, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "MD5":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(3, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA1":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(4, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA224":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(5, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(6, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_224":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(7, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(8, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_384":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(9, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA3_512":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(10, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHA512":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(11, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHAKE_128":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(12, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))
                elif hashAlgorithm == "SHAKE_256":
                    archive.write('\nAlgorithm: ' + hashAlgorithm + '\n')
                    parsedCommand = switch(13, filePath)
                    tableFormat.add_row([filePath, parsedCommand])
                    archive.write(str(tableFormat))

                    
                else:
                    raise Exception("||| Algoritmo indicado erróneo |||")
                    
            else:
                raise Exception("||| Dirección no válida |||")
                
        else:
            raise Exception("||| Dirección no válida |||")