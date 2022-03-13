"""Reto 02 Python Atareao"""
import os

def buscar_imagenes(archivo):

    """Filtrar imágenes jpg y jpeg"""
    return archivo.lower().endswith(('jpg', 'jpeg'))

def check_numero(string):

    """Comprobar si el nombre tiene un número"""
    return string.lower() if any(map(str.isdigit, string)) else string.upper()

def main():

    """Listar las imágenes dentro de descargas"""
    descargas = os.popen("xdg-user-dir DOWNLOAD").read().strip()

    archivos_jpg = filter(buscar_imagenes, os.listdir(descargas))

    for idx, val in enumerate(map(check_numero, archivos_jpg)):
        if idx % 2:
            print(idx, val)
        else:
            print('{} => "{}"'.format(idx, val))

if __name__ == '__main__':

    main()
