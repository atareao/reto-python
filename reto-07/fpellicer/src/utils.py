import functools
import glob
import mimetypes
import shutil
from pathlib import Path
from typing import List


def banner(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        """
        Añade como cabecera la ruta desde la cual se listan los archivos.
        """
        print(f"=== {args[0]} ===")
        function(*args, **kwargs)

    return wrapper


@banner
def list_images(path: Path) -> None:
    """
    Lista las imágenes del directorio indicado.

    Args:
        path: Ruta al directorio de imágenes.

    Returns:
        None
    """
    for file in path.iterdir():
        mime = mimetypes.guess_type(file)[0]
        if file.is_file() and mime == "image/jpeg":
            print(file.name)


@banner
def actions(src: Path, dst: Path, actions_: List, filter_: str) -> None:
    """
    Copia o mueve el contenido 'src' a 'dst' según el valor de 'action'.

    Args:
        filter_: Tipo de archivo a filtrar (ej: *.png).
        src: Directorio de origen.
        dst: Directorio de destino.
        actions_: Puede ser: 'move', 'copy'.

    Returns:
        None
    """
    filter_match = glob.glob(src.joinpath(filter_).as_posix())
    for action in actions_:
        if action == "copy":
            for item in filter_match:
                shutil.copy(item, dst)
        elif action == "move":
            for item in filter_match:
                name = item.split("/")[-1]
                src_ = dst / name
                if src_.exists():
                    src_.unlink()
                # Versión <= 3.8 NO acepta objetos tipo Path como src
                shutil.move(item, dst)
        else:
            pass


def filter_filetype(filetype: str) -> List:
    """
    Filtra según el tipo de archivo indicado.

    Args:
        filetype: Tipo de archivo a filtrar (ej: *.png).

    Returns:
        Lista de coincidencias según el tipo filtrado.
    """
    return glob.glob(filetype)
