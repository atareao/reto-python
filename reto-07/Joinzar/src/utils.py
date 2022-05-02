#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################################
# Modificado a partir de un fichero escrito por:                            #
# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>                     #
#############################################################################

# Copyright (c) 2022 Jon Iñaki INCHAURBE ZARATE (joinzar@gmail.com)
#
# [Official text in English]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
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
# Se comentan los mensajes ya que parece que por ahora no se quiere imprimir#
# bien se dejan para una fase posterior, quizás haciéndolo multilingüe      #
#############################################################################

import os
import mimetypes
import shutil

mimetypes.init()


def list_images(directory):
    """ Función listar imágenes de un directorio dado (argumento)

    La función es listar imágenes de un directorio dado.
    Si el directorio no existe, se debe crear.
    Pero se debe revisar si está vacío antes de listar o iterar porque si no,
    no lista nada y es mosqueante

    """
    if not directory.exists():
        os.makedirs(directory)
        # print(f"Se ha creado el directorio {directory}")
    if len(os.listdir(directory)) == 0:
        # print('El directorio está vacío')
        pass
    else:
        contador = 0
        images = ('image/jpeg', 'image/png', 'image/svg+xml',
                  'image/tiff')
        for afile in directory.iterdir():
            if (afile.is_file() and
                    mimetypes.guess_type(afile)[0] in images):
                print(afile.name)
                contador += 1
        if contador == 0:
            # print('No hay imágenes para listar')
            pass


def copy_files(directory_in, directory_out, filter_fil="filtro"):
    """ Función copiar archivos desde directory_in a directory_out
    Copiará los archivos que respondan al filtro dado.
    Se comprueba que los directorios existan. Si in no existe, imprime
    aviso y cesa. Si out no existe, se crea.
    Para cada archivo, debe comprobar que no exista un archivo con el
    mismo nombre en out y si no existe, copiarlo.
    Meto un mensaje de confirmación (verbose).
    """
    if os.path.exists(directory_in):
        if not os.path.exists(directory_out):
            os.makedirs(directory_out)
        ficheros_in = os.listdir(directory_in)
        ficheros_out = os.listdir(directory_out)
        for afile in ficheros_in:
            """ Trabajo en la hipótesis de que los filtros sólo pueden ser
            o bien *.extension o *.*, esto es, cualquiera"""
            if ((filter_fil.partition('.')[-2] +
                    filter_fil.partition('.')[-1]) in afile
                    or filter_fil == '*.*'):
                if afile not in ficheros_out:
                    shutil.copy(directory_in + '/' + afile, directory_out)
                else:
                    # print(f"{afile} ya existe, no se copiará")
                    pass
    else:
        # print(f"{directory_in} no existe. Nada para copiar")
        pass


def move_files(directory_in, directory_out, filter_fil="filtro"):
    """ Función mover archivos desde directory_in a directory_out
    Asumo que la función es mover todos los archivos que existan en el
    directorio_in al out que respondan al filtro dado y que el escenario
    es que existan sólo archivos, ya que si existieran directorios,
    el escenario cambia.
    Se comprueba que los directorios existan. Si in no existe, levantaría
    error y cesa. Si out no existe, se crea.
    Según instrucciones, se deben mover los archivos de in a out,
    pero si existen en destino, se deben borrar antes. ¿Cuáles?
    Entiendo que para cada archivo.
    Meto un mensaje de confirmación (verbose)
    """
    if os.path.exists(directory_in):
        if not os.path.exists(directory_out):
            os.makedirs(directory_out)
        ficheros_in = os.listdir(directory_in)
        ficheros_out = os.listdir(directory_out)
        for afile in ficheros_in:
            """ Trabajo en la hipótesis de que los filtros sólo pueden ser
            o bien *.extension o *.*, esto es, cualquiera"""
            if ((filter_fil.partition('.')[-2] +
                    filter_fil.partition('.')[-1]) in afile
                    or filter_fil == '*.*'):
                if afile not in ficheros_out:
                    shutil.move(directory_in + '/' + afile, directory_out)
                else:
                    os.remove(directory_out + '/' + afile)
                    shutil.move(directory_in + '/' + afile, directory_out)
    else:
        # print(f"{directory_in} no existe. Nada para copiar")
        pass
