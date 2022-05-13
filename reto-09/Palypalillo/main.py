from image_utils import ImageUtils

def main():
    imagein = '/home/paly/Pictures/avatar.jpg'
    imageout = '/home/paly/Pictures/grey_avatar.jpg'
    imagen = ImageUtils(imagein, imageout)
    if imagen.check():
        imagen.greyscale_image()

if __name__ == "__main__":
    main()