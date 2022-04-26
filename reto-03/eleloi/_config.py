import toml
import os
import pydantic
from pathlib import Path

CONFIG_PATH = "config.toml"
DOWNLOAD_FOLDER_NAME = "downloads"

class Configuration(pydantic.BaseModel):
    directorio: str



def _get_user_download_directory() -> str:
    home_dir = str(Path.home())
    download_dir = os.path.join(home_dir, DOWNLOAD_FOLDER_NAME)

    if download_dir:
        return download_dir

    raise Exception("Could not find user download directory")


def _get_default_configuration() -> Configuration:
    default_download_directory = _get_user_download_directory()
    return Configuration(directorio=default_download_directory)
    

def _write_toml(config: Configuration) -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(toml.dumps(config.dict()))


def read() -> Configuration:
    if not os.path.isfile(CONFIG_PATH):
        _write_toml(_get_default_configuration())

    return Configuration(**toml.load(CONFIG_PATH))
