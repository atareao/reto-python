# Reto 10

En este reto 10 lo vamos a complicar un poco, pero no mucho, no creas. En lugar de únicamente convertir a grises, el objetivo, es poder aplicar cualquiera de los filtros *tipo Instagram* que se muestran mas adelante.

Así, los parámetros de entrada serán el archivo de entrada, el archivo de salida y el filtro que se aplicará.

La clase tiene que tener al menos dos métodos, el primero `check`, será el que se encargue de que se cumplen todas las condiciones, mientras que el segundo de los métodos, `execute`, realizará la acción.

Los posibles filtros son los siguientes:

* _1977
* aden
* brannan
* brooklyn
* clarendon
* earlybird
* gingham
* hudson
* inkwell
* kelvin
* lark
* lofi
* maven
* mayfair
* moon
* nashville
* perpetua
* reyes
* rise
* slumber
* stinson
* toaster
* valencia
* walden
* willow
* xpro2

Así la clase resultante `InstagramImage`, al aplicarla será algo similar a lo que te muestro a continuación.

```
def main():
    filter_name = "lofi"
    filein = Path('/home/lorenzo/kk/bb.jpg')
    fileout = Path(f/home/lorenzo/kk/bb_{filter_name}.jpg)
    action = InstagramImage(filein, fileout, {filter: filter_name})
    if action.check():
        action.execute()
```
