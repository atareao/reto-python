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
# CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.

from pathlib import Path
from PIL import Image


class ResizeImage:
    def __init__(self, filein, fileout, args):
        """ Constructor
        """
        self.filein = filein
        self.fileout = fileout
        self.args = args

    def check(self, filein, args):
        """ Función check
        Comprueba:
            - que exista el fichero "filein"
            - que se hayan definido parámetros correctos, que exista anchura
            y altura y sean valores int ¿? ¿Qué pasa si valen 0?
        ** No he sabido cómo acceder a los valores de instancia sin pasarlos
        como argumentos. A revisar **
        """
        if (filein and type(args[('width')]) is int
                and type(args[('height')]) is int):
            return True

    def execute(self, filein, fileout, args):
        """ función execute
        cambia el tamaño de una imagen dada creando una nueva imagen.
        Usa librería Pillow
        Crea una instancia de Image, abriendo el archivo original y
        cargándola en memoria, para poder actuar sobre ella.
        Crea una nueva imagen (memoria) redimensionando la original y
        por último la guarda como imagen destino.
        ** No he sabido cómo acceder a los valores de instancia sin pasarlos
        como argumentos. A revisar **
        """
        with Image.open(filein) as image_origin:
            image_origin.load()
        img_origin_width = args["width"]
        img_origin_height = args["height"]
        image_new = image_origin.resize((img_origin_width, img_origin_height))
        image_new.save(fileout)


def main():
    filein = Path('/home/user/Diogenes_prueba/in/imag.png')
    fileout = Path('/home/user/Diogenes_prueba/in/salida.png')
    args = {"width": 200, "height": 200}
    resize_image = ResizeImage(filein, fileout, args)
    if resize_image.check(filein, args):
        resize_image.execute(filein, fileout, args)


if __name__ == "__main__":
    main()
