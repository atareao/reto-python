# Reto 8

Cambiamos de tercio completamente. Ahora vamos a crear *pequeñas clases* que hagan determinadas acciones sobre un archivo. Así, vamos a empezar con una sencilla clase que redimensionará Imágenes

La clase tiene que tener al menos dos métodos, el primero `check`, será el que se encargue de que se cumplen todas las condiciones, mientras que el segundo de los métodos, `execute`, realizará la acción.

En los próximos retos haremos, varias acciones con diferentes tipos de archivo, para ir viendo todas las posibilidades que nos ofrece Python y los módulos.

De cada tipo de archivo haremos de dos a tres acciones, para que veas las posibilidades, y luego daremos el salto a combinarla con el código anterior.

```
class ResizeImage:
    ...
    ...

def main():
    filein = Path('/home/lorenzo/kk/bb.png')
    fileout = Path('/home/lorenzo/kk/salida.png')
    args = {"width": 200, "height": 200}
    resize_image = ResizeImage(filein, fileout, args)
    if resize_image.check():
        resize_image.execute()
```
