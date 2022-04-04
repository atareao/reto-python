import mimetypes
import os

def list_images(path):
    """Listar imágenes de un directorio"""
    if not path.exists():
        os.makedirs(directory)
    for afile in path.iterdir():
        if not afile.is_dir() and mimetypes.guess_type(afile)[0] == 'image/jpeg':
            print(afile.name)
