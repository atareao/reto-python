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
        self.check_directories()

    def check(self) -> None:
        """
        Comprueba si existe el archivo de configuración. En caso de no existir,
        crea uno nuevo con los ajustes predeterminados.
        """
        if not self.path.exists():
            self.path.mkdir(parents=True, exist_ok=True)
        cfg_file = self.path / self.filename
        if not cfg_file.exists():
            home = Path().home().as_posix()
            conf = dict()
            conf_1 = {"in": f"{home}/ImagesIn_1", "out": f"{home}/ImagesOut_1"}
            conf_2 = {"in": f"{home}/ImagesIn_2", "out": f"{home}/ImagesOut_2"}
            conf["directories"] = {"1": conf_1, "2": conf_2}
            self.write(conf)

    def check_directories(self) -> None:
        """
        Comprueba si existen los directorios del archivo de configuración
        asignados a "in" y a "out". En caso de no existir se crean.
        """
        conf_data = self.read()
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
            cfg_file = self.path.joinpath(self.filename)
            return toml.load(cfg_file)
        except IOError as e:
            raise e

    def write(self, data: Dict) -> None:
        """
        Escribe en contenido de 'data' en un archivo de configuración TOML.
        """
        try:
            conf_file = self.path.joinpath(self.filename)
            with open(conf_file, "w") as fd:
                toml.dump(data, fd)
        except IOError as e:
            raise e

    def __str__(self) -> str:
        """
        Retorna el contenido del archivo de configuración.
        """
        return toml.dumps(self.read())
