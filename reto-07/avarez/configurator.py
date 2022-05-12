#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 14 April 2022

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
from os.path import exists
from pathlib import Path
import toml
from xdg import xdg_config_home
import app_globals


class Configurator:
    '''
    CONFIGURATOR
    '''
    def __init__(self):
        self.path_config_dir = Path(xdg_config_home()) / app_globals.APP
        self.path_config_file = Path(xdg_config_home()) / app_globals.APP \
            / app_globals.CONFIG
        if not exists(self.path_config_dir):
            os.makedirs(self.path_config_dir)
        if not exists(self.path_config_file):
            self.create_file()

    def read(self):
        '''
        DEVUELVE UN DICCIONARIO CON EL CONTENIDO DEL FICHERO TOML
        '''
        return toml.load(self.path_config_file)

    def create_file(self):
        '''
        CREA FICHERO TOML
        '''
        with open(self.path_config_file, "w", encoding="utf-8") \
             as self.file_pipe:
            self.cfg_string = """[directorios]"""
            self.cfg_string_parsed = toml.loads(self.cfg_string)
            toml.dump(self.cfg_string_parsed, self.file_pipe)
