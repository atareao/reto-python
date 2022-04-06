# -*- coding: utf-8 -*-
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
from typing import Union


mimetypes.init()


# La función 'list_mimetypes', cuando se llama con los keywords por
# defecto, produce el mismo resultado que la función 'list_images'
# usada en el reto-04: es backward compatible o compatible hacía
# atrás. La mejora consiste en que ahora podemos pedirle que filtre
# otros mime types a voluntad y pedirle que devuelva un objeto de
# tipo 'filter' en lugar de producir meros efectos laterales.

# DUDA: ¿Son correctas estas anotaciones de tipo (filter)?
def list_mimetypes(path: Path,
                   mime_types: tuple[str, ...] = ("image/jpeg",),
                   only_print: bool = True) -> Union[filter, None]:
    """\
    Listar los ficheros de "path" cuyo mime type esté en "mime_types".

    Parameters
    ----------
    path : Path
        El directorio que se quiere listar.
    mime_types : tuple[str, ...], optional
        Los mimetypes que se listarán. Por defecto es ("image/jpeg",).
    only_print : bool, optional
        Si es True la salida se envía a la salida estándar, en caso
        contrario retorna un objeto filter. The default is True.

    Returns
    -------
    None o filter

    """
    if only_print:
        print(f"Directorio {path}\n")
        for file in Path(path).iterdir():
            if mimetypes.guess_type(file)[0] in mime_types:
                print(file.name)
    else:
        # Una "inner function"
        def mimefilter(f):
            return mimetypes.guess_type(f)[0] in mime_types
        return filter(mimefilter, Path(path).iterdir())


# Las funciones en Python son "ciudadanos de primera clase" y se pueden
# asignar a otra variable. Ahora "list_images" y "list_mimetypes" son
# dos nombres (etiquetas) que hacen referencia al mismo objeto.
list_images = list_mimetypes


# Esto es por puro divertimento.
def decora(linea):
    deco = '≡' * (5 + len(linea))
    print('\n', deco)
    print(' ⭆', linea, '⭅')
    print(f" {deco}\n")


# Una vieja conocida que no utilizo en esta ocasión.
def ruta_valida(ruta: Path) -> Path:
    """Forzar que un path ('ruta') cumpla ciertos requisitos:

    1) Tiene que ser un path absoluto.
    2) Tiene que comenzar con /home/_USUARIO_
    3) Las variables de shell se sustituyen por su valor.
    4) El path se "normaliza": se sustituyen cosas como
       "/dir1/dir2/./dir3/../../dir4" por "/dir1/dir4".

    Parameters
    ----------
    ruta : Path
        El path que tenemos que procesar.

    Returns
    -------
    Path
        El path corregido.

    """
    home = Path().home()
    # No existen equivalentes a expandvars o normpath en pathlib.
    ruta = os.path.expandvars(ruta)
    ruta = Path(os.path.normpath(ruta))
    ruta = ruta.expanduser()
    if ruta.is_relative_to(home):
        return ruta
    if ruta.is_absolute():
        ruta = ruta.relative_to(ruta.anchor)
    ruta = home.joinpath(ruta)
    return ruta
