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
import mimetypes
import os

import toml
from xdg.BaseDirectory import xdg_config_home


def get_downloads_dir():
    """
    Localiza y devuelve la ruta hacia la carpeta de descargas del usuario
    que ejecuta la app.
    """
    path_to_user_dirs = os.path.join(xdg_config_home, "user-dirs.dirs")
    if os.path.exists(path_to_user_dirs):
        with open(path_to_user_dirs) as conf_dirs:
            user_dirs = toml.load(conf_dirs)
            return os.path.join(os.path.expanduser("~"),
                                user_dirs["XDG_DOWNLOAD_DIR"]
                                .replace("$HOME/", ""))


def list_images(dir_to_list):
    """
    Lista los archivos de imagen JPEG dentro del directorio pasado como
    parámetro.
    """
    for file in [file for file in os.listdir(dir_to_list)
                 if os.path.isfile(
            os.path.join(dir_to_list, file)) and
                    mimetypes.guess_type(os.path.join(
                        dir_to_list, file))[0] == 'image/jpeg']:
        print(file)
