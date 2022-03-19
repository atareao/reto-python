# El usuario define el directorio que quira usar para listar
# Guardar el directorio en un archivo de conf
import os

def buscar_imagenes(archivo):
    """Filtrar imágenes jpg y jpeg"""
    return archivo.lower().endswith(('jpg', 'jpeg'))

def check_numero(string):
    """Comprobar si el nombre tiene un número"""
    return string.lower() if any(map(str.isdigit, string)) else string.upper()

def main():
    conf_path = "/home/roberto/.config/diogenes/"
    conf_file = "diogenes.conf"
    conf_completo = conf_path + conf_file

    try:
        if not os.path.exists(conf_completo):
            os.mkdir(conf_path)
            with open(conf_completo, 'w') as f:
                descargas = os.popen("xdg-user-dir DOWNLOAD").read().strip()
                f.write(f'directorio = "{descargas}"')
        configuracion = open(conf_completo).readline()
        directorio = configuracion[configuracion.index("=") +1 :].strip().replace('"','')

        if not os.path.exists(directorio):
            raise Exception(f'No existe el directorio {directorio}')

        for idx, val in enumerate(map(check_numero, filter(buscar_imagenes,
                                                           os.listdir(directorio)))):
            print(idx, val) if idx % 2 else print('{} => "{}"'.format(idx, val))

    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    main()
