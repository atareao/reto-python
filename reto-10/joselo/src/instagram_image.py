#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Reto 10: clase InstagramImage."""

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

from pathlib import Path
from PIL import Image
import pilgram


class InstagramImage:
    """InstagramImage."""

    # pilgram.__all__[0] es '__version__'
    _FILTROS: list[str] = pilgram.__all__[1:]

    def __init__(self, filein: Path, fileout: Path,
                 args: dict[str, str]) -> None:

        self.__filein = Path(filein)
        self.__fileout = Path(fileout)
        self.__filter = None
        filtro = args['filter'] if 'filter' in args else None
        if filtro in self._FILTROS:
            self.__filter = eval(f"pilgram.{filtro}")

    # Por conveniencia, para que la función test pueda ejecutar todos los
    # filtros, uno detrás de otro.
    @classmethod
    def filtros(cls) -> list:
        """Acceso a InstagramImage._FILTROS desde objetos externos."""
        return cls._FILTROS

    def check(self) -> bool:
        """check."""
        return self.__filter is not None \
            and self.__filein.is_file() \
            and not self.__filein.is_symlink() \
            and self.__fileout.parent.is_dir() \
            and not self.__fileout.exists()

    def execute(self) -> None:
        """execute."""
        try:
            image = Image.open(self.__filein)
            image = self.__filter(image)
            image.save(self.__fileout)
        except Exception:
            pass


def main():  # noqa
    filter_name = "lofi"
    filein = Path("/home/lorenzo/kk/bb.jpg")
    fileout = Path(f"/home/lorenzo/kk/bb_{filter_name}.jpg")
    action = InstagramImage(filein, fileout, {'filter': filter_name})
    if action.check():
        action.execute()


def test():  # noqa
    filein = Path("/home/lorenzo/kk/bb.jpg")
    for filter_name in InstagramImage.filtros():
        fileout = Path(f"/home/lorenzo/kk/bb_{filter_name}.jpg")
        action = InstagramImage(filein, fileout, {'filter': filter_name})
        if action.check():
            print(filter_name)
            action.execute()


if __name__ == '__main__':
    main()
    # test()
