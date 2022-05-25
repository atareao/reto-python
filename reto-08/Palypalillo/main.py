from image_utils import ImageUtils

def main():
    imagein = '/home/paly/Pictures/kitty.jpeg'
    imageout = '/home/paly/Pictures/resize_kitty.jpeg'
    args = {"w": 200,"h": 150}
    imagen = ImageUtils(imagein, imageout, args)
    if imagen.check():
        imagen.resize_image() 

if __name__ == "__main__":
    main()