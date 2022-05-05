#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Diogenes, reto-07: main."""

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

from _constants import (
    CONFIG_HEADER,
    CONFIG_DIR_IN,
    CONFIG_DIR_OUT,)
from pathlib import Path
from xdg import xdg_config_home
from configurator import Configurator
from utils import (
    list_all,
    action,
    glob_factory)


def main(app, config):
    """El main."""
    path = Path(xdg_config_home()) / app
    conf = Configurator(path, config).read()

    for item in conf[CONFIG_HEADER].values():

        # Leer el path a los dos directorios y la acción.
        dir_in = Path(item[CONFIG_DIR_IN])
        dir_out = Path(item[CONFIG_DIR_OUT])

        # Ver el contenido de los directorios ANTES de la acción.
        print(
            "\t -- {antes de: "
            f"{repr(item['actions'])}; filtro: {item['filter']}"
            "} --\n")
        list_all(dir_in, dir_out)

        # Ejecutar las acciones.
        for action_name in item['actions']:
            filtro = glob_factory(item['filter'])
            action[action_name](dir_in, dir_out, fltr=filtro)

        # Ver el contenido de los directorios DESPUÉS de la acción.
        print(
            "\t -- {después de: "
            f"{repr(item['actions'])}; filtro: {item['filter']}"
            "} --\n")
        list_all(dir_in, dir_out)

        print(f"{80*'_'}\n")


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
