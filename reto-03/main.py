#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__license__ = """
MIT License

Copyright (c) 2022 JLNC.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import os.path as osp
import toml
import mimetypes

from xdg.BaseDirectory import xdg_config_home
from easyansi import screen  # pip install --user easyansi


mimetypes.init()


XDG_USER_DIRS = osp.join(xdg_config_home, 'user-dirs.dirs')
DGNS_CONF_DIR = osp.join(xdg_config_home, 'diogenes')
DGNS_CONF_FILE = osp.join(DGNS_CONF_DIR, 'diogenes.conf')


def get_user_dirs():
    def f(x): return x.replace("$HOME", osp.expanduser('~'))
    ud = toml.load(XDG_USER_DIRS)
    ud = {k: f(ud[k]) for k in ud.keys()}
    return ud


def input_dgns_dir():
    pass


def main():
    os.makedirs(DGNS_CONF_DIR, mode=0o755, exists_ok=True)
    dgns_dir = input_dgns_dir()
    screen.clear()
    print(f"\n{dgns_dir}\n{len(dgns_dir) * '='}\n")
    for file in os.listdir(dgns_dir):
        if mimetypes.guess_type(file)[0] == "image/jpeg":
            print(file)


if __name__ == "__main__":
    main()
