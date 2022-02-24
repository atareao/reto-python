import os

# import platform
# print('Nombre:', platform.uname())
# print()
# # print('Distribucion :', platform.linux_distribution())
# print('Maquina :', platform.machine())
# print('Nodo :', platform.node())
# print('Procesador :', platform.processor())
# print('Lanzamiento :', platform.release())
# print('Systema :', platform.system())
# print('Version :', platform.version())
# print('Plataforma :', platform.platform())

if __name__ == '__main__':

    directorio_home = os.path.expanduser('~')
    directorio_base = f"{directorio_home}/Descargas"
    existe_directorio_archivo = os.path.exists(directorio_base)

    if existe_directorio_archivo:
        directoria_a_ver = os.listdir(directorio_base)
        print(f'Directorio: {directorio_base}')
        print()
        for archivos in directoria_a_ver:
            print(archivos)