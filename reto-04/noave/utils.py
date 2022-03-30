import os
import mimetypes

def list_images(directory):
    """
    Comprueba que existe un directorio dado
    e imprime los archivos JPG que haya dentro.
    """

    if not os.path.exists(directory):
        os.mkdir(directory)

    for jpg in directory.iterdir():
        if not jpg.is_dir() and mimetypes.guess_type(jpg)[0] == "image/jpeg":
            print(jpg.name)
