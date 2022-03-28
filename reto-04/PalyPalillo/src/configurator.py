import os
from pathlib import Path
import toml

class Configurator:
    
    def __init__(self, path, config):
        self.path=path
        self.config=config
        self.check_conf()

    def getconfig(self):
        if 'XDG_CONFIG_HOME' in os.environ:
            return os.environ['XDG_CONFIG_HOME']
        else:
            return Path.home() / '.config'

    def getDirDesc(self):
        if 'XDG_DOWNLOAD_DIR' in os.environ:
            return os.environ['XDG_DOWNLOAD_DIR']
        config_dir = Path(self.getconfig())
        user_dirs_file = config_dir / 'user-dirs.dirs'
        with open(user_dirs_file, 'r') as fr:
            for line in fr.readlines():
                if line.startswith('XDG_DOWNLOAD_DIR'):
                    directory = line.split("=")[1].replace("\"",'')
                    download_dir  = directory.replace("$HOME", str(Path.home()))[:-1]
                    return Path(download_dir)
        return None

    def check_conf(self):
        config_dir = self.path
        if not config_dir.exists():
            os.makedirs(config_dir)
        config_file = config_dir / self.config
        if not config_file.exists():
            with open(config_file, 'w') as file:
                toml.dump({"directorio": str(self.getDirDesc())},file)


    def read(self):
        config_dir = Path(self.path)
        config_file = config_dir / self.config
        idata = toml.load(config_file)
        return idata