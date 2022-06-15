from ast import arg
from image_utils import ImageGrey

def main():
    imagein = '/home/paly/kk/bb.jpg'
    imageout = '/home/paly/kk/grey_bb.jpg'
    #args = {"h":200, "w":200}
    imagen = ImageGrey(imagein, imageout)
    if imagen.check():
        imagen.execute()

if __name__ == "__main__":
    main()