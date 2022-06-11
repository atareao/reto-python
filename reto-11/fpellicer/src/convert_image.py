import mimetypes
from pathlib import Path

from PIL import Image

VALID_FORMAT_IN = ('jpeg', 'png', 'bmp')
VALID_FORMAT_OUT = ('jpeg', 'png', 'bmp', 'pdf')


class ConvertImage:
    """Convierte una imagen a otros formatos.

    Formatos de entrada:
        JPG, PNG, BMP

    Formatos de salida:
        JPG, PNG, BMP, PDF

    Args:
        file_in (Path): Archivo de entrada (imagen)
        file_out (Path): Directorio donde guardar en archivo modificado
        format_ (str): Formato a convertir
    """

    def __init__(self, file_in: Path, file_out: Path, format_: str):
        """Constructor de la clase ConvertImage.

        Args:
            file_in (Path): Archivo de entrada (imagen)
            file_out (Path): Directorio donde guardar el archivo modificado
            format_ (str): Formato a convertir
        Returns:
            None
        """
        self._file_in = file_in
        self._file_out = file_out
        self._format = format_.lower()

    def check(self) -> bool:
        """Verifica:
            - Archivo de entrada es una imagen
            - Archivo de salida es compatible con los formatos aceptados
            - Directorio de salida existe
        """
        mimetype = mimetypes.guess_type(self._file_in)[0]
        type_extension = mimetype.split("/")[1]

        if type_extension not in VALID_FORMAT_IN:
            return False

        if self._format not in VALID_FORMAT_OUT:
            return False

        if not self._file_out.exists():
            return False

        return True

    def execute(self) -> None:
        """Convierte la imagen a otro formato"""
        with Image.open(self._file_in) as img:
            img.load()

        name = f"{self._file_in.stem}.{self._format}"
        img.convert("RGB")
        img.save(self._file_out / name)
        print(self._file_out / name)


def main():
    file_in = Path("/home/fran/Testing/reto-python/ImagesIn_1/beach.jpg")
    file_out = Path("/home/fran/Testing/reto-python/ImagesOut_1/")
    format_ = "pdf"
    action = ConvertImage(file_in, file_out, format_)
    if action.check():
        action.execute()


if __name__ == "__main__":
    main()
