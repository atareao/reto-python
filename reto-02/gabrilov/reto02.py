#!/usr/bin/env python

import re
### La siguiente importación puede dar error ###
### aún después de instalarlo con pip.       ###
### Se soluciona instalando el paquete       ###
### python-magic con el gestor de paquetes   ###
### de la distribución (apt, pacman, etc.)   ###
import magic
from os import scandir, environ

# Lista los archivos jpg en la ruta que se pase
def ls_jpg(ruta: str) -> list[str]:
    mime = magic.Magic(mime=True)
    return [arch.name for arch in scandir(
        ruta) if arch.is_file() and mime.from_file(arch) == 'image/jpeg']


# Obtiene la carpeta de descargas del usuario
def get_download_dir() -> str:
    homepath: str = environ['HOME']
    carpeta: str = ''
    with open(homepath + '/.config/user-dirs.dirs', 'rt') as archivo_dir:
        contenido: list[str] = archivo_dir.readlines()
    for _, linea in enumerate(contenido):
        resultado = re.search(
            r'XDG_DOWNLOAD_DIR="\$HOME\/([a-zA-Z0-9].*)"$', linea)
        if resultado is not None:
            carpeta = resultado.group(1)
        if carpeta is None:
            exit("No hay definida carpeta de descargas")
    return f"{homepath}/{carpeta}"


def main():
    path_descargas: str = get_download_dir()
    print(f'Carpeta de descargas: {path_descargas}\n')
    archivos_descargas: list[str] = ls_jpg(path_descargas)
    # Se itera sobre los jpg para agregar => a los pares
    for index, archivo in enumerate(archivos_descargas):
        prefix: str = "=>" if (index + 1) % 2 == 0 else ""
        print(f'{index + 1} {prefix} {archivo}\n')


if __name__ == "__main__":
    main()
