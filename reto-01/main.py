#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from gi.repository import GLib


def main():
    download_dir = GLib.get_user_special_dir(
        GLib.UserDirectory.DIRECTORY_DOWNLOAD)

    print(f'Directorio de descargas: {download_dir}')

    for archivo in os.listdir(download_dir):
        print(archivo)


if __name__ == '__main__':
    main()
