import os
import shutil
import pathlib


def _create_folders_if_dont_exists(paths: list[str]) -> None:
    for path in paths:
        path = pathlib.Path(path)
        path.mkdir(parents=True, exist_ok=True)


def none(in_path: str, out_path: str) -> None:
    _create_folders_if_dont_exists([in_path, out_path])
    return None


def copy(in_path: str, out_path: str) -> None:
    """Copy without overwrite"""
    _create_folders_if_dont_exists([in_path, out_path])
    in_files = os.listdir(in_path)
    out_files = os.listdir(out_path)

    for filename in [x for x in in_files if x not in out_files]:
        shutil.copy2(
            os.path.join(in_path, filename), os.path.join(out_path, filename)
        )


def move(in_path: str, out_path: str) -> None:
    """Move with overwrite"""
    _create_folders_if_dont_exists([in_path, out_path])
    for filename in os.listdir(in_path):
        shutil.move(
            os.path.join(in_path, filename), os.path.join(out_path, filename)
        )
