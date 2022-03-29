"""Reto 04"""
from xdg import xdg_config_home
from pathlib import Path
from configurator import Configurator
from utils import list_images

def main(app, config):
    """Función principal de la app"""

    path = Path(xdg_config_home()) / app
    configurator = Configurator(path, config)
    data = configurator.read()
    list_images(Path(data['directorio']))

if __name__ == '__main__':

    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
