#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Reto 08: clase ResizeImage."""

# Copyright (c) 2022 José Lorenzo Nieto Corral <a.k.a. jlnc> <a.k.a. JoseLo>

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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from pathlib import Path
from wand.image import Image


class ResizeImage:
    """ResizeImage."""

    def __init__(self, filein: Path, fileout: Path, args: dict[str, int]) -> None:
        self.__filein = Path(filein)
        self.__fileout = Path(fileout)
        try:
            self.__width = args["width"]
            self.__height = args["height"]
        except KeyError:
            print("No es posible determinar el tamaño de la imágen.")
            raise

    def check(self) -> bool:
        """check."""

        if not self.__filein.is_file():
            raise FileNotFoundError(f"No encuentro el fichero {self.__filein}")

        if os.path.getsize(self.__filein) == 0:
            raise ValueError(f"El fichero {self.__filein} está vacio.")

        im = Image(filename=self.__filein)
        if not im.mimetype.startswith("image"):
            raise ValueError(
                f"El fichero {self.__filein} no parece una imágen.")

        if self.__fileout.is_file():
            raise FileExistsError(f"El fichero {self.__fileout} ya existe.")

        if self.__fileout.is_dir():
            raise ValueError(
                f"El argumento 'fileout' debe ser un fichero, no un directorio.")

        return True

    def execute(self) -> None:
        """execute."""
        im = Image(filename=self.__filein)
        im.resize(self.__width, self.__height)
        im.save(filename=self.__fileout)

    @property
    def size(self):
        return self.__width, self.__height


def main():  # noqa
    filein = Path('/home/lorenzo/kk/bb.png')
    fileout = Path('/home/lorenzo/kk/salida.png')
    args = {"width": 200, "height": 200}
    resize_image = ResizeImage(filein, fileout, args)
    if resize_image.check():
        resize_image.execute()


if __name__ == '__main__':
    main()
