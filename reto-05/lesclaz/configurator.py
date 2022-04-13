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

import os
from pathlib import Path
from typing import MutableMapping, Any, Mapping

import toml

from utils import get_downloads_dir


class Configurator:

    def __init__(self, path: str, config: str):
        """
        Interfaz que permite crear, leer o guardar un archivo de configuración.
        :param path: ruta hacia el directorio que alojara el archivo de
        configuración.
        :param config: nombre del archivo de configuración.
        """
        self.path = path
        self.config_file = Path(path, config)

        # verificar si existe el archivo de configuración.
        self.__verify_config_file()

        # crear directorios que no existan.
        self.__create_dirs()

    def __create_dirs(self) -> None:
        """
        Crea los Directorios del archivo de configuración que no existan.
        __ oculta la función impidiendo su acceso de forma sencilla.
        """
        if "directorios" in self.read():
            dirs = self.read()["directorios"]
            try:
                for dir_ in dirs:
                    os.makedirs(dirs[dir_]["in"], exist_ok=True)
                    os.makedirs(dirs[dir_]["out"], exist_ok=True)
            except KeyError:
                raise Exception(
                    "El archivo de configuración está mal formateado."
                )

    def __verify_config_file(self) -> None:
        """
        Verifica si existe el archivo pasado como parámetro al crear la
        instancia de la clase, y de no ser así, lo crea.
        __ oculta la función impidiendo su acceso de forma sencilla.
        """
        os.makedirs(self.path, exist_ok=True)
        if not os.path.exists(self.config_file):
            with open(self.config_file, "w") as fp:
                fp.write(toml.dumps({
                    "directorios": {
                        "1": {
                            "in": get_downloads_dir(),
                            "out": get_downloads_dir()
                        }
                    }
                }))

    def read(self) -> MutableMapping[str, Any]:
        """
        Lee el archivo de configuración y devuelve su contenido.
        :return: contenido del archivo de configuración.
        """
        with open(self.config_file) as f:
            return toml.load(f)

    def save(self, config: Mapping[str, Any]) -> None:
        """
        Guarda la configuración en el archivo.
        :param config: Mapping[str, Any] con la estructura del archivo de
        configuración o str resultante de toml.dumps().
        """
        with open(self.config_file, "w") as file:
            file.write(toml.dumps(config))
