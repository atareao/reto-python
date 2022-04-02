import os
import mimetypes

def list_images(directorio):
    if not directorio.exists():
        os.makedirs(directorio)
    for file in directorio.iterdir():
        if not file.is_dir() and mimetypes.guess_type(file)[0] == 'image/jpeg':
            print(file.name)