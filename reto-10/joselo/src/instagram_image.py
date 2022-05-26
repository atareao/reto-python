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
from typing import Optional


class InstagramImage:
    """InstagramImage."""

    _FILTROS = (
        "_1977", "aden", "brannan", "brooklyn", "clarendon", "earlybird",
        "gingham", "hudson", "inkwell", "kelvin", "lark", "lofi",
        "maven", "mayfair", "moon", "nashville", "perpetua", "reyes",
        "rise", "slumber", "stinson", "toaster", "valencia", "walden",
        "willow", "xpro2")

    def __init__(self, filein: Path, fileout: Path,
                 args: Optional[dict[str, str]] = None) -> None:

        self.__filein = Path(filein)
        self.__fileout = Path(fileout)

        try:
            self.__filter = args['filter']
        except KeyError:
            raise

        if self.__filter not in InstagramImage._FILTROS:
            raise ValueError(
                f"{self.__filter} no está en la lista de filtros.")

    def check(self) -> bool:
        """check."""
        return self.__filein.is_file() \
            and not self.__filein.is_symlink() \
            and not self.__fileout.exists()

    def execute(self) -> None:
        """execute."""
        image = Image.open(self.__filein)
        image = eval(f"pilgram.{self.__filter}(image)")
        image.save(self.__fileout)


def main():  # noqa
    filter_name = "lofi"
    filein = Path("/home/lorenzo/kk/bb.jpg")
    fileout = Path(f"/home/lorenzo/kk/bb_{filter_name}.jpg")
    action = InstagramImage(filein, fileout, {'filter': filter_name})
    if action.check():
        action.execute()


if __name__ == '__main__':
    main()
