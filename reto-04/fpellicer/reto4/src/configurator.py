from pathlib import Path
from typing import Dict, Union, MutableMapping, Any

import toml


class Configurator:
    """
    Lee y escribe datos de los archivos de configuración TOML
    indicando la ruta y el nombre del archivo.
    """
    def __init__(self, path: Path, filename: str) -> None:
        self.filename = filename
        self.path = path

    def read(self) -> MutableMapping[str, Any]:
        """
        Retorna los datos del archivo de configuración indicado.
        Si no existe, retorna los datos por defecto.
        """
        path = self.path.joinpath(self.filename)
        try:
            with open(path) as fd:
                conf = toml.load(fd)
            return conf
        except FileNotFoundError:
            toml_string = (f"title = 'diogenes configuration file.'\n"
                           f"directory = '{Path().home()}/Descargas'\n")

            conf = toml.loads(toml_string)
            self.write(conf)
            return conf

    def write(self, data: Union[Dict, MutableMapping[str, Any]]) -> None:
        """
        Escribe en contenido de 'data' en un archivo de configuración TOML.
        """
        path = self.path.joinpath(self.filename)
        try:
            self.path.mkdir(parents=True, exist_ok=True)
            path.write_text(toml.dumps(data))
        except IOError as e:
            raise e

    def __str__(self) -> str:
        """
        Retorna el contenido del archivo de configuración.
        """
        return toml.dumps(self.read())
