from pathlib import Path
from PIL import Image
import pilgram

FILTERS = [
    "_1977", "aden", "brannan", "brooklyn", "clarendon", "earlybird",
    "gingham", "hudson", "inkwell", "kelvin", "lark", "lofi", "maven",
    "mayfair", "moon", "nashville", "perpetua", "reyes", "rise",
    "slumber", "stinson", "toaster", "valencia", "walden", "willow", "xpro2"]

class InstagramImage:
    
    def __init__(self, filein, fileout, args={}):
        self.__filein = Path(filein)
        self.__fileout = Path(fileout)
        self.__args = args

    def check(self):
        if not self.__filein.exists() or not self.__filein.is_file():
            return False
        if not self.__fileout.parent.exists() or \
                not self.__fileout.parent.is_dir():
            return False
        if "filter" not in self.__args.keys() or \
                self.__args['filter'] not in FILTERS:
            return False        
        return True

    def execute(self):
        image = Image.open(self.__filein)
        filter_name = self.__args['filter']
        filter = getattr(pilgram, filter_name)
        filter(image).save(self.__fileout)        