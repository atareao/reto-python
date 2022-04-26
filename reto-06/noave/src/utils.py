#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import mimetypes
import shutil


def list_images(directory):
    """
    Comprueba que existe un directorio dado
    e imprime los archivos JPG que haya dentro.
    """
    # if not directory.exists(): según ATAREAO
    if not os.path.exists(directory):
        os.makedirs(directory)

    for image in directory.iterdir():
        if image.is_file() and mimetypes.guess_type(image)[0] in [
            "image/jpeg",
            "image/png",
            "image/svg+xml",
        ]:
            print(image.name)


def copy(source, dest):
    """Copia los archivos de un directorio a otro,
    a menos que ya existan en el directorio de destino."""
    images = os.listdir(source)
    for image in images:
        if not os.path.exists(f"{dest}/{image}"):
            shutil.copy2(f"{source}/{image}", dest)


def move(source, dest):
    """Mueve los archivos de un directorio a otro.
    Si ya existen, borra primero los de destino."""
    images = os.listdir(source)
    for image in images:
        if os.path.exists(f"{dest}/{image}"):
            os.remove(f"{dest}/{image}")
        shutil.move(f"{source}/{image}", dest)
