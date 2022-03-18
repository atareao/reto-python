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

import mimetypes
import re
from gi.repository import GLib
from pathlib import Path

mimetypes.init()

def main():
    try:
        downloads_dir = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
        print(f"\nDirectorio: {downloads_dir}\n")
        patron = r".*[0-9].*"
        if downloads_dir.is_dir():
            for index, afile in enumerate(downloads_dir.iterdir()):
            #for index, afile in enumerate downloads_dir.iterdir():
            #for index, afile in enumerate([x for x in downloads_dir.iterdir() if not x.is_dir()]):
                if afile.is_file():
                    if re.match(patron, afile.name):
                        nombre = afile.name.lower()
                    else:
                        nombre = afile.name.upper()
                    #nombre = afile.name.lower() if re.match(patron, afile.name) else afile.name.upper()
                    if mimetypes.guess_type(afile)[0] == "image/jpeg":
                        if index % 2 == 0:
                            print(index, f" => \"{nombre}\"")
                        else:
                            print(index, nombre)
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()
