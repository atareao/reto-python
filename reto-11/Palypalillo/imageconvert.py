from pathlib import Path
import mimetypes
import re
from PIL import Image


ORIGEN = ["image/jpeg", "image/png", "image/x-ms-bmp"]
DESTINO = ["image/jpeg", "image/png", "image/x-ms-bmp", "application/pdf"]

mimetypes.init()


class Convert:
    
    def __init__(self, filein, fileout):
        self.__filein = Path(filein)
        self.__fileout = Path(fileout)
        
    def check(self):
        if not self.__filein.exists() or not self.__filein.is_file():
            return False
        if not self.__fileout.parent.exists() or \
                not self.__fileout.parent.is_dir():
            return False
        mimetype_filein = mimetypes.guess_type(self.__filein)[0]
        mimetype_fileout = mimetypes.guess_type(self.__fileout)[0]
        if mimetype_filein not in ORIGEN:
            return False
        if mimetype_fileout not in DESTINO or \
                mimetype_fileout == mimetype_filein:
            return False
        return True
    
    def execute(self):
        image = Image.open(self.__filein)
        image.save(self.__fileout)