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
from pathlib import Path

def get_config_dir():
    return os.environ['XDG_CONFIG_DIR'] if 'XDG_CONFIG_DIR' in os.environ \
            else Path.home() / '.config'

def get_download_dir():
    if 'XDG_DOWNLOAD_DIR' in os.environ:
        return os.environ['XDG_DOWNLOAD_DIR']
    config_dir = Path(get_config_dir())
    user_dirs_file = config_dir / 'user-dirs.dirs'
    with open(user_dirs_file, 'r') as fr:
        for line in fr.readlines():
            if line.startswith('XDG_DOWNLOAD_DIR'):
                directory = line.split("=")[1].replace("\"",'')
                download_dir  = directory.replace("$HOME", str(Path.home()))[:-1]
                return Path(download_dir)
    return None

def main():
    try:
        download_dir = get_download_dir()
        if download_dir is not None and isinstance(download_dir, Path) and \
                download_dir.is_dir():
            print(f"\nDirectorio: {download_dir}\n")
            for afile in [x for x in download_dir.iterdir() if not x.is_dir()]:
                print(afile.name)
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()
