import os
import mimetypes
import shutil

def list_images(directorio):
    if not directorio.exists():
        os.makedirs(directorio)
    for file in directorio.iterdir():
        if not file.is_dir() and mimetypes.guess_type(file)[0] == 'image/jpeg':
            print(file.name)
            
def move(dirin,dirout,filtro):
    if not dirin.exists():
        os.makedirs(dirin)
    elif not dirout.exists():
        os.makedirs(dirout)
    for file in dirin.iterdir():
        nombre=file.name
        if file.is_file() and nombre.lower().endswith(str.lower(filtro)):
            fileout = dirout / nombre
            print(f"moviendo {nombre}")
            os.replace(file, fileout)

def copy(dirin,dirout,filtro):
    if not dirin.exists():
        os.makedirs(dirin)
    elif not dirout.exists():
        os.makedirs(dirout)
    for file in dirin.iterdir():
        nombre=file.name
        fileout = dirout / nombre
        if file.is_file() and not fileout.exists():
            if nombre.lower().endswith(str.lower(filtro)):
                print(f"copiando {nombre}")
                shutil.copy(file, dirout)
        else:    
            print(f"el archivo {nombre} ya existe en destino")
            