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
from utils import list_images, copy, move

def set_filter(dir):
    if 'filter' in dir:
        filtro=dir['filter'][1:]        
    else:
        filtro=''
    return filtro
    
def to_do(data):
    for dir in data['directorios'].values():
        print('===', dir['in'], '===')
        list_images(Path(dir['in']))
        filtro=set_filter(dir)
        if 'accion' in dir:
            for n in range(len(dir['accion'])):
                if dir['accion'][n] == 'copy':
                    copy(Path(dir['in']), Path(dir['out']), filtro)
                elif dir['accion'][n] == 'move':
                    move(Path(dir['in']), Path(dir['out']), filtro)
                elif dir['accion'][n] == 'none':
                    print('No se hace Nada en este Caso')

def main(app, config):
    path = Path(xdg_config_home()) / app
    configurator = Configurator(path, config)
    data = configurator.read()
    to_do(data)

if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)