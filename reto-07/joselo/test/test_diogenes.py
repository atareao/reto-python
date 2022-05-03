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

sys.path.append(os.path.join("../src"))  # noqa
from configurator import (
    Configurator,
    CONFIG_HEADER,
    CONFIG_DIR_IN,
    CONFIG_DIR_OUT,)
from utils import action, glob_factory

TEST_ROOT = Path('./diogenes').absolute()
CONFIG_FILE = "diogenes.conf"

CONFIG = {CONFIG_HEADER: {
    "1": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn1"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut1"),
        "actions": ["copy", "move"],
        "filter": "*.png"},
    "2": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn2"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut2"),
        "actions": ["move"],
        "filter": "*.svg"},
    "3": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn3"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut3"),
        "actions": ["copy", "none"],
        "filter": "*.txt"},
    "4": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn4"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut4"),
        "actions": [],
        "filter": "*"},
    "5": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn5"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut5"),
        "actions": ["move"],
        "filter": ""},
    # "6": {
    #     CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn6"),
    #     CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut6"),
    #     "actions": None,
    #     "filter": "*"},
    "7": {
        CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn7"),
        CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut7"),
        "actions": ["cosa"],
        "filter": "*"}}}

IMAGES_LIST = ["image.jpg", "image.svg", "image.png", "texto.txt"]


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
        configurator = Configurator(TEST_ROOT, CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        for item in config.values():
            dir_in = TEST_ROOT / item[CONFIG_DIR_IN]
            dir_out = TEST_ROOT / item[CONFIG_DIR_OUT]
            self.assertTrue(dir_in.exists())
            self.assertTrue(dir_out.exists())
        for item in TEST_ROOT.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                os.remove(item)

    def test_actions(self):
        with open(CONFIG_FILE, 'w') as file_writer:
            toml.dump(CONFIG, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(TEST_ROOT, CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        print(config)
        for item in config.values():
            print(item)
            dir_in = TEST_ROOT / item[CONFIG_DIR_IN]
            dir_out = TEST_ROOT / item[CONFIG_DIR_OUT]
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
            filtro = glob_factory(item['filter'])
            for action_name in item['actions']:
                action[action_name](dir_in, dir_out, fltr=filtro)
        # --- 👆 --- aquí va tu código --- 👆 ---
                if action_name == 'none':
                    for name in IMAGES_LIST:
                        self.assertIn(dir_in / name, dir_in.iterdir())
                        self.assertNotIn(dir_out / name, dir_out.iterdir())
                elif action_name == 'move':
                    for name in IMAGES_LIST:
                        self.assertNotIn(dir_in / name, dir_in.iterdir())
                        self.assertIn(dir_out / name, dir_out.iterdir())
                else:  # action_name == 'copy':
                    for name in IMAGES_LIST:
                        self.assertIn(dir_in / name, dir_in.iterdir())
                        self.assertIn(dir_out / name, dir_out.iterdir())
        for item in TEST_ROOT.iterdir():
            if item.is_dir():
                shutil.rmtree(item)


if __name__ == '__main__':
    unittest.main()
