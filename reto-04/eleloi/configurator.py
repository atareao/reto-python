import toml
import os
import pydantic
from pathlib import Path


class Configuration(pydantic.BaseModel):
    directorio: str

class Configurator:
    def __init__(self, config_path: str, config_filename: str) -> None:
        self.config_file = os.path.join(config_path, config_filename)
        
    def read(self) -> Configuration:
        if not os.path.isfile(self.config_file):
            self._write_toml(self._get_default_configuration())

        return Configuration(**toml.load(self.config_file))
    

    def _write_toml(self, config: Configuration) -> None:
        with open(self.config_file, "w", encoding="utf-8") as f:
            f.write(toml.dumps(config.dict()))
            
    @staticmethod
    def _get_user_download_directory() -> str:
        home_dir = str(Path.home())
        download_dir = os.path.join(home_dir, "downloads")

        if download_dir:
            return download_dir

        raise Exception("Could not find user download directory")
            
    def _get_default_configuration(self) -> Configuration:
        default_download_directory = self._get_user_download_directory()
        return Configuration(directorio=default_download_directory)