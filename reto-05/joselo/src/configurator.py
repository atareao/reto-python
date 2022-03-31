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
# from xdg import XDG_CONFIG_HOME


class Configurator:
    """Clase Configurator: crear y manejar la configuración de Diogenes.
    """

    def __init__(self, path: Path, config: str) -> None:
        """Constructor.

        :param path: La ruta al directorio de la configuración.
        :param config: El nombre del fichero de configuración.
        """
        self.directory = path
        self.filename = config
        self.check()

    def check(self):
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

    def read(self):
        config_file = self.directory / self.filename
        return toml.load(config_file)

    def save(self, conf):
        config_file = self.directory / self.filename
        with open(config_file, 'w') as fw:
            toml.dump(conf, fw)
