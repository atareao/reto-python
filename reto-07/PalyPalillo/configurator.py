import os
from pathlib import Path
import toml

class Configurator:
    
    def __init__(self, path, config):
        self.path=path
        self.config=config
        self.check_conf()

    def check_conf(self):
        config_dir = self.path
        if not config_dir.exists():
            os.makedirs(config_dir)
        config_file = config_dir / self.config
        if not config_file.exists():
            data = {}
            data['directorios'] = {}
            with open(config_file, 'w') as file:
                toml.dump(data,file)
        conf=self.read()
        for dir in conf['directorios'].values():
                    if 'in' in dir:
                        dir_in = Path(dir['in'])
                        if not dir_in.exists():
                            os.makedirs(dir_in)
                    if 'out' in dir:
                        dir_out = Path(dir['out'])
                        if not dir_out.exists():
                            os.makedirs(dir_out)


    def read(self):
        config_dir = Path(self.path)
        config_file = config_dir / self.config
        idata = toml.load(config_file)
        return idata