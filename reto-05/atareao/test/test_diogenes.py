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
import sys
import shutil
import unittest
import toml
from pathlib import Path
sys.path.append(os.path.join("../src"))
from configurator import Configurator
from utils import list_images

CONFIG_FILE = "diogenes.toml"

class DiogenesTest(unittest.TestCase):
    def setUp(self):
        if Path(CONFIG_FILE).exists():
            os.remove(CONFIG_FILE)
        with open(CONFIG_FILE, 'w') as file_writer:
            configuration = {"directorios": {}}
            toml.dump(configuration, file_writer)
        return super().setUp()

    def tearDown(self):
        if Path(CONFIG_FILE).exists():
            #os.remove(CONFIG_FILE)
            pass
        return super().tearDown()

    def test_caso1(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            dir_in1 = Path('.').absolute() / "dir1/in"
            dir_ou1 = Path('.').absolute() / "dir1/ou"
            def_conf = {'directorios': {}}
            def_conf['directorios']['1'] = {"in": str(dir_in1),
                                            "ou": str(dir_ou1)}
            toml.dump(def_conf, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        Configurator(Path('.').absolute(), CONFIG_FILE)
        # --- 👆 --- aquí va tu código --- 👆 ---
        self.assertTrue(dir_in1.exists())
        self.assertTrue(dir_ou1.exists())
        shutil.rmtree(dir_in1)
        shutil.rmtree(dir_ou1)

    def test_caso2(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            dir_in1 = Path('.').absolute() / "dir1/in"
            dir_ou1 = Path('.').absolute() / "dir1/ou"
            dir_in2 = Path('.').absolute() / "dir2/in"
            dir_ou2 = Path('.').absolute() / "dir2/ou"
            def_conf = {'directorios': {}}
            def_conf['directorios']['1'] = {"in": str(dir_in1),
                                            "ou": str(dir_ou1)}
            def_conf['directorios']['2'] = {"in": str(dir_in2),
                                            "ou": str(dir_ou2)}
            toml.dump(def_conf, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        Configurator(Path('.').absolute(), CONFIG_FILE)
        # --- 👆 --- aquí va tu código --- 👆 ---
        self.assertTrue(dir_in1.exists())
        self.assertTrue(dir_ou1.exists())
        shutil.rmtree(dir_in1)
        shutil.rmtree(dir_ou1)
        shutil.rmtree(dir_in2)
        shutil.rmtree(dir_ou2)

    def test_caso3(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            dir_in1 = Path('.').absolute() / "dir1/in"
            dir_ou1 = Path('.').absolute() / "dir1/ou"
            def_conf = {'directorios': {}}
            def_conf['directorios']['1'] = {"in": str(dir_in1),
                                            "ou": str(dir_ou1)}
            toml.dump(def_conf, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(Path('.').absolute(), CONFIG_FILE)
        file1 = dir_in1 / "image1.jpg"
        file1.touch()
        file2 = dir_in1 / "image2.jpg"
        file2.touch()
        file3 = dir_in1 / "image3.jpg"
        file3.touch()
        conf = configurator.read()
        images = list_images(Path(conf['directorios']['1']['in']))
        self.assertTrue(file1 in images)
        self.assertTrue(file2 in images)
        self.assertTrue(file3 in images)
        # --- 👆 --- aquí va tu código --- 👆 ---
        self.assertTrue(dir_in1.exists())
        self.assertTrue(dir_ou1.exists())
        shutil.rmtree(dir_in1)
        shutil.rmtree(dir_ou1)


if __name__ == '__main__':
    unittest.main()


