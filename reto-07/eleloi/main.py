from typing import Callable
import _config
import _executers

CONFIG_PATH = "config.toml"


def execute_action(directory: _config.UserDir):

    Executer = Callable[[str, str, str], None]

    executers: dict[_config.Action, Executer] = {
        _config.Action.NONE: _executers.none,
        _config.Action.COPY: _executers.copy,
        _config.Action.MOVE: _executers.move,
    }

    executers[directory.action](directory.in_, directory.out, directory.filter_)


def main():
    config = _config.read(CONFIG_PATH)
    for directory in config.directorios:
        execute_action(directory)


if __name__ == "__main__":
    main()
