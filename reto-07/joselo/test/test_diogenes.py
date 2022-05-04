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


CONFIG_APP = Path("~/.config/diogenes").expanduser()
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
    # "7": {
    #     CONFIG_DIR_IN: str(TEST_ROOT / "ImágenesIn7"),
    #     CONFIG_DIR_OUT: str(TEST_ROOT / "ImágenesOut7"),
    #     "actions": ["cosa"],
    #     "filter": "*"}
    }}

FILES = ["image.jpg", "image.svg", "image.png", "text.txt"]


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


class DiogenesTest(unittest.TestCase):

    def setUp(self):
        config_file = CONFIG_APP / CONFIG_FILE
        if Path(config_file).exists():
            os.remove(config_file)
        with open(config_file, 'wt', encoding='utf-8') as file_writer:
            configuration = {CONFIG_HEADER: {}}
            toml.dump(configuration, file_writer)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_configurator(self):
        config_file = CONFIG_APP / CONFIG_FILE
        with open(config_file, 'wt', encoding='utf-8') as file_writer:
            toml.dump(CONFIG, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(CONFIG_APP, CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        for item in config[CONFIG_HEADER].values():
            dir_in = Path(item[CONFIG_DIR_IN])
            dir_out = Path(item[CONFIG_DIR_OUT])
            self.assertTrue(dir_in.exists())
            self.assertTrue(dir_out.exists())

    def test_actions(self):
        config_file = CONFIG_APP / CONFIG_FILE
        with open(config_file, 'wt', encoding='utf-8') as file_writer:
            toml.dump(CONFIG, file_writer)
        # --- 👇 --- aquí va tu código --- 👇 ---
        configurator = Configurator(CONFIG_APP, CONFIG_FILE)
        config = configurator.read()
        # --- 👆 --- aquí va tu código --- 👆 ---
        for item in config[CONFIG_HEADER].values():
            dir_in = Path(item[CONFIG_DIR_IN])
            dir_out = Path(item[CONFIG_DIR_OUT])
            self.assertTrue(dir_in.exists())
            self.assertTrue(dir_out.exists())
            for name in FILES:
                file = dir_in / name
                file.touch()
                self.assertTrue(file.exists())
            for name in FILES:
                self.assertIn(dir_in / name, dir_in.iterdir())
                self.assertNotIn(dir_out / name, dir_out.iterdir())
            filtro = glob_factory(item['filter'])
            for action_name in item['actions']:
                if action_name == "none":
                    all_files_input_inicial = \
                        set(p.name for p in dir_in.iterdir())
                    all_files_output_inicial = \
                        set(p.name for p in dir_out.iterdir())
        # --- 👇 --- aquí va tu código --- 👇 ---
                action[action_name](dir_in, dir_out, fltr=filtro)
        # --- 👆 --- aquí va tu código --- 👆 ---
                if action_name == 'none':
                    all_files_input = set(p.name for p in dir_in.iterdir())
                    all_files_output = set(p.name for p in dir_out.iterdir())
                    self.assertTrue(
                        all_files_input_inicial == all_files_input)
                    self.assertTrue(
                        all_files_output_inicial == all_files_output)
                elif action_name == 'move':
                    all_files = set(p.name for p in dir_in.iterdir())
                    sel_files = filtro(all_files)
                    nosel_files = all_files - sel_files
                    for elem in sel_files:
                        elem_in = dir_in / elem
                        elem_out = dir_out / elem
                        self.assertNotIn(elem_in, dir_in.iterdir())
                        self.assertIn(elem_out, dir_out.iterdir())
                    for elem in nosel_files:
                        elem_in = dir_in / elem
                        elem_out = dir_out / elem
                        self.assertIn(elem_in, dir_in.iterdir())
                        self.assertNotIn(elem_out, dir_out.iterdir())
                else:  # action_name == 'copy':
                    all_files = set(p.name for p in dir_in.iterdir())
                    sel_files = filtro(all_files)
                    nosel_files = all_files - sel_files
                    for elem in sel_files:
                        elem_in = dir_in / elem
                        elem_out = dir_out / elem
                        self.assertIn(elem_in, dir_in.iterdir())
                        self.assertIn(elem_out, dir_out.iterdir())
                    for elem in nosel_files:
                        elem_in = dir_in / elem
                        elem_out = dir_out / elem
                        self.assertIn(elem_in, dir_in.iterdir())
                        self.assertNotIn(elem_out, dir_out.iterdir())


if __name__ == '__main__':
    mkdirs()
    unittest.main()
