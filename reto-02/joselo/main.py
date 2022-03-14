#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022 JLNC

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
import re

from xdg import Path
from xdg.BaseDirectory import xdg_config_home


USER_DIRS_FILE = os.path.join(xdg_config_home, 'user-dirs.dirs')


def get_downloads_dir():
    try:
        with open(USER_DIRS_FILE, 'r') as f:
            for line in f.readlines():
                if line.startswith('XDG_DOWNLOAD_DIR'):
                    line = line.strip() \
                            .replace('"', '') \
                            .replace("$HOME", os.environ['HOME'])
                    key, _ , XDG_DOWNLOAD_DIR = line.partition('=')
    except Exception as exception:
        msg = f"No se encuentra el fichero {USER_DIRS_FILE}"
        raise RuntimeError(msg) from exception

    return XDG_DOWNLOAD_DIR


def main():

    pnum = re.compile(r'.*\d+')
    pjpg = re.compile(r'.*\.(jpe?g|JPE?G)$')

    try:
        downloads_dir = Path(get_downloads_dir())
        print(f"\nDirectorio: {downloads_dir}\n", flush=True)
        # Primero los nombres de los ficheros
        files = [x.name for x in downloads_dir.iterdir() if not x.is_dir()]
        # Después filtro los jpegs
        jpegs = [x for x in files if pjpg.match(x)]
        for n, name in enumerate(jpegs):
            name = name.upper() if pnum.match(name) else name.lower()
            prefix = " => " if n % 2 == 0 else ' '
            print(str(n) + prefix + name)
    except Exception as exception:
        msg = f"No existe el directorio {XDG_DOWNLOAD_DIR}"
        raise RuntimeError(msg) from exception


if __name__ == "__main__":
    main()