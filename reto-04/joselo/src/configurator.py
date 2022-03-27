# -*- coding: utf-8 -*-
# Copyright (c) 2022 José Lorenzo Nieto Corral <a.k.a. jlnc> <a.k.a. JoseLo>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
from pathlib import Path
import toml
from xdg import XDG_CONFIG_HOME


class Configurator:
    """Clase Configurator: crear y manejar la configuración de Diogenes.
    """

    def __init__(self, path: Path, config: str) -> None:
        """Constructor.

        :param: path: La ruta al directorio de la configuración.
        :param: config: El nombre del fichero de configuración.
        """
        self._set_config_dir(path)
        self._set_config_file(config)

    def _set_config_dir(self, path: Path) -> None:
        """Crear el directorio de la aplicación.

        Asegurarnos de que al constructor no se le pasan rutas extrañas, de
        que el path del directorio de la aplicación está donde debe estar y
        de que ese directorio existe.
        """
        def ruta_valida(ruta: Path) -> Path:
            home = Path().home()
            # No existen equivalentes a expandvars o normpath en pathlib.
            ruta = os.path.expandvars(ruta)
            ruta = Path(os.path.normpath(ruta))
            ruta = ruta.expanduser()
            if ruta.is_relative_to(home):
                return ruta
            if ruta.is_absolute():
                ruta = ruta.relative_to(ruta.anchor)
            ruta = home.joinpath(ruta)
            return ruta

        self._config_dir = ruta_valida(path)
        if not self._config_dir.exists():
            os.makedirs(self._config_dir, exist_ok=True)

    def _set_config_file(self, config: str) -> None:
        """Crear el fichero de configuración y definir el directorio de descargas.

        Hay que asegurar que el nombre del fichero dado en el argumento es un
        mombre de fichero válido. Los caráteres no válidos para el nombre de un
        fichero son: '\\/:*?"<>|', al espacio en blanco le damos un tratamiento
        diferente: no se acepta ni al principio ni al final del nombre y se
        reemplaza por '_' cuando está en el interior del nombre.
        """

        fname = config.strip().replace(' ', '_')
        if any(c in fname for c in '\\/:*?"<>|'):
            raise ValueError
        self._config_file = self._config_dir / fname

        try:
            directorio = toml.load(self._config_file)["directorio"]
        except (FileNotFoundError, KeyError):
            directorio = ''

        if not os.path.exists(directorio):

            try:
                xdg_config_file: Path = XDG_CONFIG_HOME / "user-dirs.dirs"
                user_dirs = toml.load(xdg_config_file)
                directorio = os.path.expandvars(user_dirs["XDG_DOWNLOAD_DIR"])

            except FileNotFoundError as exception:
                msg = f"""\
No existe el fichero {0} que define los directorios de usuario del Cross
Desktop Group (XDG) de freedesktop.org y no es posible continuar.
""".format(xdg_config_file)
                raise RuntimeError(msg) from exception

            except KeyError as exception:
                msg = f"""\
No se ha podido encontrar una entrada que defina el directorio estándar
de descargas en el fichero de configuración {0} y no es posible
continuar.""".format(xdg_config_file)
                raise RuntimeError(msg) from exception

        with open(self._config_file, 'w', encoding='utf-8') as file_write:
            data = dict()
            data["directorio"] = directorio
            toml.dump(data, file_write)

    def read(self):
        return toml.load(self._config_file)
