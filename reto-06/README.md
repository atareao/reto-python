# Reto 6

A llegado el momento de hacer alguna cosa con los archivos. El primer paso será modificar el archivo de configuración, y añadir una entrada adicional en cada uno de los directorios indicando la acción que quieres realizar. En concreto tienes tres acciones,

* `none` => No se realizará ninguna acción.
* `move` => Se moverán todos los archivos en cada uno de los directorios del `in` al `out`. Si existen en el directorio de destino se tienen que borrar del directorio de destino primero.
* `copy` => Se copiarán todos los archivos del directorio `in` al directorio `out` siempre y cuando no exista un archivo con el mismo nombre en el directorio `out`.

Así, siguiendo con el ejemplo del reto 4, tu archivo de configuración puede tener un aspecto similar al que te muestro a continuación,

```
[directorios]

[directorios.1]
in = "/home/lorenzo/ImágenesIn1"
out = "/home/lorenzo/ImágenesOut1"
action = "none"

[directorios.2]
in = "/home/lorenzo/ImágenesIn2"
out = "/home/lorenzo/ImágenesOut2"
action = "move"

[directorios.3]
in = "/home/lorenzo/ImágenesIn3"
out = "/home/lorenzo/ImágenesOut3"
action = "copy"
```

No tiene por que tener tres entradas, `directorios.1`, `directorios.2` y `directorios.3`. Puede o no tener ninguna o tener tantas como el usuario quiera. Por supuesto las acciones se pueden repetir.

