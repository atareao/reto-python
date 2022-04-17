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
    """
    for file in path.iterdir():
        mime = mimetypes.guess_type(file)[0]
        if file.is_file() and mime == "image/jpeg":
            print(file.name)
