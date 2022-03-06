# Esto es el Reto Python 2 para MACOS
import os


def main():
    print()
    directorio = os.environ['HOME'] + "/Downloads"
    print("Directorio: " + directorio)
    print()

    contenido = os.listdir(directorio)
    contador = 0

    for fichero in contenido:
        if os.path.isfile(os.path.join(directorio, fichero)):
            if fichero.endswith(("jpg", "JPG", "jpeg", "JPEG")):
                if contador % 2 == 0:
                    print("=> ", end='')
                if any(str.isdigit(c) for c in fichero):
                    print(fichero.upper())
                else:
                    print(fichero.lower())
                contador += 1


if __name__ == "__main__":
    main()
