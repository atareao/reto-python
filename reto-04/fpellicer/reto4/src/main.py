from pathlib import Path

from xdg import xdg_config_home

from configurator import Configurator
from utils import list_images


def main(app: str, filename: str):
    path = Path(xdg_config_home(), app)
    configurator = Configurator(path, filename)
    config_data = configurator.read()
    list_images(Path(config_data["directory"]))


if __name__ == "__main__":
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
