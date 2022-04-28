import os
import mimetypes
import shutil

def list_images(directorio):
    if not directorio.exists():
        os.makedirs(directorio)
    for file in directorio.iterdir():
        if not file.is_dir() and mimetypes.guess_type(file)[0] == 'image/jpeg':
            print(file.name)
            
def move(dirin,dirout):
    if not dirin.exists():
        os.makedirs(dirin)
    elif not dirout.exists():
        os.makedirs(dirout)
    for file in dirin.iterdir():
        if file.is_file():
            fileout = dirout / file.name
            os.replace(file, fileout)

def copy(dirin,dirout):
    if not dirin.exists():
        os.makedirs(dirin)
    elif not dirout.exists():
        os.makedirs(dirout)
    for file in dirin.iterdir():
        fileout = dirout / file.name
        if file.is_file() and not fileout.exists():
            print(f"copiando {file.name}")
            shutil.copy(file, dirout)
        else:    
            print(f"el archivo {file.name} ya existe en destino")
            