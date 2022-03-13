"""Reto 01 Python Atareao"""
import os

def main():

    """Buscar directorio descargar y listar contenido"""
    descargas = os.popen("xdg-user-dir DOWNLOAD").read().strip()
    print("Directorio:", descargas, "\n".join(os.listdir(descargas)))

if __name__ == '__main__':

    main()
