#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Author: Andrés Pérez <a.k.a. avarez>
# Copyright (c)
# Created: 11 June 2022

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


from file_ops import Copy, Remove


def main():
    '''
    (None) -> None
    main method
    '''
    in_filepath = "/home/andy/Downloads/file.jpg"
    out_filepath = "/home/andy/Downloads/file1.jpg"
    copy_op = Copy(in_filepath, out_filepath)
    if copy_op.check():
        copy_op.execute()
    out_filepath = "/home/andy/Downloads/file2.jpg"
    copy_op = Copy(in_filepath, out_filepath)
    if copy_op.check():
        copy_op.execute()
    remove_op = Remove(out_filepath)
    if remove_op.check():
        remove_op.execute()


if __name__ == "__main__":
    main()

