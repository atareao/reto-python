#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Diogenes, reto-06: main."""

# Copyright (c) 2022 José Lorenzo Nieto Corral <a.k.a. jlnc> <a.k.a JoseLo>

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
from xdg import xdg_config_home
from configurator import Configurator
from utils import list_images, action

# Constantes de conveniencia.
CONFIG_FILE = "diogenes.toml"

CONFIG_HEADER = Configurator.HEADER
DIRS_IN = Configurator.DIR_INPUT
DIRS_OUT = Configurator.DIR_OUTPUT


def main(app, config):
    """El main."""
    path = Path(xdg_config_home()) / app
    conf = Configurator(path, config).read()
    for item in conf['directorios'].values():
        # Leer el path a los dos directorios y la acción.
        dir_in, dir_out = Path(item[DIRS_IN]), Path(item[DIRS_OUT])
        action_name = item['action']
        # Ver el contenido de los directorios ANTES de la acción.
        print("\t -- {"f'antes de: {action_name}'"} --\n")
        for dir_ in (dir_in, dir_out):
            list_images(dir_)
        # Ejecutar la acción.
        action(dir_in, dir_out, action=action_name)
        # Ver el contenido de los directorios DESPUÉS de la acción.
        print("\t -- {"f'después de: {action_name}'"} --\n")
        for dir_ in (dir_in, dir_out):
            list_images(dir_)
        print(f"{80*'_'}\n")


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
