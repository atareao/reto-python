# Esto es el Reto Python 1 para MACOS
import os


def main():
    print()
    directorio = os.environ['HOME'] + "/Downloads"
    print("Directorio: " + directorio)
    print()

    contenido = os.listdir(directorio)

    for fichero in contenido:
        if os.path.isfile(os.path.join(directorio, fichero)):
            print(fichero)


if __name__ == "__main__":
    main()
