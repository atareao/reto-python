'''RETO PYTHON (ATAREAO) - EJERCICIO 3'''

import os
from os.path import exists
import magic
import toml

HOME = os.path.expanduser('~')
USER_DIRS = f"{HOME}/.config/user-dirs.dirs"

TOML_FILE = f"{HOME}/.config/diogenes/diogenes.conf"
TOML_DIR = f"{HOME}/.config/diogenes"

USER_DIRS_DICT = {}
TOML_DICT = {}


def find_users_dirs():
    '''
    FUNCIÓN QUE CREA UN DICT CON LOS DIRECTORIOS DE USUARIO
    '''
    if exists(USER_DIRS):
        with open(USER_DIRS, "rt", encoding="utf-8") as filesteam:
            content = filesteam.readlines()
        for line in content:
            if line.startswith("XDG"):
                item_list = line.strip("\n").split("=")
                USER_DIRS_DICT[item_list[0]] = \
                    item_list[1].replace("$HOME", HOME).replace('"', "")



def check_toml():
    '''
    FUNCIÓN QUE COMPRUEBA EXISTENCIA FICHERO TOML
    - SI NO EXISTE EL DIRECTORIO LO CREA

    - SI NO EXISTE EL FICHERO LO CREA Y LO RELLENA CON EL DIRECTORIO DE USUARIO
    - SI EXISTE CARGA LAS ASIGNACIONES A UN DICCIONARIO
    '''
    global TOML_DICT
    if not exists(TOML_DIR):
        os.mkdir(TOML_DIR)
        print(f"Creado el directorio {TOML_DIR}")

    if not exists(TOML_FILE):
        find_users_dirs()
        TOML_DICT["directorio"] = USER_DIRS_DICT["XDG_DOWNLOAD_DIR"]
        with open(TOML_FILE, "w", encoding="utf-8") as fp:
            toml.dump(TOML_DICT, fp)
    TOML_DICT = toml.load(TOML_FILE)


def list_dir(user_path, filetype):
    '''
    FUNCIÓN QUE LISTA DIRECTORIOS
    '''
    if os.path.isdir(user_path):
        for file in os.listdir(user_path):
            absolute_path_file = os.path.join(user_path, file)
            if filetype == magic.from_file(absolute_path_file, mime=True):
                print(f"{file}")


def main():
    '''
    MAIN
    '''
    check_toml()
    list_dir(TOML_DICT["directorio"], "image/jpeg")

if __name__ == '__main__':
    main()

