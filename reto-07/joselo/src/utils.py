# -*- coding: utf-8 -*-

"""Diogenes, reto-07: utilidades."""

# Copyright (c) 2022 José Lorenzo Nieto Corral <a.k.a. jlnc> <a.k.a. JoseLo>

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


import fnmatch
import os
from pathlib import Path
import shutil


# En el reto 7 ya no hay que listar los ficheros de un tipo determinado, hay
# listarlos todos.
def list_all(d_in: Path, d_out: Path) -> None:
    """
    Listar los ficheros de ambos directorios.

    Parameters
    ----------
    d_in : Path
        El directorio origen.
    d_in : Path
        El directorio destino.

    Returns
    -------
    None

    """
    for path in [d_in, d_out]:
        print(f"=== Directorio {path} ===")
        for file in Path(path).iterdir():
            print(file.name)
        print(f"\t{28*'·'}\n")


# =====================================================================
# FILTROS
#
# Ver https://gist.github.com/jlnc/26c041127117c1932929225097db96cd
#
def glob_factory(glb: str) -> callable:  # noqa
    def filter_glob(files: set) -> set:
        return set(fnmatch.filter(files, glb))
    return filter_glob


# Ejemplos de filtros:
filter_all = glob_factory('*')
filter_gif = glob_factory('*.gif')
filter_jpg = glob_factory('*.jpg')
filter_pdf = glob_factory('*.pdf')
filter_png = glob_factory('*.png')
filter_sh = glob_factory('*.sh')
filter_svg = glob_factory('*.svg')
filter_txt = glob_factory('*.txt')


# =====================================================================
# ACCIONES
#
def __move(path_in: Path, path_out: Path,
           fltr: callable = filter_all) -> None:
    files = set([f.name for f in path_in.iterdir()])
    for src in fltr(files):
        dest = path_out / src
        if not dest.exists():
            shutil.move(path_in / src, path_out)
        else:
            print("Action move:\n"
                  f"No es posible mover {src} a {str(path_out)} "
                  "porque ya existe un fichero con el mismo nombre.\n\n"
                  f"Se procede a borrar el fichero {src} de {str(path_in)}.")
            os.remove(path_in / src)


def __copy(path_in: Path, path_out: Path,
           fltr: callable = filter_all) -> None:
    files = set([f.name for f in path_in.iterdir()])
    for src in fltr(files):
        dest = path_out / src
        if not dest.exists():
            shutil.copy(path_in / src, path_out, follow_symlinks=False)


# Un diccionario para recopilar las acciones disponibles.
action = {
    "none": lambda *args, **kwords: None,
    "move": __move,
    "copy": __copy
    }


def add_action(name):
    """Un decorador para añadir nuevas acciones al diccionario.

    Ejemplo de uso:

        @add_action('nueva')
        def nueva_accion():
            print("Una nueva accion.")

    """
    def register_action(func):
        action[name] = func
        return func
    return register_action
