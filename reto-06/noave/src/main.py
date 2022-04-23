# Python 3.10.2 UTF-8
# Para el "reto-python" de Lorenzo Carbonell <a.k.a. atareao>

from pathlib import Path
import os.path
from configurator import Configurator
import utils


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
    for folder in dictio["directorios"].values():
        print("=====", folder["in"], "=====")
        utils.list_images(Path(folder["in"]))


def step3(dictio):
    """Lee las acciones del archivo de configuración
    y las ejecuta."""
    for folder in dictio["directorios"].values():
        action = folder["action"]
        if action == "copy":
            utils.copy(folder["in"], folder["out"])
        elif action == "move":
            utils.move(folder["in"], folder["out"])


def main(app, tomlconf):
    """
    Inicia Diogenes.
    """
    path = os.path.join(os.path.expanduser("~"), ".config", app)
    dictio = step1(path, tomlconf)
    step2(dictio)
    step3(dictio)


if __name__ == "__main__":
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
