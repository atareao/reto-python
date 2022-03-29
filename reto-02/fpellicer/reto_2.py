from pathlib import Path
from gi.repository import GLib
from typing import Tuple

download_dir = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))


def append_arrow(function):
    """
    Decora 'function' añadiendo => al comienzo de las líneas pares.
    """
    arrow = True

    def wrapper(*args, **kwargs):
        nonlocal arrow
        item = function(*args, **kwargs)
        if item is not None:
            if arrow:
                arrow = False
                print(f"=> {item}")
            else:
                arrow = True
                print(item)

    return wrapper


@append_arrow
def filter_by_extension(file: Path, ext: Tuple[str] = None) -> str:
    """
    Retorna el nombre del archivo si coincide con la extensión dada y si contiene
    números retorna este en mayúsculas.
    Si no se indica extensión, retorna los nombres de los archivos.
    Valores indicados en el parámetro `ext` deben ir precedidos por punto, ej: .jpg.
    """
    if ext is None:
        return file.name
    elif file.suffix.lower() in ext:
        digits = tuple("0123456789")
        if any(item in digits for item in file.name):
            return file.name.upper()
        else:
            return file.name.lower()


def list_files(path: Path) -> None:
    """
    Toma solamente los archivos contenidos en path y filtra por extensión.
    """
    for file in path.iterdir():
        if file.is_file():
            filter_by_extension(file, (".jpg", ".jpeg"))


def main():
    print(f"Directorio: {download_dir}\n")
    list_files(download_dir)


if __name__ == "__main__":
    main()
