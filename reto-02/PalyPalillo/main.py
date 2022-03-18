import os
from pathlib import Path

def getconfig():
    if 'XDG_CONFIG_HOME' in os.environ:
        return os.environ['XDG_CONFIG_HOME']
    else:
        return Path.home() / '.config'

def getDirDesc():
    if 'XDG_DOWNLOAD_DIR' in os.environ:
        return os.environ['XDG_DOWNLOAD_DIR']
    config_dir = Path(getconfig())
    user_dirs_file = config_dir / 'user-dirs.dirs'
    with open(user_dirs_file, 'r') as fr:
        for line in fr.readlines():
            if line.startswith('XDG_DOWNLOAD_DIR'):
                directory = line.split("=")[1].replace("\"",'')
                download_dir  = directory.replace("$HOME", str(Path.home()))[:-1]
                return Path(download_dir)
    return None

def cribar(archivo):
    exten = ('jpeg', 'jpg')
    archivo=archivo.lower()
    if archivo.endswith(exten):
        return archivo
    
def es_par(numero):
    if numero%2 == 0:
        return(str(numero)+' =>')
    else:
        return(str(numero))

def imprimir(archivo, numero):
    encontrado=False
    n=-1
    while n<9:
        n+=1
        if archivo.find(str(n))!=-1:
            encontrado=True
    if encontrado:
        print(es_par(numero), archivo)
    else:
        print(es_par(numero), archivo.upper())                
    
    
def main():
    numero=0
    try:
        directorio = getDirDesc()
        if directorio is not None and isinstance(directorio, Path) and directorio.is_dir():
            print(f"\nDirectorio: {directorio}\n")
            for file in directorio.iterdir():
                if not file.is_dir() and cribar(file.name) is not None:
                    numero+=1
                    imprimir(file.name, numero)
            
    except Exception as ex:
        print(ex)
        


if __name__ == "__main__":
    main()