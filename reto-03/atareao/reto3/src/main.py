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
import os
import toml
from pathlib import Path
from xdg import xdg_config_home

APP = "diogenes"
CONFIG = f"{APP}.conf"


def check_conf():
    config_dir = Path(xdg_config_home()) / APP
    if not config_dir.exists():
        os.makedirs(config_dir)
    config_file = config_dir / CONFIG
    if not config_file.exists():
        idata = {}
        idata["directorio"] = "/home/lorenzo/Descargas"
        with open(config_file, 'w') as file_writer:
            toml.dump(idata, file_writer)


def read_conf():
    config_dir = Path(xdg_config_home()) / APP
    config_file = config_dir / CONFIG
    idata = toml.load(config_file)
    return idata


def list_images(directory):
    if not directory.exists():
        os.makedirs(directory)
    for afile in directory.iterdir():
        if not afile.is_dir() and mimetypes.guess_type(afile)[0] == 'image/jpeg':
            print(afile.name)

def main():
    check_conf()
    data = read_conf()
    list_images(Path(data['directorio']))

if __name__ == '__main__':
    main()
