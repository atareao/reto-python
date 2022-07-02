import shutil
from pathlib import Path
from typing import Union


class Copy:
    """Copia/renombra archivos"""

    def __init__(self, file_in: Union[str, Path], file_out: Union[str, Path]):
        self.file_in = Path(file_in)
        self.file_out = Path(file_out)

    def check(self) -> bool:
        """
        Verifica:
         - file_in existe y es un archivo
         - file_out existe y es un archivo (permite renombrar)

         Returns:
             bool
        """
        if not self.file_in.exists() and not self.file_in.is_file():
            return False

        if self.file_out.exists() and not self.file_out.is_file():
            return False

        return True

    def execute(self) -> None:
        """Copia/renombra el archivo indicado"""
        if self.check():
            if not self.file_out.parent:
                self.file_out.parent.mkdir(parents=True)

            shutil.copy2(self.file_in, self.file_out)


class Remove:
    """Elimina un archivo"""

    def __init__(self, file_in: Union[str, Path]):
        self.file_in = Path(file_in)

    def check(self) -> bool:
        """
        Verifica:
         - file_in es un archivo y existe

        Returns:
            bool
        """
        return self.file_in.exists() and self.file_in.is_file()

    def execute(self) -> None:
        """Elimina el archivo indicado"""
        self.file_in.unlink()


def main():
    file_in = "/home/fran/Testing/reto-python/ImagesIn_1/beach.jpg"
    file_out = "/home/fran/Testing/reto-python/ImagesOut_1/beach.jpg"
    action = Copy(file_in, file_out)
    # action = Remove(file_out)
    if action.check():
        action.execute()


if __name__ == "__main__":
    main()
