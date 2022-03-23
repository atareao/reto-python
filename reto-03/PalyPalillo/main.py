import os
from pathlib import Path
import mimetypes
import toml

mimetypes.init()

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

def main():
    
    diogenes_dir=str(getconfig()) + "/diogenes"
    os.makedirs(diogenes_dir, exist_ok=True)
    config_file = os.path.join(diogenes_dir, "diogenes.toml")
    
    if not Path(config_file).exists():
        with open(config_file, "w") as f:
            f.write(toml.dumps({"directorio": str(getDirDesc())}))
            
    if Path(config_file).exists():
        with open(config_file, "r") as f:
            directorio=toml.load(f)["directorio"]
        for file in os.listdir(directorio):
            if os.path.isfile(os.path.join(directorio, file)) \
                and mimetypes.guess_type(os.path.join(directorio, file))[0] == 'image/jpeg':
                print(file)

if __name__ == "__main__":
    main()