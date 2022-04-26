from enum import Enum
import toml
import os
import pydantic


class Action(Enum):
    NONE = "none"
    MOVE = "move"
    COPY = "copy"


class UserDir(pydantic.BaseModel):
    in_: str
    out: str
    action: Action

    class Config:
        fields = {"in_": "in"}


class Configuration(pydantic.BaseModel):
    directorios: list[UserDir]


def _generate_default_configuration_file(config_path: str) -> None:
    default_config = Configuration(directorios=[])
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(toml.dumps(default_config.dict()))


def read(config_path: str) -> Configuration:
    if not os.path.isfile(config_path):
        _generate_default_configuration_file(config_path)

    return Configuration(**toml.load(config_path))
