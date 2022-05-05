from enum import Enum
import re
import toml
import os
import pydantic


class InvalidFilterString(ValueError):
    def __init__(self, value: str, *args: object) -> None:
        self.value = value
        super().__init__(*args)


class Action(Enum):
    NONE = "none"
    MOVE = "move"
    COPY = "copy"


class UserDir(pydantic.BaseModel):
    in_: str = pydantic.Field(alias="in")
    out: str
    actions: list[Action]
    filter_: str = pydantic.Field(
        # regex=r"^\*\.\w+$",
        # description="a filter to select which files to process, like *.jpg",
        alias="filter",
    )

    @pydantic.validator("filter_")
    @classmethod
    def check_filter_regex_match(cls, value):
        if not re.search(r"^\*\.\w+$", value):
            raise InvalidFilterString(value=value)
        return value


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
