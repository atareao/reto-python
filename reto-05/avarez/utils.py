''' UTILS '''

# -*- coding: utf-8 -*-

# Copyright (c) 2022 Andrés Pérez <a.k.a. avarez>

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
import magic
import app_globals


def list_dir(toml_cfg_dict, filetype):
    '''
    FUNCIÓN QUE LISTA DIRECTORIOS ESPECIFICADOS EN FICHERO TOML
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
    dir_list = []
    for dict_entries in dict_cfg.values():
        for dir_type, dir_entry in dict_entries.items():
            if dir_type == 'in':
                dir_list.append(dir_entry)
    for dir_entry in dir_list:
        if os.path.isdir(dir_entry):
            print("⇨", dir_entry, "⇦")
            for dir_entry_item in os.listdir(dir_entry):
                apf = os.path.join(dir_entry, dir_entry_item)
                if not os.path.isdir(apf):
                    if filetype == magic.from_file(apf, mime=True):
                        print(f"{dir_entry_item}")
