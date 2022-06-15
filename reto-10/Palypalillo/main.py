from instagramfilter import InstagramImage

def main():
    filter_name = "valencia"
    filein = '/home/paly/kk/bb.jpg'
    fileout = f'/home/paly/kk/bb_{filter_name}.jpg'
    action = InstagramImage(filein, fileout, {"filter": filter_name})
    if action.check():
        action.execute()
        
if __name__ == "__main__":
    main()