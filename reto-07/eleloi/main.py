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


def execute_action(
    in_path: str, out_path: str, filter_: str, action: _config.Action
):

    executers: dict[_config.Action, Executer] = {
        _config.Action.NONE: _executers.NoneExecuter(
            in_path=in_path,
            out_path=out_path,
            extension_filter=filter_,
        ),
        _config.Action.COPY: _executers.CopyExecuter(
            in_path=in_path,
            out_path=out_path,
            extension_filter=filter_,
        ),
        _config.Action.MOVE: _executers.MoveExecuter(
            in_path=in_path,
            out_path=out_path,
            extension_filter=filter_,
        ),
    }

    executers[action].run()


def main():
    config = _config.read(CONFIG_PATH)
    for directory in config.directorios:
        for idx, action in enumerate(directory.actions):
            in_dir = directory.in_ if idx == 0 else directory.out
            out_dir = directory.out
            filter_ = directory.filter_
            execute_action(in_dir, out_dir, filter_, action)


if __name__ == "__main__":
    main()
