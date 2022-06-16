from imageconvert import Convert

def main():
    filein = '/home/paly/kk/bb.jpg'
    fileout = '/home/paly/kk/bb.bmp'
    action = Convert(filein, fileout)
    if action.check():
        action.execute()
        
if __name__ == "__main__":
    main()