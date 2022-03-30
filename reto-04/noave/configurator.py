import os
import toml

class Configurator:
    
    def __init__(self, path, config):
        
        self.path = path
        self.config = config
        self.check_exist()
        
        
    def check_exist(self):
        
        """
        Comprueba que existen una ruta y su archivo
        de configuración. Si no, los crea.
        """
        
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        configFile= os.path.join(self.path, self.config)

        if not os.path.exists(configFile):
            contenidoConf = dict(directorio='/Users/noave/Downloads')

            with open(configFile, 'w') as f:
                toml.dump(contenidoConf, f)


    def read(self):
        """
        Lee el contenido de un archivo toml.
        """
        configFile = os.path.join(self.path, self.config)

        return toml.load(configFile)

