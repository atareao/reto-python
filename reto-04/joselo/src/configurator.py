#!/usr/bin/env python3
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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
import os
import toml

from xdg import xdg_config_home


class Configurator(object):

    def __init__(self, path, config):
        self._config_dir = path
        if not self._config_dir.exists():
            os.makedirs(self._config_dir)
        self._config_file = self._config_dir / config
        self.setup_conf()

    def read(self):
        return toml.load(self._config_file)

    def setup_conf(self, directorio=None):

        if directorio is None:
            try:
                xdg_config_file = xdg_config_home() / "user-dirs.dirs"
                user_dirs = toml.load(xdg_config_file)
                directorio = os.path.expandvars(user_dirs["XDG_DOWNLOAD_DIR"])
            except (FileNotFoundError, KeyError) as exception:
                msg = f"""\
No se ha podido encontrar un directorio válido en los ficheros de configuración
{xdg_config_file} y/o {self._config_file}

Abortando...
"""
                raise RuntimeError(msg) from exception

        with open(self._config_file, 'w') as fw:
            toml.dump({'directorio': directorio}, fw)
