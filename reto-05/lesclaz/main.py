#  Copyright (c) 2022. LESCLAZ.
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  #
#  You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import sys

from app import CONFIG_PATH, CONFIG_FILE
from configurator import Configurator
from utils import list_images


# Lista todos los directorios "in" en el archivo de configuración, de existir
# este, en caso contrario lo crea y le añade el directorio de descargas del
# usuario. Además si se ejecuta la app con el parámetro -add añade el
# directorio al archivo de configuración, ejemplo: python3 main.py -add
# pepito /home/pepe/pepito/in /home/pepe/pepito/out.


def listar(dir_to_list: str) -> None:
    """
    Lista el directorio pasado como parámetro.
    :return:
    """
    print(f"Directorio: {dir_to_list}")
    for i, file in enumerate(list_images(dir_to_list)):
        file = file.lower() if re.findall('[0-9]+', file) else file.upper()
        print(f'{i} => {file}' if i % 2 == 0 else f'{i} {file}')
    print("\n")


def add_dir_conf(dir_conf: dict) -> None:
    """
    Añade un par de directorios (in, out) al archivo de configuración.
    :param dir_conf: dictado con la estructura del archivo de configuración.
    :return:
    """
    config = Configurator(CONFIG_PATH, CONFIG_FILE)
    conf = config.read()
    conf['directorios'] = {
        **conf['directorios'],
        **dir_conf['directorios']
    }
    config.save(conf)


def main() -> None:
    """
    Crea una instancia de la clase `Configurator` pasándole como parámetros
    la ruta a la carpeta que alojara el archivo de configuración y el nombre
    de dicho archivo, luego hace una llamada al método listar pasándole como
    parámetro el directorio `in` de cada par (in, out).
    :return:
    """
    config = Configurator(CONFIG_PATH, CONFIG_FILE)
    dirs_conf = config.read()["directorios"]
    for dir_ in dirs_conf:
        listar(dirs_conf[dir_]["in"])


if __name__ == '__main__':

    # Si el usuario ejecuta `python main.py` listara las imágenes en los
    # directorios `in` especificados en el archivo de configuración.
    if len(sys.argv) == 1:
        main()

    # Si usa -add como parámetro adicional, tomará e interpretará las 3 cadenas
    # siguientes como nombre para el par de directorios (in, out), la ruta
    # hacia el directorio `in` y la ruta hacia el directorio `out`
    # respectivamente.
    elif sys.argv[1] == "-add":
        add_dir_conf(
            {
                "Directorios": {
                    sys.argv[2]: {
                        "in": sys.argv[3],
                        "out": sys.argv[4]
                    }
                }
            }
        )

    # Si usa -h como parámetro, se imprimirá una pequeña ayuda.
    elif sys.argv[1] == "-h":
        print(
            'Uso: python3 main.py -add {name config dir} {dir "in"} '
            '{dir "out"}'
        )

    # En cualquier otro caso, imprimirá un mensaje de error.
    else:
        print("Mala ejecución")
