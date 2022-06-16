#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 27 May 2022

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
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
from PIL import Image
import pilgram


class InstagramFilter():
    '''
    instagram image class
    '''
    def __init__(self, dir_path, file_name, file_ext):
        '''
        init method
        '''
        self.filters = {1: "_1977",
                        2: "aden",
                        3: "brannan",
                        4: "brooklyn",
                        5: "clarendon",
                        6: "earlybird",
                        7: "gingham",
                        8: "hudson",
                        9: "inkwell",
                        10: "kelvin",
                        11: "lark",
                        12: "lofi",
                        13: "maven",
                        14: "mayfair",
                        15: "moon",
                        16: "nashville",
                        17: "perpetua",
                        18: "reyes",
                        19: "rise",
                        20: "slumber",
                        21: "stinson",
                        22: "toaster",
                        23: "valencia",
                        24: "walden",
                        25: "willow",
                        26: "xpro2"}
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_ext = file_ext
        self.filter_name = None

    def list_filters(self):
        '''
        list filters method
        '''
        for filter_index in self.filters.keys():
            print(f"{filter_index:2d} : {self.filters[filter_index]}")

    def set_filter(self, filter_index):
        '''
        set filter method
        '''
        self.filter_name = self.filters[filter_index]

    def filters_indexes(self):
        '''
        filters indexes method
        '''
        return self.filters.keys()

    def check(self):
        '''
        check method
        '''
        if Path(f"{self.dir_path}/{self.file_name}.{self.file_ext}"):
            print(f"In: {self.dir_path}/{self.file_name}.{self.file_ext}")
            if self.filter_name:
                print(f"Filtro: {self.filter_name}")
                return True
        return False

    def execute(self):
        '''
        execute method
        '''
        in_img = f"{self.dir_path}/{self.file_name}.{self.file_ext}"
        out_img = f"{self.dir_path}/{self.file_name}.{self.filter_name}.{self.file_ext}"
        print(f"Out: {out_img}")
        img = Image.open(in_img)
        if self.filter_name == "_1977":  # 1
            pilgram._1977(img).save(out_img)
        if self.filter_name == "aden":  # 2
            pilgram.aden(img).save(out_img)
        if self.filter_name == "brannan":  # 3
            pilgram.brannan(img).save(out_img)
        if self.filter_name == "brooklyn":  # 4
            pilgram.brooklyn(img).save(out_img)
        if self.filter_name == "clarendon":  # 5
            pilgram.clarendon(img).save(out_img)
        if self.filter_name == "earlybird":  # 6
            pilgram.earlybird(img).save(out_img)
        if self.filter_name == "gingham":  # 7
            pilgram.gingham(img).save(out_img)
        if self.filter_name == "hudson":  # 8
            pilgram.hudson(img).save(out_img)
        if self.filter_name == "inkwell":  # 9
            pilgram.inkwell(img).save(out_img)
        if self.filter_name == "kelvin":  # 10
            pilgram.kelvin(img).save(out_img)
        if self.filter_name == "lark":  # 11
            pilgram.lark(img).save(out_img)
        if self.filter_name == "lofi":  # 12
            pilgram.lofi(img).save(out_img)
        if self.filter_name == "maven":  # 13
            pilgram.maven(img).save(out_img)
        if self.filter_name == "mayfair":  # 14
            pilgram.mayfair(img).save(out_img)
        if self.filter_name == "moon":  # 15
            pilgram.moon(img).save(out_img)
        if self.filter_name == "nashville":  # 16
            pilgram.nashville(img).save(out_img)
        if self.filter_name == "perpetua":  # 17
            pilgram.perpetua(img).save(out_img)
        if self.filter_name == "reyes":  # 18
            pilgram.reyes(img).save(out_img)
        if self.filter_name == "rise":  # 19
            pilgram.rise(img).save(out_img)
        if self.filter_name == "slumber":  # 20
            pilgram.slumber(img).save(out_img)
        if self.filter_name == "stinson":  # 21
            pilgram.stinson(img).save(out_img)
        if self.filter_name == "toaster":  # 22
            pilgram.toaster(img).save(out_img)
        if self.filter_name == "valencia":  # 23
            pilgram.valencia(img).save(out_img)
        if self.filter_name == "walden":  # 24
            pilgram.walden(img).save(out_img)
        if self.filter_name == "willow":  # 25
            pilgram.willow(img).save(out_img)
        if self.filter_name == "xpro2":  # 26
            pilgram.xpro2(img).save(out_img)
