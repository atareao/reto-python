# Python 3.10.2 UTF-8
# Para el "reto-python" de Lorenzo Carbonell <a.k.a. atareao>

from pathlib import Path
import os.path
from configurator import Configurator
from utils import list_images


def step1(path, tomlconfig):
    """
    Inicia Configurator y devuelve su lectura.
    """
    Configurator(path, tomlconfig)
    conf = Configurator(path, tomlconfig).read()
    print(conf)
    return conf


def step2(dictio):
    """
    Imprime directorios e inicia lista de imágenes.
    """
    for folder in dictio['directorios'].values():
        print('=====', folder['in'], '=====')
        list_images(Path(folder['in']))


def main(app, tomlconf):
    """
    Inicia Diogenes.
    """
    path = os.path.join(os.path.expanduser("~"),
                        '.config', app)

    step2(step1(path, tomlconf))


if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
