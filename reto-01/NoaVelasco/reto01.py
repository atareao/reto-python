import os

def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")
    
print(get_download_folder()) 

ejemplo_dir = get_download_folder()
with os.scandir(ejemplo_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
for i in ficheros:
    print(i)