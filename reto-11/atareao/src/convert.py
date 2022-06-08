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
import mimetypes
from PIL import Image


ALLOWED_FROM = ["image/jpeg", "image/png", "image/bmp"]
ALLOWED_TO = ["image/jpeg", "image/png", "image/bmp", "application/pdf"]

mimetypes.init()


class Convert:
    def __init__(self, filein, fileout, args={}):
        self._filein = filein
        self._fileout = fileout

    def check(self):
        if not self._filein.exists() or not self._filein.is_file():
            return False
        if not self._fileout.parent.exists() or \
                not self._fileout.parent.is_dir():
            return False
        mimetype_filein = mimetypes.guess_type(self._filein)[0]
        mimetype_fileout = mimetypes.guess_type(self._fileout)[0]
        if mimetype_filein not in ALLOWED_FROM:
            return False
        if mimetype_fileout not in ALLOWED_TO and \
                mimetype_filein != mimetype_fileout:
            return False
        return True

    def execute(self):
        image = Image.open(self._filein)
        image.save(self._fileout)


def main():
    filein = Path("/home/lorenzo/kk/bb.jpg")
    fileout = Path("/home/lorenzo/kk/bb.pdf")
    action = Convert(filein, fileout)
    if action.check():
        action.execute()


if __name__ == "__main__":
    main()
