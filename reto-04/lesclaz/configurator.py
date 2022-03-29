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
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os

import toml

from utils import get_downloads_dir


class Configurator:

    def __init__(self, path, config):
        self.path = path
        self.config_file = os.path.join(path, config)
        self.__verify_config_file()

    def __verify_config_file(self):
        """
        Verifica si existe el archivo pasado como parámetro al crear la
        instancia de la clase, y de no ser así, lo crea.
        __ oculta la función impidiendo su acceso de forma sencilla.
        """
        os.makedirs(self.path, exist_ok=True)
        if not os.path.exists(self.config_file):
            with open(self.config_file, "w") as fp:
                fp.write(toml.dumps({"directorio": get_downloads_dir()}))

    def read(self):
        """
        Lee el archivo de configuración y devuelve su contenido.
        """
        with open(self.config_file) as f:
            return toml.load(f)
