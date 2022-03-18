#  Copyright (c) 2022. LESCLAZ.
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  #
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
import configparser
import mimetypes
import os
import re
import sys

from xdg.BaseDirectory import xdg_config_home


def get_download_dir():
    config = configparser.ConfigParser()
    try:
        with open(os.path.join(xdg_config_home, "user-dirs.dirs")) as f:
            config.read_string(f'[XDG_USER_DIR]\n{f.read()}'
                               .replace('$HOME', os.path.expanduser("~"))
                               .replace('"', ''))
        return config["XDG_USER_DIR"]["XDG_DOWNLOAD_DIR"]
    except FileNotFoundError:
        print("Este Usuario no tiene directorio de descargas")
        sys.exit()


def files_in_download_dir():
    return [file for file in os.listdir(get_download_dir()) if
            os.path.isfile(os.path.join(get_download_dir(), file))]


def main():
    jpegs = [file for file in files_in_download_dir() if
             mimetypes.guess_type(os.path.join(get_download_dir(),
                                               file))[0] == 'image/jpeg']
    print(f'\nDirectorio: {get_download_dir()}\n')
    for i, jpeg in enumerate(jpegs):
        jpeg = jpeg.lower() if re.findall('[0-9]+', jpeg) else jpeg.upper()
        print(f'{i} => {jpeg}' if i % 2 == 0 else f'{i} {jpeg}')


if __name__ == '__main__':
    main()
