#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>

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


class GreyscaleImage:
    def __init__(self, filein, fileout, args={}):
        self.__filein = filein
        self.__fileout = fileout

    def check(self):
        if not self.__filein.exists() or not self.__filein.is_file():
            return False
        if not self.__fileout.parent.exists() or \
                not self.__fileout.parent.is_dir():
            return False
        return True

    def execute(self):
        image = Image.open(self.__filein)
        greyscale_image = image.convert('L')
        greyscale_image.save(self.__fileout)


def main():
    filein = Path('/home/lorenzo/kk/bb.png')
    fileout = Path('/home/lorenzo/kk/bb_grayscale.png')
    action = GreyscaleImage(filein, fileout)
    if action.check():
        action.execute()


if __name__ == "__main__":
    main()
