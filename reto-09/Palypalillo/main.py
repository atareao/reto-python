from image_utils import ImageUtils

def main():
    imagein = '/home/paly/Pictures/avatar.jpg'
    imageout = '/home/paly/Pictures/modifi_avatar.jpg'
    args = {"w": 140,"h": 200}
    modificacion = ImageUtils(imagein, imageout, args)

    if modificacion.check():
        modificacion.resize_image()
        modificacion2 = ImageUtils(imageout, imageout)
        if modificacion2.check():
            modificacion2.greyscale_image()

if __name__ == "__main__":
    main()