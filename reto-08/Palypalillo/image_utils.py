from pathlib import Path
from PIL import Image

class ImageUtils():
    
    def __init__(self, imagein, imageout, args) -> None:
        self.__imagein = Path (imagein)
        self.__imageout = Path (imageout)
        self.__args = args
        self.__image = Image.open(self.__imagein)
    
    def check(self):
        if not self.__imagein.exists() or not self.__imagein.is_file():
            return False
        if not self.__imageout.parent.exists() or not self.__imageout.parent.is_dir():
            return False
        if "width" not in self.__args:
            return False
        if (self.__args['width']/self.__args['height']) != (self.__image.width/self.__image.height):
            print("Proporciones no validas elige una altura y ancho correctos")
            print( f"ejemplo para esta imagen width: {self.__args['width']} "\
                f"height: {(self.__image.height/self.__image.width)*self.__args['width']}")
            return False
        else:
            return True
    
    def resize_image(self):
        resize_image = self.__image.resize((self.__args['width'],
                                     self.__args['height']))
        resize_image.save(self.__imageout)