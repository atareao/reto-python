#!/usr/bin/env python3
# List Downloads folder content
import os

home = os.path.expanduser('~')

def list_files():
    if os.path.isdir('~/Descargas'):
        print(f'Directorio: {home}/Descargas\n')
        (os.system('find ~/Descargas -maxdepth 1 -type f -printf "%f\n"'))
    else:
        print(f'Directorio: {home}/Downloads\n')
        (os.system('find ~/Downloads -maxdepth 1 -type f -printf "%f\n"'))

list_files()