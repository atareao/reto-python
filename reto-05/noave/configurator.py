import os
from pathlib import Path
import toml

class Configurator:
    
    def __init__(self, path, config):
        
        self.path = path
        self.config = config
        self.check_exist()
        dirs = self.read()
        
        for dir in dirs['directorios'].values():
            for d in dir.values():
                if not os.path.exists(d):
                    os.mkdir(d)

        
    def check_exist(self):
        
        """
        Comprueba que existen una ruta y su archivo
        de configuración. Si no, los crea.
        """

        configFile= os.path.join(self.path, self.config)
        contenidoConf = {'directorios': {'1': {'in': '/Users/noave/Diogenes/ImgIn1',
                                               'out': '/Users/noave/Diogenes/ImgOut1'},
                                         '2': {'in': '/Users/noave/Diogenes/ImgIn2',
                                               'out': '/Users/noave/Diogenes/ImgOut2'}}}
        
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if not os.path.exists(configFile):
            with open(configFile, 'w') as f:
                toml.dump(contenidoConf, f)


    def read(self):
        """
        Lee el contenido de un archivo toml.
        """
        configFile = os.path.join(self.path, self.config)
        return toml.load(configFile)

