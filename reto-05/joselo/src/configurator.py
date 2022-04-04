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
# ¡Gracias @fpellicer!
from typing import Dict, Union, MutableMapping, Any


class Configurator:
    """Crear y manejar la configuración de la aplicación.
    """

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
        self.directory = path
        self.filename = config
        self.check()

    def check(self) -> None:
        """Chequea la integridad de la configuración.

        1) Si no existe el directorio de la configuración, lo crea.

        2) Si no existe el fichero de configuración, lo crea y escribe
           el nombre de la sección principal: '["directorios"]'.

        3) Si existe el fichero de configuración, lo lee y crea todos
           los directorios definidos en él.

           No verifica si los paths de esos directorios contienen cosas
           como ~/directorio, $HOME/directorio, ../../directorio, etc
           pero debería ya que en esos casos se crean paths relativos
           al directorio actual: ${PWD}/"~/directorio",
           ${PWD}/"$HOME/directorio", etc y no es eso lo que queremos.

        Returns
        -------
        None.

        """
        if not self.directory.exists():
            os.makedirs(self.directory)
        config_file = self.directory / self.filename
        if not config_file.exists():
            config_file.write_text('["directorios"]\n')
        conf = toml.load(config_file)
        for dirs in conf['directorios'].values():
            for path in [Path(d) for d in dirs.values()]:
                if not path.exists():
                    os.makedirs(path)

    def read(self) -> MutableMapping[str, Any]:
        config_file = self.directory / self.filename
        return toml.load(config_file)

    def save(self, conf: Union[Dict, MutableMapping[str, Any]]) -> None:
        config_file = self.directory / self.filename
        with open(config_file, 'w') as fw:
            toml.dump(conf, fw)
