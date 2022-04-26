# -*- coding: utf-8 -*-

"""Diogenes, reto-06: utilidades."""

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


import os
import mimetypes
from pathlib import Path
import shutil
from typing import Union, Iterable


mimetypes.init()


MIME_TYPES = ("image/jpeg", "image/png", "image/svg+xml", "image/gif")


def list_images(path: Path) -> Union[Iterable, None]:
    """
    Listar los ficheros de "path" cuyo mime type esté en "MIME_TYPES".

    Parameters
    ----------
    path : Path
        El directorio que se quiere listar.

    Returns
    -------
    None

    """
    print(f"=== Directorio {path} ===")
    for file in Path(path).iterdir():
        if mimetypes.guess_type(file)[0] in MIME_TYPES:
            print(file.name)
    print(f"\t{28*'·'}\n")


# ====================================================================
# Una forma clásica de resolver el problema: cada acción es una de las
# opciones de una sentencia `case` de `C` o, en el caso de Python, una
# de las opciones de un if-elif-else; aunque en este caso es aún más
# simple.
#
# En este caso el uso sería:
#    action(dir_in, dir_out, action=action_name)
#
def func_action(path_in: Path, path_out: Path, action: str = "none") -> None:
    """
    Aplica la acción definida en "action" a los ficheros de "path_in".

    Parameters
    ----------
    path_in : Path
        El directorio de los ficheros que queremos procesar.
    path_out : Path
        El directorio al que debemos mover/copiar los ficheros de
        "path_in".
    action : str, optional
        La acción que hay que aplicar:
            "none": No se realizará ninguna acción.
            "move": Se moverán todos los archivos en cada uno de los
                    directorios del `in` al `out`. Si existen en el
                    directorio de destino se tienen que borrar del
                    directorio de destino primero.
            "copy": Se copiarán todos los archivos del directorio `in`
                    al directorio `out` siempre y cuando no exista un
                    archivo con el mismo nombre en el directorio `out`.
        The default is "none".

    Raises
    ------
    ValueError
        Solo se admiten tres acciones: "none", "move" y "copy".

    Returns
    -------
    None

    """
    if action not in ("none", "move", "copy"):
        raise ValueError("Acción no válida.")

    if action == 'none':
        return

    if action == 'move':
        for src in path_in.iterdir():
            dest = path_out / src.name
            if dest.is_file():
                dest.unlink(missing_ok=True)
            shutil.move(src, path_out)
    else:  # action == 'copy'
        for src in path_in.iterdir():
            dest = path_out / src.name
            if not dest.exists() and not src.is_dir():
                shutil.copy2(src, path_out, follow_symlinks=False)


# ====================================================================
# Otra forma, no sé si más "pythonica", de resover el problema: un
# diccionario y varias funciones por separado.
#
# La ventaja de esta segunda forma es la facilidad con la que podemos
# añadir nuevas acciones.

def __move(path_in: Path, path_out: Path) -> None:
    for src in path_in.iterdir():
        dest = path_out / src
        if dest.is_file():
            dest.unlink(missing_ok=True)
        shutil.move(src, path_out)


def __copy(path_in: Path, path_out: Path) -> None:
    for src in path_in.iterdir():
        dest = path_out / src
        if not dest.exists() and not src.is_dir():
            shutil.copy2(src, path_out, follow_symlinks=False)


# En este caso el uso sería:
#    action[action_name](dir_in, dir_out)
dir_action = {
    "none": lambda x=None, y=None: None,
    "move": __move,
    "copy": __copy
    }
# ====================================================================


action = func_action
