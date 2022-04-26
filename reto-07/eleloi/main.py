from typing import Protocol
import _config
import _executers

CONFIG_PATH = "config.toml"


class Executer(Protocol):
    in_path: str
    out_path: str
    extension_filter: str

    def run(self) -> None:
        ...


def execute_action(directory: _config.UserDir):

    executers: dict[_config.Action, Executer] = {
        _config.Action.NONE: _executers.NoneExecuter(
            in_path=directory.in_,
            out_path=directory.out,
            extension_filter=directory.filter_,
        ),
        _config.Action.COPY: _executers.CopyExecuter(
            in_path=directory.in_,
            out_path=directory.out,
            extension_filter=directory.filter_,
        ),
        _config.Action.MOVE: _executers.MoveExecuter(
            in_path=directory.in_,
            out_path=directory.out,
            extension_filter=directory.filter_,
        ),
    }

    executers[directory.action].run()


def main():
    config = _config.read(CONFIG_PATH)
    for directory in config.directorios:
        execute_action(directory)


if __name__ == "__main__":
    main()
