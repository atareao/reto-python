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

from xdg import Path
from xdg.BaseDirectory import xdg_config_home


if __name__ == "__main__":

    xdg_user_dirs = Path(xdg_config_home) / "user-dirs.dirs"

    try:
        with open(xdg_user_dirs, 'r') as f:
            # Vivamos peligrosamente... :D
            exec(f.read().replace("$HOME", os.environ["HOME"]))
    except Exception as exception:
        msg = f"No se encuentra el fichero {xdg_user_dirs}"
        raise RuntimeError(msg) from exception

    try:
        downloads_dir = Path(XDG_DOWNLOAD_DIR)
        print(f"\nDirectorio: {XDG_DOWNLOAD_DIR}\n")
        for f in downloads_dir.iterdir():
            if f.is_file() and not f.is_symlink():
                print(str(f))
    except Exception as exception:
        msg = f"No existe el directorio {XDG_DOWNLOAD_DIR}"
        raise RuntimeError(msg) from exception
