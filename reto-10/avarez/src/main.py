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

from instagram_filters import InstagramFilter


def main():
    '''
    main method
    '''
    dir_path = "/home/andy/Downloads"
    file_name = "image"
    file_ext = "jpg"
    ifilter = InstagramFilter(dir_path, file_name, file_ext)
    while True:
        print("Filtros disponibles: ")
        ifilter.list_filters()
        try:
            msg = "Introduce el número de filtro a aplicar: "
            filter_index = int(input(msg))
            if filter_index in ifilter.filters_indexes():
                ifilter.set_filter(filter_index)
            else:
                continue
            break
        except ValueError:
            print("Se ha producido un error.")
    if ifilter.check():
        ifilter.execute()


if __name__ == "__main__":
    main()
