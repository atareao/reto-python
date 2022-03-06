'''RETO PYTHON (ATAREAO) - EJERCICIO 1'''

import os
from os.path import exists

HOME = os.path.expanduser('~')
USER_DIRS = f"{HOME}/.config/user-dirs.dirs"
user_dirs_dict = {}


def find_users_dirs():
    ''' FUNCIÓN QUE CREA UN DICT CON LOS DIRECTORIOS DE USUARIO
    DEVUELVE 1 SI ENCONTRÓ EL ARCHIVO, 0 EN CASO CONTRARIO. '''
    if exists(USER_DIRS):
        with open(USER_DIRS, "rt", encoding="utf-8") as filesteam:
            content = filesteam.readlines()
        for line in content:
            if line.startswith("XDG"):
                item_list = line.strip("\n").split("=")
                user_dirs_dict[item_list[0]] = item_list[1].replace("$HOME", HOME).replace('"', "")
        return 1
    else:
        return 0


def list_dir(user_path):
    ''' FUNCIÓN QUE LISTA SÓLO FICHEROS EN DIRECTORIOS '''
    found = False
    if os.path.isdir(user_path):
        for file in os.listdir(user_path):
            absolute_path_file = os.path.join(user_path, file)
            if not os.path.islink(absolute_path_file):
                if not os.path.isdir(absolute_path_file):
                    print(file)
                    found = True
        if not found:
            print("No se encontraron ficheros...")
    else:
        print(f"{user_path} no existe!")


if __name__ == '__main__':
    if find_users_dirs():
        print(f"Directorio: {user_dirs_dict['XDG_DOWNLOAD_DIR']}")
        list_dir(user_dirs_dict["XDG_DOWNLOAD_DIR"])
    else:
        print("No se encontraron directorios de usuario...")
