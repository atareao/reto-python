# -*- coding: utf-8 -*-

"""atareao/reto-python, reto-07: clase Configurator."""

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


from _constants import (
    CONFIG_DEFAULT,
    CONFIG_DIR_IN,
    CONFIG_DIR_OUT,
    CONFIG_HEADER,)
import os
from pathlib import Path
import toml
from typing import (
    Any,
    Dict,
    MutableMapping,
    Union)


class Configurator:
    """Una clase para generar y verificar la configuración."""

    def __init__(self, path: Path, config: str) -> None:
        """Constructor.

        Almacena los parametros de entada y chequea la configuración.

        Parameters
        ----------
        path : Path
            El path al directorio de la configuración.
        config : str
            El nombre del fichero de configuración.

        Returns
        -------
        None

        """
        self.__directory = path
        self.__filename = config
        # La ruta hasta el fichero de configuración. Read Only.
        self.__config_file = self.__directory / self.__filename
        self.check()

    def check(self) -> None:
        """Chequea la integridad de la configuración.

        1) Si no existe el directorio de la configuración, lo crea.

        2) Si no existe el fichero de configuración, lo crea y escribe
           el nombre de la sección principal: '["directorios"]'.

        3) Si existe el fichero de configuración, lo lee y crea todos
           los directorios definidos en él.


        Returns
        -------
        None.

        """
        # Directorio de configuración: si no existe, se crea.
        if not self.__directory.exists():
            os.makedirs(self.__directory)
        # Fichero de configuración: si no existe, se crea.
        if not self.__config_file.exists():
            self.save(CONFIG_DEFAULT)
        # la variable interna que almacena la configuración; Read Only.
        self.__config = self.read()
        # Los directorios del usuario: si no existen, se crean.
        user_dirs = [CONFIG_DIR_IN, CONFIG_DIR_OUT]
        for item in self.__config[CONFIG_HEADER].values():
            if all(d in item for d in user_dirs):
                for d in user_dirs:
                    path = Path(item[d])
                    if not path.exists():
                        os.makedirs(path)

    @property
    def config_file(self):  # noqa
        return self.__config_file

    @property
    def config(self):  # noqa
        return self.__config

    def read(self) -> MutableMapping[str, Any]:
        """Leer la configuración.

        Accede al fichero de configuración usando los atributos que
        se definen en el constructor (self.path y self.filename)

        Returns
        -------
        MutableMapping[str, Any]

        """
        return toml.load(self.__config_file)

    def save(self, conf: Union[Dict, MutableMapping[str, Any]]) -> None:
        """Guarda la configuración en el formato TOML.

        Parameters
        ----------
        conf : Union[Dict, MutableMapping[str, Any]]
            La variable que hemos usado para definir la configuración
            de forma interna.

        Returns
        -------
        None

        """
        # DUDA: ¿Asignar la configuración además de salvarla en el fichero?
        # self.__config = conf

        # BUG? A veces toml.dump no escribe la cabecera ["directorios"]
        with open(self.__config_file, 'wt', encoding='utf-8') as fw:
            toml.dump(conf, fw)
