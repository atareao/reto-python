from pathlib import Path
import mimetypes


def list_images(path: Path) -> None:
    """
    Lista las imágenes del directorio indicado
    """
    for file in path.iterdir():
        mime = mimetypes.guess_type(file)[0]
        if file.is_file() and mime == "image/jpeg":
            print(file.name)
