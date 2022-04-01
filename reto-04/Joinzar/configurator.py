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
# Creado para reto Python 4                                                 #
# https://atareao.es/tutorial/reto-python/reto-python-4-un-reto-con-clase/  #
#############################################################################


from gi.repository import GLib  
import os
from pathlib import Path
import toml

from utils import crear_fichero


class Configurator():
    """
    Esta clase tiene como funciones:
    - leer un archivo dado en un directorio dado
    - Si no existe el directorio dado, lo crea (y también el archivo).
    - Si existe el directorio pero no el archivo, lo crea.
    - Al fichero se le metería un contenido determinado 
    """


    def __init__(self, directorio, fichero):
        """
        Comprueba si existen directorio y/o fichero y si no, los crea.
        El contenido del fichero, en el reto será /home/user/download,
        porque no se da opción a otra cosa. En mi opinión, si queremos una
        clase general, debiera pasarse contenido por parámetro o fichero 
        o solicitar por input.
        """
        self.directorio = directorio
        self.fichero = fichero
        # Miramos si existe directorio y/o fichero y si no, se crean
        if os.path.isdir(self.directorio) == False: # No existe directorio
            print("No encuentro el directorio, pero creo directorio y fichero")
            os.makedirs(self.directorio, exist_ok=True)
            conf_default = \
Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
            crear_fichero(directorio, fichero, conf_default)
        else: 
            print("Sí existe el directorio") 
            if os.path.isfile(f"{self.directorio}/{self.fichero}") == False:
                print("No veo el fichero, pero lo creo ahora")
                conf_default = \
Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
                crear_fichero(directorio, fichero, conf_default)
            else: print("Ya veo el fichero y existe, tranki")


    def read(self):
 # comento mi solución inicial porque el main del reto busca el diccionario
#        datos = toml.load(f"{self.fichero}")
#        resultado = datos['directorio']
        resultado = toml.load(f"{self.directorio}/{self.fichero}")
        return resultado
