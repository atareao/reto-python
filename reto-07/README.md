# Reto 7

En el reto 6, comenzaste a realizar acciones con los distintos archivos que se encontraban en cada uno de los archivos. El problema es que era de forma indiscriminada. Lo hacías con todos los archivos.

En este nuevo reto, tienes que aplicar filtros, de forma que las acciones solo se apliquen en aquellos archivos que cumplan con los filtros que indiques. En principio, serán filtros del tipo `*.jpg`, por ejemplo. Es decir, filtros relativos a extensiones.

Así, siguiendo con el ejemplo del reto 6, tu archivo de configuración puede tener un aspecto similar al que te muestro a continuación,

```
[directorios]

[directorios.1]
in = "/home/lorenzo/ImágenesIn1"
out = "/home/lorenzo/ImágenesOut1"
actions = ["copy", "move"]
filter = "*.png"

[directorios.2]
in = "/home/lorenzo/ImágenesIn2"
out = "/home/lorenzo/ImágenesOut2"
actions = ["move"]
filter = "*.svg"

[directorios.3]
in = "/home/lorenzo/ImágenesIn3"
out = "/home/lorenzo/ImágenesOut3"
actions = ["copy", "none"]
```

No tiene por que tener tres entradas, `directorios.1`, `directorios.2` y `directorios.3`. Puede o no tener ninguna o tener tantas como el usuario quiera. Por supuesto las acciones se pueden repetir.
