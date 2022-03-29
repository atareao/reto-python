#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from gi.repository import GLib


def main():
    download_dir = GLib.get_user_special_dir(
        GLib.UserDirectory.DIRECTORY_DOWNLOAD)

    print(f'Directorio de descargas: {download_dir}')

    jpgRegex = re.compile(r"[a-zA-Z]*[0-9]*.jp[e]?g", re.IGNORECASE)
    patronNum = re.compile(r"[0-9]", re.IGNORECASE)

    files = []

    for file in os.listdir(download_dir):
        if jpgRegex.search(file):
            files.append(file)

    for key, value in enumerate(files):
        if key % 2 == 0:
            value = "=> " + value

        if patronNum.search(value):
            print(key, value.lower())
        else:
            print(key, value.upper())


if __name__ == '__main__':
    main()
