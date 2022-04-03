#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
from utils import list_images, decora


# =====================================================================
# Los dos bloques de código, el comentado con step1, step2 y main, y
# el main sin comentar son igualmente válidos y ambos funcionan, pero
# yo prefiero el segundo.
# =====================================================================
# def step1(path, config):
#     Configurator(path, config)
#
#
# def step2(path, config):
#     conf = Configurator(path, config).read()
#     for dir in conf['directorios'].values():
#         decora(dir['in'])
#         for image in list_images(Path(dir['in']),
#                                  mime_types=("image/jpeg",
#                                              "image/png"),
#                                  only_print=False):
#             print(image.name)
#
#
# def main(app, config):
#     path = Path(xdg_config_home()) / app
#     step1(path, config)
#     step2(path, config)
#
# =====================================================================

def main(app, config):
    path = Path(xdg_config_home()) / app
    # Cuando se llama al constructor de Configurator, se ejecuta el
    # método "check" y solo cuando se ha construido el objeto, se
    # ejecuta el método "read" con el chequeo ya hecho.
    conf = Configurator(path, config).read()
    for dir in conf['directorios'].values():
        decora(dir['in'])
        # Llamamos a list_mimetypes usando su otro nombre: list_images.
        for image in list_images(Path(dir['in']),
                                 mime_types=("image/jpeg", "image/png"),
                                 only_print=False):
            print(image.name)


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
