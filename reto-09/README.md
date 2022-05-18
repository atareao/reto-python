# Reto 9

Seguimos con las *pequeñas clases*, en este caso, es otra sencilla clase para convertir una imagen a escala de grises. Nada mas y nada menos.

Igual que sucedía en el reto anterior, la clase tiene que tener al menos dos métodos, el primero `check`, será el que se encargue de que se cumplen todas las condiciones, mientras que el segundo de los métodos, `execute`, realizará la acción.

De cada tipo de archivo haremos de dos a tres acciones, para que veas las posibilidades, y luego daremos el salto a combinarla con el código anterior.

```
class Image2Gray:
    ...
    ...

def main():
    filein = Path('/home/lorenzo/kk/bb.png')
    fileout = Path('/home/lorenzo/kk/bb_grayscale.png')
    action = Image2Gray(filein, fileout)
    if action.check():
        action.execute()
```
