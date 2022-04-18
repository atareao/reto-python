#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Lorenzo Carbonell <a.k.a. atareao>
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
import toml
import unittest

sys.path.append(os.path.join("../src"))
from configurator import Configurator  # noqa: E402
from utils import action               # noqa: E402


CONFIG_FILE = "diogenes.toml"

CONFIG_HEADER = Configurator.HEADER
DIRS_IN = Configurator.DIR_INPUT
DIRS_OUT = Configurator.DIR_OUTPUT

TEST_ROOT = Path('.').absolute()

CONFIG = {CONFIG_HEADER: {
    "1": {
        DIRS_IN: "home/lorenzo/ImágenesIn1",
        DIRS_OUT: "home/lorenzo/ImágenesOut1",
        "action": "none"},
    "2": {
        DIRS_IN: "home/lorenzo/ImágenesIn2",
        DIRS_OUT: "home/lorenzo/ImágenesOut2",
        "action": "move"},
    "3": {
        DIRS_IN: "home/lorenzo/ImágenesIn3",
        DIRS_OUT: "home/lorenzo/ImágenesOut3",
        "action": "copy"}}}

IMAGES_LIST = ["image.jpg", "image.svg", "image.png", "image.gif"]


class DiogenesTest(unittest.TestCase):

    def setUp(self):
        if Path(CONFIG_FILE).exists():
            os.remove(CONFIG_FILE)
        with open(CONFIG_FILE, 'w') as file_writer:
            configuration = {CONFIG_HEADER: {}}
            toml.dump(configuration, file_writer)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_configurator(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            toml.dump(CONFIG, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(Path('.').absolute(), CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        for n in (1, 2, 3):
            dir_in = TEST_ROOT / config[CONFIG_HEADER][str(n)][DIRS_IN]
            dir_out = TEST_ROOT / config[CONFIG_HEADER][str(n)][DIRS_OUT]
            self.assertTrue(dir_in.exists())
            self.assertTrue(dir_out.exists())
        for item in TEST_ROOT.iterdir():
            if item.is_dir():
                shutil.rmtree(item)

    def test_actions(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            toml.dump(CONFIG, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(TEST_ROOT, CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        for n in (1, 2, 3):
            item = config[CONFIG_HEADER][str(n)]
            dir_in = TEST_ROOT / item[DIRS_IN]
            dir_out = TEST_ROOT / item[DIRS_OUT]
            self.assertTrue(dir_in.exists())
            self.assertTrue(dir_out.exists())
            for name in IMAGES_LIST:
                file = dir_in / name
                file.touch()
                self.assertTrue(file.exists())
            for name in IMAGES_LIST:
                self.assertIn(dir_in / name, dir_in.iterdir())
                self.assertNotIn(dir_out / name, dir_out.iterdir())
        # --- 👇 --- aquí va tu código --- 👇 ---
            action(dir_in, dir_out, action=item["action"])
        # --- 👆 --- aquí va tu código --- 👆 ---
            if item['action'] == 'none':
                for name in IMAGES_LIST:
                    self.assertIn(dir_in / name, dir_in.iterdir())
                    self.assertNotIn(dir_out / name, dir_out.iterdir())
            elif item['action'] == 'move':
                for name in IMAGES_LIST:
                    self.assertNotIn(dir_in / name, dir_in.iterdir())
                    self.assertIn(dir_out / name, dir_out.iterdir())
            else:  # item['action'] == 'copy':
                for name in IMAGES_LIST:
                    self.assertIn(dir_in / name, dir_in.iterdir())
                    self.assertIn(dir_out / name, dir_out.iterdir())
        for item in TEST_ROOT.iterdir():
            if item.is_dir():
                shutil.rmtree(item)


if __name__ == '__main__':
    unittest.main()
