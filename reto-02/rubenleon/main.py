#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import re


def checkStringNumeros(texto):
    
    numeros = re.findall('[0-9]+', texto)
    if(len(numeros)) == 0:
        texto = texto.upper() 
    else:
        texto = texto.lower() 
    return texto

carpetas = ("Downloaders","Descargas") #Posibles formas de llamar el directorio descargas

path = f"/home/{os.getlogin()}"
for indice,carpeta in enumerate(carpetas):
    if(os.path.exists(path+"/"+carpeta)):
        path = path+"/"+carpeta
    elif(len(carpetas)==indice+1): 
        print("Error: No existe la carpeta de Descargas")
        exit(1)
        

print(f"Descargas: {path} \n")

for indice,item in enumerate(os.listdir(path)):
    if os.path.isfile(path+"/"+item):
        if(item.endswith(".jpg")):
            #indice+=1
            item = checkStringNumeros(item)
            if(indice % 2 == 0):
                print(" => " + item)
            else:
                print(item)



