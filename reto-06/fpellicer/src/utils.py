import shutil
from pathlib import Path
import mimetypes
import functools


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

    Parameters:
        path (Path): Ruta al directorio de imágenes.

    Returns:
        None
    """
    for file in path.iterdir():
        mime = mimetypes.guess_type(file)[0]
        if file.is_file() and mime == "image/jpeg":
            print(file.name)


@banner
def actions(src: Path, dst: Path, action: str) -> None:
    """
    Copia o mueve el contenido 'src' a 'dst' según el valor de 'action'.

    Parameters:
        src (Path): Directorio de origen.
        dst (Path): Directorio de destino.
        action (str): Puede ser: 'move', 'copy'.

    Returns:
        None
    """
    if action == "copy":
        for item in src.iterdir():
            shutil.copy(item, dst)
    elif action == "move":
        for item in src.iterdir():
            src_ = dst / item.name
            if src_.exists():
                src_.unlink()
            # Versión <= 3.8 NO acepta objetos tipo Path como src
            shutil.move(item.as_posix(), dst)
    else:
        pass
