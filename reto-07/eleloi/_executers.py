from dataclasses import dataclass
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


@dataclass
class NoneExecuter:

    in_path: str
    out_path: str
    extension_filter: str

    def run(self) -> None:
        _create_folders_if_dont_exists([self.in_path, self.out_path])
        return None


@dataclass
class CopyExecuter:

    in_path: str
    out_path: str
    extension_filter: str

    def run(self) -> None:
        """Copy without overwrite"""
        _create_folders_if_dont_exists([self.in_path, self.out_path])
        in_files = os.listdir(self.in_path)
        out_files = os.listdir(self.out_path)
        extension = _get_extension_of_filter(self.extension_filter)

        for filename in [
            x
            for x in in_files
            if x not in out_files and x.lower().endswith(extension)
        ]:
            shutil.copy2(
                os.path.join(self.in_path, filename),
                os.path.join(self.out_path, filename),
            )


@dataclass
class MoveExecuter:

    in_path: str
    out_path: str
    extension_filter: str

    def run(self) -> None:
        """Move with overwrite"""
        _create_folders_if_dont_exists([self.in_path, self.out_path])
        extension = _get_extension_of_filter(self.extension_filter)

        for filename in [
            x for x in os.listdir(self.in_path) if x.lower().endswith(extension)
        ]:
            shutil.move(
                os.path.join(self.in_path, filename),
                os.path.join(self.out_path, filename),
            )
