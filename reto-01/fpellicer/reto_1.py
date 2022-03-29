import os
from pathlib import Path


def main():
    """
    Lista solamente los archivos del directorio de descargas
    """
    user_dirs = Path(Path.home(), ".config/user-dirs.dirs")

    with open(user_dirs) as f:
        for line in f.readlines():
            if "XDG_DOWNLOAD_DIR" in line:
                _, path = line.split("=")  # path toma el valor '"$HOME/Descargas"\n'
                break

    _ = path.strip()
    download_path = Path(os.path.expandvars(_.strip('"')))

    print(f"Directory: {download_path}\n")

    for file in download_path.iterdir():
        if file.is_file():
            print(file.name)


if __name__ == '__main__':
    main()
