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
        return True
    
    def resize_image(self):
        if "w" in self.__args and "h" in self.__args:
            if (self.__args['w']/self.__args['h']) != (self.__image.width/self.__image.height):
                print("La Imagen de Salida no guarda las Proporciones")
                print( f"ejemplo para esta imagen w: {self.__args['w']} "\
                    f"h: {(self.__image.height/self.__image.width)*self.__args['w']}")
            resize_image = self.__image.resize((self.__args['w'],
                                        self.__args['h']))
            resize_image.save(self.__imageout)
        else:
            print("no se ha introducido nuevo tamaño")