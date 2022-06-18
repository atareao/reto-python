#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 18 June 2022

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
import shutil


class Copy():
    '''
    Copy class
    '''
    def __init__(self, orig_file, dest_file):
        '''
        (path, path) -> None
        Inicializa la clase Copy
        '''
        self.orig_file = orig_file
        self.dest_file = dest_file

    def check(self):
        '''
        (None) -> bool
        Comprueba que el fichero origen existe.
        Devuelve:
        True si el fichero existe.
        False en caso contrario.
        '''
        print("Copy check()")
        if Path(self.orig_file).exists():
            if not Path(self.dest_file).parent.exists():
                print("El directorio destino no existe." +
                      "Se cancela la operación")
                return False
            if Path(self.dest_file).exists():
                print("El archivo destino existe. Se cancela la operación.")
                return False
        print("Sin errores.")
        return True

    def execute(self):
        '''
        (None) -> bool
        Ejecuta la operación de copia.
        Devuelve:
        True si la operación se realizó con éxito.
        False en caso contrario.
        '''
        print("Copy execute():")
        try:
            print(f"Copiando {self.orig_file} a {self.dest_file}")
            shutil.copy(self.orig_file, self.dest_file)
            print("Sin errores.")
            return True
        except:
            print("Se produjeron errores.")
            return False


class Remove():
    '''
    Remove class
    '''
    def __init__(self, file_name):
        '''
        (path) -> None
        Inicializa la clase Remove
        '''
        self.file_name = file_name

    def check(self):
        '''
        (None) -> bool
        Comprueba que el fichero existe.
        Devuelve:
        True si el fichero existe.
        False en caso contrario.
        '''
        print("Remove check():")
        if Path(self.file_name).exists():
            print("Sin errores.")
            return True
        print(f"{file_name} no existe.")
        return False

    def execute(self):
        '''
        (None) -> bool
        Ejecuta la operación de borrado.
        Devuelve:
        True si la operación se realizó con éxito.
        False en caso contrario.
        '''
        print("Remove execute():")
        try:
            print(f"Removing {self.file_name}")
            Path(self.file_name).unlink()
            print("Sin errores.")
            return True
        except:
            print("Se produjeron errores.")
            return False
