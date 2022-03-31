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

from pathlib import Path
from xdg import xdg_config_home
from configurator import Configurator
from utils import list_images


def step1(path, config):
    Configurator(path, config)


def step2(path, config):
    conf = Configurator(path, config).read()
    for dir in conf['directorios'].values():
        print('\n== ', dir['in'], ' ==\n')
        for image in list_images(Path(dir['in'])):
            print(image.name)


def main(app, config):
    path = Path(xdg_config_home()) / app
    step1(path, config)
    step2(path, config)


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
