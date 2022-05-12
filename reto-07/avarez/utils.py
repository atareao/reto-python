#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 14 April 2022

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
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import shutil
from pathlib import Path
import app_globals


def run(toml_cfg_dict):
    '''
    FUNCIÓN QUE PROCESA ACCIONES ENTRE DIFERENTES DIRECTORIOS
    ESPECIFICADOS EN FICHERO TOML
    '''
    if toml_cfg_dict:
        if toml_cfg_dict["directorios"]:
            dict_cfg = toml_cfg_dict["directorios"]
        else:
            print(f"Fichero {app_globals.CONFIG} no válido")
            return
    else:
        print(f"Fichero {app_globals.CONFIG} no válido")
        return
    for dict_entries in dict_cfg.values():
        for action in dict_entries['actions']:
            if os.path.isdir(dict_entries['in']):
                src = dict_entries['in']
                if os.path.isdir(dict_entries['out']):
                    dest = dict_entries['out']
                    for src_userfile in Path(src).glob(dict_entries['filter']):
                        dest_userfile = \
                            os.path.join(dest, os.path.basename(src_userfile))
                        if action == 'copy':
                            if os.path.isfile(dest_userfile):
                                os.remove(dest_userfile)
                            shutil.copy(src_userfile, dest)
                        elif action == 'move':
                            if os.path.isfile(dest_userfile):
                                os.remove(dest_userfile)
                            shutil.move(src_userfile, dest)
                        elif action == 'none':
                            pass
