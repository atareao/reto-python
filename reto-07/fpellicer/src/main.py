from pathlib import Path

from xdg import xdg_config_home

from configurator import Configurator
from utils import list_images, actions


def list_in(configurator: Configurator) -> None:
    """
    Lista las imágenes contenidas en las rutas del archivo de configuración
    correspondientes a la clave "in".
    """
    conf_data = configurator.read()
    for value in conf_data["directories"].values():
        path = Path(value.get("in", False))
        if path is not False:
            list_images(path)


def do_actions(configurator: Configurator) -> None:
    """
    Realiza las acciones asignadas en el archivo de configuración
    a cada entrada con la etiqueta "action".
    """
    conf_data = configurator.read()
    for value in conf_data["directories"].values():
        actions_ = value.get("actions", False)
        if actions_:
            src = Path(value["in"])
            dst = Path(value["out"])
            filter_ = value["filter"]
            actions(src, dst, actions_, filter_)


def main(app: str, filename: str):
    path = Path(xdg_config_home(), app)
    configurator = Configurator(path, filename)
    do_actions(configurator)


if __name__ == "__main__":
    APP = "diogenes"
    config = f"{APP}.toml"
    main(APP, config)
