# reto09
----
### Formas de convertir una imágen a escala de grises con **Wand** e **ImageMagick**.

Ref.: [Use python wand to grayscale image](https://stackoverflow.com/questions/16145959/use-python-wand-to-grayscale-image)

----
 - Forzando el tipo de la imágen 
```python
    from wand import Image
        ...
    with Image(filename='color.jpg') as img:
        img.type = 'grayscale'
```
 - Transformando `colorspace`
```python
    from wand import Image
        ...
    with Image(filename=str(f)) as img:
        img.transform_colorspace('gray')
```

La segunda forma es la correcta ya que preserva el canal alfa mientras que con la primera un fondo transparente queda en negro.

----
### Formas de convertir una imágen a escala de grises con **PIL(Pillow)**.

Ref.: [**Pillow(PIL fork)**](https://pillow.readthedocs.io/en/stable/index.html) 

----
 - Con el método `convert` de la clase `Image`:
```python
    from PIL import Image
        ...
    with Image.open("image.png") as img: 
        img = img.convert(mode='L')
```
 - Con el módulo `ImageOps`:
```python
    from PIL import Image, ImageOps
        ...
    with Image.open("image.png") as img: 
        img = ImageOps.grayscale(img)
```

En este caso los dos métodos nos dan el mismo resultado, que es como en el primer caso de arriba. Esto es lógico ya que el código fuente de `ImageOps.grayscale` es:
```python
    def grayscale(image):
        """
        Convert the image to grayscale.

        :param image: The image to convert.
        :return: An image.
        """
        return image.convert("L")
```

----
