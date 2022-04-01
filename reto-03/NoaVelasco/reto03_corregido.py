# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Para el "reto-python" de Lorenzo Carbonell <a.k.a. atareao>

import os
import toml
import mimetypes
from pathlib import Path


configPath = os.path.join(os.path.expanduser("~"), 
                          '.config\\diogenes')
configFile = os.path.join(configPath, 'diogenes.conf')


def check_exist():
    """
    Comprueba que existen la ruta y  el archivo 
    de configuración. Si no, los crea.    
    """
    
    if not os.path.exists(configPath):
        os.mkdir(configPath)
        
    if not os.path.exists(configFile):
        contenidoConf = dict(directorio= '/Users/noave/Downloads')

        with open(configFile, "w") as f:
            toml.dump(contenidoConf, f)


def read_conf():
    """
    Lee el contenido del archivo toml.
    """
    
    contenidoConf = toml.load(configFile)
    return contenidoConf


def list_images(directory):
    """
    Comprueba que existe la carpeta que viene 
    en el archivo toml e imprime los archivos jpg.
    """
    
    if not os.path.exists(directory):
        os.mkdir(directory)
        
    for jpg in directory.iterdir():
        if not jpg.is_dir() and mimetypes.guess_type(jpg)[0] == "image/jpeg":
            print(jpg.name)


def main():
    check_exist()

if __name__ == "__main__":
    main()
    loadedConf = read_conf()
    list_images(Path(loadedConf['directorio']))
