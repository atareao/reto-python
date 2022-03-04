import os
import re


def get_download_folder():
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")


print(get_download_folder())

patronJPG = re.compile(r"\.jp[e]?g", re.IGNORECASE)
patronNum = re.compile(r"[0-9]", re.IGNORECASE)
descargasDir = get_download_folder()

contenido = os.listdir(descargasDir)
imagenes = []
for fichero in contenido:
    if os.path.isfile(os.path.join(descargasDir, fichero)) and patronJPG.search(fichero):
        imagenes.append(fichero)

pos = 0

for i in imagenes:
    pos += 1
    if pos % 2 == 0:
        i = "=> " + i

    if patronNum.search(i):
        print(i.upper())
    else:
        print(i.lower())
