#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Reto 12: clase Copy."""

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
import shutil
from typing import Union


class Copy:
    """Copy."""

    def __init__(self, filein: Union[Path, str],
                   fileout: Union[Path, str]) -> None:
        self.__filein = Path(filein)
        self.__fileout = Path(fileout)

    def check(self) -> bool:
        """check."""
        return self.__filein.is_file() \
            and not self.__filein.is_symlink() \
            and self.__fileout.parent.is_dir() \
            and (self.__fileout.is_dir() or not self.__fileout.exists())

    def execute(self) -> None:
        """execute."""
        shutil.copy(self.__filein, self.__fileout, follow_symlinks=False)


def main():  # noqa
    filein = Path('/home/lorenzo/kk/bb.jpg')
    fileout = Path('/home/lorenzo/kk/bb_copy.jpg')
    action = Copy(filein, fileout)
    if action.check():
        action.execute()


if __name__ == '__main__':
    main()
