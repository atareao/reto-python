import mimetypes
from pathlib import Path

from PIL import Image


class ResizeImage:
    """
    Redimensiona una imagen indicando la anchura y la altura.
    """

    def __init__(self, file_in, file_out, args):
        """
        Args:
            file_in (Path): Archivo de entrada (imagen)
            file_out (Path): Directorio donde guardar en archivo editado
            args (dict): Valores para el ancho (width) y el alto (height)

        Returns:
            None
        """
        self.file_in = file_in
        self.file_out = file_out
        self.width = int(args["width"])
        self.height = int(args["height"])

    def check(self) -> bool:
        """
        Verifica que el archivo de entrada es una imagen y que el
        directorio de salida existe.
        """
        mimetype = mimetypes.guess_type(self.file_in)[0]
        return "image" in mimetype and self.file_out.exists()

    def execute(self) -> None:
        """Redimensiona una imagen"""
        with Image.open(self.file_in) as img:
            img.load()

        resized_image = img.resize((self.width, self.height))
        name = self.file_in.stem + "_resized" + self.file_in.suffix
        resized_image.save(self.file_out / name)
        print(self.file_out / name)

    def thumbnail(self) -> None:
        """Redimensiona una imagen preservando las proporciones"""
        with Image.open(self.file_in) as img:
            img.load()

        img_copy = img.copy()
        img_copy.thumbnail((self.width, self.height))
        name = self.file_in.stem + "_thumbnail" + self.file_in.suffix
        img_copy.save(self.file_out / name)
        print(self.file_out / name)


def main():
    file_in = Path("/home/fran/Testing/reto-python/ImagesIn_1/tux.png")
    file_out = Path("/home/fran/Testing/reto-python/ImagesOut_1/")
    args = {"width": 200, "height": 200}
    resize_image = ResizeImage(file_in, file_out, args)
    if resize_image.check():
        resize_image.execute()
        # resize_image.thumbnail()


if __name__ == "__main__":
    main()
