#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__license__ = """
MIT License

Copyright (c) 2022 JLNC.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import os.path as osp
import toml
import mimetypes

from xdg.BaseDirectory import xdg_config_home
from easyansi import screen  # pip install --user easyansi
from easyansi.drawing import box
from easyansi.cursor import locate
from easyansi.attributes import (
    normal,
    dim,
    italic,
    italic_off,
    underline_code,
    underline_off_code
    )

mimetypes.init()


XDG_USER_DIRS = osp.join(xdg_config_home, 'user-dirs.dirs')
DGNS_CONF_DIR = osp.join(xdg_config_home, 'diogenes')
DGNS_CONF_FILE = osp.join(DGNS_CONF_DIR, 'diogenes.conf')

PRESENTACION = """\
 Diogenes es una aplicación pensada para la limpieza y organización semi automática
 de los directorios donde realizamos las descargas. En el estadio de desarrollo
 actual, Diogenes solo lista los ficheros de tipo "image/jpeg" del directorio que se
 encuentra en el fichero de configuración "~/.config/diogenes/diogenes.conf".

 Ese directorio es por defecto el directorio estándar de descargas del usuario pero
 puede ser cambiado a voluntad del usuario editando el fichero de configuración o
 bien introduciendo una ruta válida en el menú que se ofrece a continuación.
"""


def get_user_dirs():
    ud = toml.load(XDG_USER_DIRS)
    ud = {k: osp.expandvars(ud[k]) for k in ud.keys()}
    return ud


def read_dgns_dir():

    try:
        dgdir = toml.load(DGNS_CONF_FILE)['directorio']
    except (FileNotFoundError, KeyError):
        dgdir = get_user_dirs()['XDG_DOWNLOAD_DIR']

    lineas = PRESENTACION.split('\n')
    box_width = 4 + max(len(x) for x in lineas)
    box_height = 1 + len(lineas)

    while True:
        screen.clear()
        box(box_width, box_height, style="d")
        dim()
        italic()
        for fila, linea in enumerate(lineas):
            locate(1, fila + 1)
            print(linea)
        normal()
        italic_off()
        print()
        print("El directorio de trabajo actual es: "
              f"{underline_code()}{dgdir}{underline_off_code()}")
        print(
            "Si quieres conservar ese directorio pulsa ENTER, en caso contrario "
            "introduce una ruta\nválida para el nuevo directorio: ")
        respuesta = input(" >> ")
        if not respuesta:
            break
        respuesta = osp.normpath(osp.expanduser(respuesta))
        if osp.isdir(respuesta):
            dgns_dir = respuesta
        else:
            print(f"{respuesta} no es un directorio válido.")

    pass


def main():
    os.makedirs(DGNS_CONF_DIR, mode=0o755, exist_ok=True)
    dgns_dir = read_dgns_dir()
    screen.clear()
    print(f"Directorio {dgns_dir}\n")
    for file in os.listdir(dgns_dir):
        if mimetypes.guess_type(file)[0] == "image/jpeg":
            print(file)


if __name__ == "__main__":
    main()
