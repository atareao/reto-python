#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import toml


class Configurator:
    def __init__(self, path, config):

        self.path = path
        self.config = config
        self.check_exist()
        dirs = self.read()

        for dr in dirs["directorios"].values():
            for d in dr.values():
                if not os.path.exists(d):
                    os.mkdir(d)

    def check_exist(self):
        """
        Comprueba que existen una ruta y su archivo
        de configuración. Si no, los crea.
        """

        configFile = os.path.join(self.path, self.config)
        contenidoConf = {
            "directorios": {
                "1": {
                    "in": "/Users/noave/Diogenes/Img_1_In",
                    "out": "/Users/noave/Diogenes/Img_1_Out",
                    "action": "none",
                },
                "2": {
                    "in": "/Users/noave/Diogenes/Img_2_In",
                    "out": "/Users/noave/Diogenes/Img_2_Out",
                    "action": "move",
                },
                "3": {
                    "in": "/Users/noave/Diogenes/Img_3_In",
                    "out": "/Users/noave/Diogenes/Img_3_Out",
                    "action": "copy",
                },
            }
        }

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if not os.path.exists(configFile):
            with open(configFile, "w", encoding="utf-8") as f:
                toml.dump(contenidoConf, f)

    def read(self):
        """
        Lee el contenido de un archivo toml.
        """
        configFile = os.path.join(self.path, self.config)
        return toml.load(configFile)
