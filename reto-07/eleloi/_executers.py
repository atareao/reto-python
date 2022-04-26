import os
import shutil
import pathlib


def _create_folders_if_dont_exists(paths: list[str]) -> None:
    for path in paths:
        path = pathlib.Path(path)
        path.mkdir(parents=True, exist_ok=True)


def _get_extension_of_filter(filter: str) -> str:
    """
    Remove * character

    the filter has the form *.jpg or *.zzz garanteed by pydantic validator
    """
    return filter[1:].lower()


def none(in_path: str, out_path: str, filter: str) -> None:
    _create_folders_if_dont_exists([in_path, out_path])
    return None


def copy(in_path: str, out_path: str, filter: str) -> None:
    """Copy without overwrite"""
    _create_folders_if_dont_exists([in_path, out_path])
    in_files = os.listdir(in_path)
    out_files = os.listdir(out_path)
    extension = _get_extension_of_filter(filter)

    for filename in [
        x
        for x in in_files
        if x not in out_files and x.lower().endswith(extension)
    ]:
        shutil.copy2(
            os.path.join(in_path, filename), os.path.join(out_path, filename)
        )


def move(in_path: str, out_path: str, filter: str) -> None:
    """Move with overwrite"""
    _create_folders_if_dont_exists([in_path, out_path])
    extension = _get_extension_of_filter(filter)

    for filename in [
        x for x in os.listdir(in_path) if x.lower().endswith(extension)
    ]:
        shutil.move(
            os.path.join(in_path, filename), os.path.join(out_path, filename)
        )
