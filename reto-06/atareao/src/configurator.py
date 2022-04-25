#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>

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

import os
import shutil
from pathlib import Path
import toml


class Configurator:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.check()

    def check(self):
        if not self.path.exists():
            os.makedirs(self.path)
        config_file = self.path / self.filename
        if config_file.exists():
            conf = self.read()
            print(conf)
            if 'directorios' not in conf:
                conf = {'directorios': []}
                self.save(conf)
            else:
                for data in conf['directorios'].values():
                    if 'in' in data:
                        dir_in = Path(data['in'])
                        if not dir_in.exists():
                            os.makedirs(dir_in)
                    if 'out' in data:
                        dir_ou = Path(data['out'])
                        if not dir_ou.exists():
                            os.makedirs(dir_ou)

    def read(self):
        config_file = self.path / self.filename
        return toml.load(config_file)

    def save(self, conf):
        config_file = self.path / self.filename
        with open(config_file, 'w') as file_writer:
            toml.dump(conf, file_writer)

    def do_action(self):
        conf = self.read()
        for data in conf['directorios'].values():
            if 'in' in data and 'out' in data and 'action' in data:
                dir_in = Path(data['in'])
                dir_ou = Path(data['out'])
                action = data['action']
                for item in dir_in.iterdir():
                    if item.is_file():
                        dest = dir_ou / item.name
                        if action == 'move':
                            shutil.move(item, dest)
                        elif action == 'copy':
                            shutil.copy(item, dest)
