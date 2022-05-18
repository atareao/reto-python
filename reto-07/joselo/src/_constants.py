#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""atareao/reto-python, reto-07: constantes."""

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

from pathlib import Path

# APP = "diogenes"
# config = f"{APP}.conf"

CONFIG_APP = Path("~/.config/diogenes").expanduser()
TEST_ROOT = Path('./diogenes').absolute()
CONFIG_FILE = "diogenes.conf"

CONFIG_HEADER = "directorios"
CONFIG_DIR_IN = "in"
CONFIG_DIR_OUT = "out"
CONFIG_DEFAULT = {CONFIG_HEADER: {}}
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
        "filter": ""}}}

FILES = ["image.jpg", "image.svg", "image.png", "text.txt"]
