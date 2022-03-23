# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

# Para el proyecto "reto-python" de Lorenzo Carbonell <a.k.a. atareao>

import mimetypes  # Para los JPG
from os import listdir, path  # Para manejar rutas
import re  # Para buscar o reemplazar

# No tengo la menor idea de qué es lo de TOML y no sé
# si hay que implementar algo o cómo hacerlo.


def main():

    rutaDiogenes = path.join(path.expanduser(
        "~"), '.config\\diogenes\\diogenes.conf')

    # ¿Existe el archivo config? Si no, se crea:
    # No es buen condicional según PEP8, pero no sé cómo hacerlo si no.

    if path.isfile(rutaDiogenes) == False:
        with open(rutaDiogenes, "w") as f:
            f.write('directorio = "/Users/noave/Downloads"')

    # Se lee el archivo:

    with open(rutaDiogenes, "r") as f:
        dwnldDir = f.readline()

    # Aisla el directorio con expresiones regulares:

    patron = re.compile(r'"(\S+)"')
    reemplazo3 = re.findall(patron, dwnldDir)

    print(
        f"Imágenes JPG en el directorio {reemplazo3[0]}: \n-----------------------------")

    # Si los archivos del directorio son JPG, mostrarlos uno a uno:

    listArchivos = listdir(reemplazo3[0])
    for fichero in listArchivos:
        if mimetypes.guess_type(fichero)[0] == "image/jpeg":
            print(fichero)


if __name__ == "__main__":
    main()
