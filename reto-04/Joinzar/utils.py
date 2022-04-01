#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Jon Iñaki INCHAURBE ZARATE (joinzar@gmail.com)
#
# [Official text in English]
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software 
#is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software. 
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE. 
#
# [Traducción no oficial en español]
# Por la presente se concede permiso, libre de cargos, a cualquier persona que 
# obtenga una copia de este software y de los archivos de documentación 
# asociados (el "Software"), a utilizar el Software sin restricción, 
# incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, 
# publicar, distribuir, sublicenciar, y/o vender copias del Software, y a 
# permitir a las personas a las que se les proporcione el Software a hacer lo 
# mismo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas 
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "COMO ESTA", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA 
# O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, 
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS 
# AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE 
# NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN 
# DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN 
# CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE. 

#############################################################################
#  módulos para usar en proyecto reto python de ateeao.es                   #
#  https://atareao.es/tutorial/reto-python/reto-python-4-un-reto-con-clase/ #
#############################################################################


import mimetypes
import os
import re # debe ser para expresiones regulares

def crear_fichero(directorio, fichero, conf_default):
    """
    Crea un fichero toml y lo dota de contenido.
    Argumentos:
    - directorio: en el que se va a crear_fichero
    - fichero: nombre de fichero a crear_fichero
    - conf_default: contenido por defecto que escribe
    """
    fichero_crear = open(f"{directorio}/{fichero}", "w")
    fichero_crear.write(f'directorio = "{conf_default}"')
    fichero_crear.close()

def list_images(directorio):
    """ Reto 2 de Python: Se trata de listar sólo los JPEG de la carpeta  
    downloadas. Además, los pares deben llevar  por delante una flecha =>; 
    yo he decidido poner también el número de línea.
    Además, si el nombre tiene números se debe mostrar en mayúsculas; si no 
    tiene, en minúsculas
    """
    print(f"\nDirectorio: {directorio} \n")
    contador = 1  # Lo usaremos para saber si es par o impar
    ficheros = os.listdir(directorio)  # carga en ficheros los nombres de los 
    # ficheros del directorio
    for elemento in ficheros:
        if os.path.isfile(os.path.join(directorio, elemento)) and \
mimetypes.guess_type(elemento)[0] == 'image/jpeg':
            x = re.findall('[0-9]+', elemento)  # Miranmos si nombre tiene      
                # números
            if len(x) >= 1:  # Si se encuentra, el número extraído tendrá  
                #longitud mínima de 1 carácter
                elemento = elemento.upper()  # convierte texto a mayúsculas
            else:
                elemento = elemento.lower()
            if contador % 2 == 0:
                print(f"{contador}=> {elemento}")
                contador += 1
            else:
                print(f"{contador}   {elemento}")
                contador += 1
