import mimetypes
from pathlib import Path

import pilgram
from PIL import Image


class InstagramImage:
    """Aplica filtros de Instagram a una imagen.

    Args:
        file_in (Path): Archivo de entrada (imagen)
        file_out (Path): Directorio donde guardar en archivo editado
        filter_ (str): Nombre del filtro de imagen
    """

    # Dict: Filtros aceptados y su correspondiente método
    _filters = {
        "_1977": pilgram._1977,
        "aden": pilgram.aden,
        "brannan": pilgram.brannan,
        "brooklyn": pilgram.brooklyn,
        "clarendon": pilgram.clarendon,
        "earlybird": pilgram.earlybird,
        "gingham": pilgram.gingham,
        "hudson": pilgram.hudson,
        "inkwell": pilgram.inkwell,
        "kelvin": pilgram.kelvin,
        "lark": pilgram.lark,
        "lofi": pilgram.lofi,
        "maven": pilgram.maven,
        "mayfair": pilgram.mayfair,
        "moon": pilgram.moon,
        "nashville": pilgram.nashville,
        "perpetua": pilgram.perpetua,
        "reyes": pilgram.reyes,
        "rise": pilgram.rise,
        "slumber": pilgram.slumber,
        "stinson": pilgram.stinson,
        "toaster": pilgram.toaster,
        "valencia": pilgram.valencia,
        "walden": pilgram.walden,
        "willow": pilgram.willow,
        "xpro2": pilgram.xpro2,
    }

    def __init__(self, file_in: Path, file_out: Path, filter_: str):
        """Constructor de la clase InstagramImage.

        Args:
            file_in (Path): Archivo de entrada (imagen)
            file_out (Path): Directorio donde guardar en archivo editado
            filter_ (str): Nombre del filtro de imagen

        Returns:
            None
        """
        self._file_in = file_in
        self._file_out = file_out
        self._filter = self._filters.get(filter_, False)

    def check(self) -> bool:
        """Verifica:
            - Archivo de entrada es una imagen.
            - Directorio de salida existe.
            - Filtro es válido.
        """
        mimetype = mimetypes.guess_type(self._file_in)[0]
        return "image" in mimetype and self._file_out.exists() and self._filter

    def execute(self) -> None:
        """Aplica el filtro"""
        with Image.open(self._file_in) as img:
            img.load()

        img_mod = self._filter(img)
        name = f"{self._file_in.stem}_{self._filter.__name__}{self._file_in.suffix}"
        img_mod.save(self._file_out / name)
        print(self._file_out / name)


def main():
    filter_name = "valencia"
    file_in = Path("/home/fran/Testing/reto-python/ImagesIn_1/beach.jpg")
    file_out = Path("/home/fran/Testing/reto-python/ImagesOut_1/")
    action = InstagramImage(file_in, file_out, filter_name)
    if action.check():
        action.execute()


if __name__ == "__main__":
    main()
