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


"""
Lista todos los directorios "in" en el archivo de configuracion, de existir
este, en caso contrario lo crea y le añade el directorio de descargas del
usuario. Ademas si se ejecuta la app con el parametro -add añade el directorio
al archivo de configuracion, ejemplo: python3 main.py -add {nombre del la
seccion} {ruta directorio in} {ruta directorio out}. no se usan las llaves.
"""


def listar(dir_to_list):
    print(f"Directorio: {dir_to_list}")
    for i, file in enumerate(list_images(dir_to_list)):
        file = file.lower() if re.findall('[0-9]+', file) else file.upper()
        print(f'{i} => {file}' if i % 2 == 0 else f'{i} {file}')
    print("\n")


def add_dir_conf(dir_conf: dict):
    config = Configurator(CONFIG_PATH, CONFIG_FILE)
    conf = config.read()
    conf['Directorios'] = {
        **conf['Directorios'],
        **dir_conf['Directorios']
    }
    config.save(conf)


def main():
    config = Configurator(CONFIG_PATH, CONFIG_FILE)
    dirs_conf = config.read()["Directorios"]
    for dir_ in dirs_conf:
        listar(dirs_conf[dir_]["in"])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
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
    elif sys.argv[1] == "-h":
        print("""
        Uso: python3 main.py -add {name config dir} {dir "in"} {dir "out"}
        """)
    else:
        print("Mala ejecucion")
