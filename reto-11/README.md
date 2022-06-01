# Reto 11

Nos quedan ya pocas cosas por hacer. Sin embargo, algo importante que no hemos hecho hasta el momento es convertir entre distintos formatos. Por ejemplo convertir de un formato de imagen a otro formato de imagen, o incluso convertir una imagen en un documento PDF.

Pues de esto va precisamente este reto, se trata de convertir entre distintos formatos. En este caso entre unos formatos permitidos. En concreto, se tiene que poder convertir desde,

* image/jpeg
* image/png
* image/bmp

a los siguientes formatos,

* image/jpeg
* image/png
* image/bmp
* application/pdf

Así la clase resultante `Convert`, al aplicarla será algo similar a lo que te muestro a continuación.

```
def main():
    filein = Path("/home/lorenzo/kk/bb.jpg")
    fileout = Path("/home/lorenzo/kk/bb.pdf")
    action = Convert(filein, fileout)
    if action.check():
        action.execute()
```
