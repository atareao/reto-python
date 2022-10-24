#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created:  5 June 2022

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
from PIL import Image
import magic


class Convert():
    '''
    convert class
    '''
    def __init__(self, dir_path, in_file, out_file):
        '''
        init method
        '''
        self.dir_path = dir_path
        self.in_file = in_file
        self.out_file = out_file
        self.in_file_types = ("image/jpeg",
                              "image/png",
                              "image/bmp")
        self.in_file_type = None
        self.out_file_extensions = (".jpeg",
                                    ".jpg",
                                    ".png",
                                    ".bmp",
                                    ".pdf")
        self.out_file_extension = None

    def check(self):
        '''
        check method
        '''
        if self.in_file == self.out_file:
            print("Nombre fichero base y resultante iguales.")
            return False
        # SE COMPRUEBA SI EXISTE EL FICHERO BASE DE LA CONVERSIÓN
        if Path(f"{self.dir_path}/{self.in_file}"):
            in_file_path = Path(f"{self.dir_path}/{self.in_file}")
            print(f"Fichero base: {in_file_path}")
            self.in_file_type = magic.from_file(f"{in_file_path}", mime=True)
            print(f"Tipo fichero base: {self.in_file_type}")
        else:
            print("El fichero {self.in_file} no existe.")
            return False
        # SE COMPRUEBA SI EL TIPO DE FICHERO BASE ESTÁ EN LA LISTA
        if self.in_file_type in self.in_file_types:
            print("Tipo de fichero base soportado")
        else:
            print("Tipo de fichero base no soportado")
            return False
        # SE COMPRUEBA SI LA EXTENSION DEL FICHERO RESULTANTE ESTÁ EN LA LISTA
        print(f"Fichero resultante: {self.out_file}")
        self.out_file_extension = Path(self.out_file).suffix.lower()
        print(f"Extensión fichero resultante: {self.out_file_extension}")
        if self.out_file_extension in self.out_file_extensions:
            print("Extensión del fichero resultante soportada")
        else:
            print("Extensión del fichero resultante no soportada")
            return False
        # SI NO SE ENCONTRARON ERRORES SE DEVUELVE TRUE
        return True

    def execute(self):
        '''
        execute method
        '''
        img = Image.open(Path(f"{self.dir_path}/{self.in_file}"))
        img.save(Path(f"{self.dir_path}/{self.out_file}"))
