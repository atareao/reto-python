from pathlib import Path
import os.path
from configurator import Configurator
from utils import list_images


def main(app, config):
    path = os.path.join(os.path.expanduser("~"),
                        '.config', app)
    configurator = Configurator(path, config)
    data = configurator.read()
    list_images(Path(data['directorio']))


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
