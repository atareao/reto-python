#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 14 May 2022

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

from PIL import Image, ImageOps


class GrayscaleImage():
    '''
    GrayscaleImage class
    '''
    def __init__(self,
                 input_image_filename,
                 output_image_filename,
                 image_format):
        '''
        GrayscaleImage init method
        '''
        self.image = Image.open(input_image_filename)
        self.image_format = image_format
        self.grayscaled_image_filename = output_image_filename

    def check(self):
        '''
        GrayscaleImage check method
        '''
        if self.image.format == self.image_format:
            return True
        else:
            return False

    def execute(self):
        '''
        GrayscaleImage execute method
        '''
        grayscaled_image = ImageOps.grayscale(self.image)
        grayscaled_image.save(self.grayscaled_image_filename,
                              self.image_format)
