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

import os
import toml
import utils


class Configurator:
    """ Clase Configurator de Diogenes app
    Establece acciones y atributos para la configuración de la app
    Diogenes.
    Atributos:
    path: Directorio de archivos de configuración, que se pasen como
    argumento.
    filename: nombre del archivo que se pase como argumento.
    """

    def __init__(self, path, filename):
        """ Constructor de Configurator
        Establece atributos:
        path: Directorio de archivos de configuración, que se pasen como
        argumento.
        filename: nombre del archivo que se pase como argumento.
        Ejecuta también función check()
        """
        self.path = path
        self.filename = filename
        self.check()

    def check(self):
        """ Módulo check de la clase Configurator
        Comprueba que exista el directorio de configuración. Si no existe
        lo crea y también el fichero de configuración, pero vacío, sin
        valores.
        """
        if not self.path.exists():
            os.makedirs(self.path)
        config_file = self.path / self.filename
        if not config_file.exists():
            idata = {'Directorios': {}}
            with open(config_file, 'w') as file_writer:
                toml.dump(idata, file_writer)

    def read(self):
        """ Módulo read de Configurator.
        Lee el fichero de configuración (formato toml) y devuelve el
        contenido en forma de diccionario
        """
        config_file = self.path / self.filename
        return toml.load(config_file)

    def save(self, conf):
        """ Módulo save de Configurator
        Vuelca en el archivo de configuración (formato toml) el
        contenido pasado por argumento.
        """
        config_file = self.path / self.filename
        with open(config_file, 'w') as file_writer:
            toml.dump(conf, file_writer)

    def actions_execute(self):
        """ Módulo actions_execute
        Ejecuta acciones según fichero de configuración para cada uno
        de los directorios
        """
        conf = self.read()
        if len(conf['Directorios']) == 0:
            # print(
            # f"El archivo {config} está vacío. Por favor, incluya ",
            # "algún valor válido")
            pass
        else:
            for dir in conf['Directorios'].values():
                dir_in = dir['in']
                dir_out = dir['out']
                filtro = dir['filter']
                for act in dir['actions']:
                    if act == 'none':
                        # print('No se ejecutará ninguna acción')
                        pass
                    elif act == 'copy':
                        utils.copy_files(dir_in, dir_out, filter_fil=filtro)
                    elif act == 'move':
                        utils.move_files(dir_in, dir_out, filter_fil=filtro)
