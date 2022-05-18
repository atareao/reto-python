#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Diogenes, reto 07: mkdirs(aux)."""

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

import os
from pathlib import Path
import shutil
import sys

sys.path.append(os.path.join("../src"))  # noqa
from _constants import (
    CONFIG,
    CONFIG_APP,
    CONFIG_DIR_IN,
    CONFIG_DIR_OUT,
    CONFIG_FILE,
    CONFIG_HEADER,
    FILES,
    TEST_ROOT,)
from configurator import Configurator


def mkdirs():  # noqa
    if TEST_ROOT.exists():
        shutil.rmtree(TEST_ROOT)
    configurator = Configurator(TEST_ROOT, CONFIG_FILE)
    configurator.save(CONFIG)
    config = configurator.read()
    shutil.copy(TEST_ROOT / CONFIG_FILE, CONFIG_APP)
    for item in config[CONFIG_HEADER].values():
        for dir_ in (CONFIG_DIR_IN, CONFIG_DIR_OUT):
            path = Path(item[dir_])
            os.makedirs(path)
            if dir_ == CONFIG_DIR_IN:
                for f in FILES:
                    file = path / f
                    file.touch()


if __name__ == '__main__':
    mkdirs()
