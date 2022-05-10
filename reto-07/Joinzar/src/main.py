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
# CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE

#############################################################################
# Se comentan los mensajes ya que parece que por ahora no se quiere imprimir#
# o bien se dejan para una fase posterior, quizás haciéndolo multilingüe    #
#############################################################################

from pathlib import Path
from xdg import xdg_config_home
from configurator import Configurator
import utils


def step1(path, config):
    """ Función step1
    Crea una instancia? de la clase Configurator
    """
    Configurator(path, config)


def step2(path, config):
    """ Función step2. Listar imagenes
    Lista las imágenes que pueda haber en cada directorio
    """
    conf = Configurator(path, config).read()
    # Controlar que exista contenido, pues crea archivo nuevo vacío
    if len(conf['Directorios']) == 0:
        print(
            f"El archivo {config} está vacío. Por favor, incluya ",
            "algún valor válido")
    else:
        for dir in conf['Directorios'].values():
            print('=====', dir['in'], '=====')
            utils.list_images(Path(dir['in']))


def step3(path, config):
    """ Función step3
    Lee el contenido del archivo de configuración usando módulo read
    de la clase Configurator y da el valor a la variable conf.
    Sobre ello, ejecuta el módulo actions_execute de Configurator
    """
    conf = Configurator(path, config)
    conf.actions_execute()


def main(app, config):
    path = Path(xdg_config_home()) / app
    step1(path, config)
    step2(path, config)
    step3(path, config)


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
