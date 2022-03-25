import mimetypes
from pathlib import Path

import toml

home = Path().home()
toml_config_file = Path(f"{home}/.config/diogenes/diogenes.conf")
# Configuración predeterminada
toml_string = (f"\n"
               f"# Archivo de configuración TOML\n\n"
               f"titulo = 'Archivo de configuración de diogenes.'\n"
               f"directorio = '{home}/Descargas'\n")

try:
    with open(toml_config_file) as f:
        conf = toml.load(f)
except FileNotFoundError:
    conf = toml.loads(toml_string)
    toml_config_file.parent.mkdir(parents=True)
    toml_config_file.write_text(toml.dumps(conf))


def filter_by_filetype(file: Path, file_type: str) -> bool:
    """
    Retorna el nombre del archivo si coincide con el tipo de archivo indicado
    """
    mime = mimetypes.guess_type(file)[0]

    # Evita comparar un archivo no reconocido (None), retorna error
    if mime is not None and file_type == mime:
        return True


def list_files(path: Path) -> None:
    """
    Toma solamente los archivos contenidos en path y filtra por extensión
    """
    for file in path.iterdir():
        if file.is_file() and filter_by_filetype(file, "image/jpeg"):
            print(file.name)


def main():
    path = Path(conf.get("directorio"))
    if not path.exists():
        path.mkdir(parents=True)

    print(f"Directorio: {conf.get('directorio')}\n")
    list_files(path)


if __name__ == "__main__":
    # CORREGIR MIMETYPE ARCHIVOS TEXTO RETORNA None
    main()
