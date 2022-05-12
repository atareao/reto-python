from pathlib import Path
from typing import Dict, Union, MutableMapping

import toml


class Configurator:
    """
    Lee y escribe datos de los archivos de configuración TOML
    indicando la ruta y el nombre del archivo.
    """

    def __init__(self, path: Path, filename: str) -> None:
        self.filename = filename
        self.path = path
        self.check()

    def check(self) -> None:
        """
        Crea el archivo de configuración y su directorio si no existen y
        añade la entrada "directories" vacía.

        Comprueba si existen los directorios del archivo de configuración
        asignados a "in" y a "out". En caso de no existir se generan.
        """
        if not self.path.exists():
            self.path.mkdir(parents=True, exist_ok=True)

        cfg_file = self.path / self.filename
        if not cfg_file.exists():
            conf = {"directories": {}}
            self.write(conf)

        conf_data = self.read()
        if "directories" not in conf_data:
            conf = {"directories": {}}
            self.write(conf)
        else:
            for value in conf_data["directories"].values():
                for k, v in value.items():
                    if k == "in" or k == "out":
                        path = Path(v)
                        if not Path(path).exists():
                            path.mkdir(parents=True)

    def read(self) -> Union[Dict, MutableMapping]:
        """
        Retorna los datos del archivo de configuración indicado.
        Si no existe, retorna los datos por defecto.
        """
        try:
            cfg_file = self.path / self.filename
            return toml.load(cfg_file)
        except IOError as e:
            raise e

    def write(self, data: Dict) -> None:
        """
        Escribe en contenido de 'data' en un archivo de configuración TOML.
        """
        try:
            conf_file = self.path.joinpath(self.filename)
            with conf_file.open("w") as fd:
                toml.dump(data, fd)
        except IOError as e:
            raise e

    def __str__(self) -> str:
        """
        Retorna el contenido del archivo de configuración.
        """
        return toml.dumps(self.read())
