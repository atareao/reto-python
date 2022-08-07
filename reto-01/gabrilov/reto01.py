#!/usr/bin/env python

import re
from os import scandir, environ


def ls(ruta: str):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


homepath: str = environ['HOME']
carpeta: str = ''

with open(homepath + '/.config/user-dirs.dirs', 'rt') as archivo_dir:
    contenido: list[str] = archivo_dir.readlines()

for _, linea in enumerate(contenido):
    resultado = re.search(r'XDG_DOWNLOAD_DIR="\$HOME\/([a-zA-Z0-9].*)"$', linea)
    if resultado is not None:
        carpeta = resultado.group(1)

if carpeta is None:
    exit("No hay definida carpeta de descargas")

path_descargas: str = homepath + '/' + carpeta

print(path_descargas + "\n")

carpeta_descargas: list[str] = ls(path_descargas)

for archivo in carpeta_descargas:
    print(archivo)
