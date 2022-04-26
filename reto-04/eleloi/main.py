from pathlib import Path
from configurator import Configurator
from utils import list_images


def main(app, config):
    path = Path.home() / app
    configurator = Configurator(path, config)
    data = configurator.read()
    list_images(str(Path(data.directorio)))


if __name__ == "__main__":
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
