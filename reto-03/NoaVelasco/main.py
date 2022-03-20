# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

# Para el proyecto "reto-python" de Lorenzo Carbonell <a.k.a. atareao>

import mimetypes  # Para los JPG
from os import listdir, path  # Para manejar rutas
import re  # Para buscar o reemplazar 

# No tengo la menor idea de qué es lo de TOML y no sé
# si hay que implementar algo o cómo hacerlo.

def main():
    
    rutaDiogenes = path.join(path.expanduser(
        "~"), '.config\diogenes\diogenes.conf')

    # ¿Existe el archivo config? Si no, se crea:
    
    if path.isfile(rutaDiogenes)==False:
        with open(rutaDiogenes, "w") as f:
            f.write('directorio = "/Users/noave/Downloads"')

    # Se lee el archivo:
    
    with open(rutaDiogenes, "r") as f:
            dwnldDir = f.readline()
            
    # No he sido capaz de obtener el resultado de un re.compile/re.search 
    # como string para usarlo como directorio. He tenido que hacer reemplazos,
    # lo que es poco eficiente y elegante, pero aún no sé manejar el módulo re.
    
    reemplazo1 = re.sub(r"""[ ="]""", "", dwnldDir)
    reemplazo2 = re.sub(r"""\n""", "", reemplazo1)
    reemplazo3 = re.sub(r"""directorio""", "", reemplazo2) 

    print(f"Imágenes JPG en el directorio '{reemplazo3}': \n-----------------------------")
    
    # Si los archivos del directorio son JPG, mostrarlos uno a uno:
    
    listArchivos = listdir(reemplazo3)
    for fichero in listArchivos:
        if mimetypes.guess_type(fichero)[0] == "image/jpeg":
            print(fichero)
        
 
if __name__ == "__main__":
    main()
