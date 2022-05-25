import mimetypes
from pathlib import Path

from PIL import Image


class GrayscaleImage:
    """
    Convierte una imagen a escala de grises.
    """

    def __init__(self, file_in, file_out):
        """
        Args:
            file_in (Path): Archivo de entrada (imagen)
            file_out (Path): Directorio donde guardar en archivo editado

        Returns:
            None
        """
        self._file_in = file_in
        self._file_out = file_out

    def check(self) -> bool:
        """
        Verifica que el archivo de entrada es una imagen y que el
        directorio de salida existe.
        """
        mimetype = mimetypes.guess_type(self._file_in)[0]
        return "image" in mimetype and self._file_out.exists()

    def execute(self) -> None:
        """Convierte a escala de grises"""
        with Image.open(self._file_in) as img:
            img.load()

        resized_image = img.convert("L")
        name = self._file_in.stem + "_grayscale" + self._file_in.suffix
        resized_image.save(self._file_out / name)
        print(self._file_out / name)


def main():
    file_in = Path("/home/fran/Testing/reto-python/ImagesIn_1/aloy.jpg")
    file_out = Path("/home/fran/Testing/reto-python/ImagesOut_1/")
    resize_image = GrayscaleImage(file_in, file_out)
    if resize_image.check():
        resize_image.execute()


if __name__ == "__main__":
    main()
