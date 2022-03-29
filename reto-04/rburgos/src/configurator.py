import toml

class Configurator:

    def __init__(self, path, config):
        self.path = path
        self.config = config
        self.config_file = path / config

    def __check_conf(self):
        """Comprobar si existe el path de configuración"""
        if not self.path.exists():
            os.makedirs(self.path)
        if not self.config_file.exists():
            idata = {}
            idata["directorio"] = "/home/rburgos/Descargas"
            with open(config_file, 'w') as file_writer:
                toml.dump(idata, file_writer)

    def read(self):
        """Listar contenido del archivo de configuración"""
        self.__check_conf()
        idata = toml.load(self.config_file)
        return idata
