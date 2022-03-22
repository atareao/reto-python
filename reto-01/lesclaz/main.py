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

import sys
import os
import configparser

from xdg.BaseDirectory import xdg_config_home

if __name__ == "__main__":
    config = configparser.ConfigParser()
    try:
        with open(os.path.join(xdg_config_home, "user-dirs.dirs")) as f:
            config.read_string(f'[XDG_USER_DIR]\n{f.read()}'
                               .replace('$HOME', os.path.expanduser("~"))
                               .replace('"', ''))
        download_dir = config["XDG_USER_DIR"]["XDG_DOWNLOAD_DIR"]

        print(f'\nDirectorio: {download_dir}\n')
        for file in [file for file in os.listdir(download_dir)
                     if os.path.isfile(os.path.join(download_dir, file))]:
            print(file)

    except FileNotFoundError:
        print("Este Usuario no tiene directorio de descargas")
        sys.exit()
