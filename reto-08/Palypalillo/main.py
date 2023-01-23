from image_utils import ImageResize

def main():
    imagein = '/home/paly/kk/bb.jpg'
    imageout = '/home/paly/kk/bbresize.jpg'
    args = {"w": 200,"h": 150}
    imagen = ImageResize(imagein, imageout, args)
    if imagen.check():
        imagen.execute() 

if __name__ == "__main__":
    main()