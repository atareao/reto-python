"""Reto 02 Python Atareao"""
import os

def buscar_imagenes(archivo):
    """Filtrar imágenes jpg y jpeg"""
    return archivo.lower().endswith(('jpg', 'jpeg'))

def check_numero(string):
    """Comprobar si el nombre tiene un número"""
    return string.lower() if any(map(str.isdigit, string)) else string.upper()

def main():
    """Listar imágenes desde un archivo de configuracion"""
    conf_path = os.path.expanduser('~/.config/diogenes/')
    conf_completo = os.path.join(conf_path, "diogenes.conf")

    try:
        if not os.path.exists(conf_completo):
            os.mkdir(conf_path)
            with open(conf_completo, 'w') as f:
                descargas = os.popen("xdg-user-dir DOWNLOAD").read().strip()
                f.write(f'directorio = "{descargas}"')

        configuracion = open(conf_completo).readline()
        directorio = configuracion.split("=")[1].strip().replace('"', '')

        if not os.path.exists(directorio):
            raise Exception(f'No existe el directorio {directorio}')

        for idx, val in enumerate(map(check_numero, filter(buscar_imagenes,
                                                           os.listdir(directorio)))):
            print(idx, val) if idx % 2 else print(f'{idx} => "{val}"')
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    main()
