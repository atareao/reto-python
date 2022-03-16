# Reto 3

Ahora que mas o menos tenemos controlado la opción de listar y *gestionar* todos los archivos que se encuentran en nuestro directorio de `Descargas`, ha llegado el momento de *rizar el rizo*. En lugar de utilizar el directorio de `Descargas`, vas a permitir que el usuario de tu aplicación pueda definir el directorio quiera.

Para hacer esto necesitas un archivo de configuración donde guardar la información. En este caso, y como primer paso, solo vas a guardar un directorio. Para hacer esto, en este tercer reto vas a utilizar el formato TOML [Tom's Obvious Minimal Language](https://github.com/toml-lang/toml).

Así, el archivo de configuración tendrá el siguiente contenido

```
directorio = "/home/lorenzo/Descargas"
```

Así, el objetivo de este reto es crear el archivo de configuración en el caso de que no exista el mismo, y asignar como directorio el directorio por defecto el directorio de descargas, del primero de los retos.

El archivo de configuración se tiene que encontrar en `/home/lorenzo/.config/diogenes/`, y su nombre será `diogenes.conf`.

En el caso de que exista el archivo de configuración tiene que leer el contenido del mismo y listar los imágenes *jpeg* que se encuentran en él. En el caso de que no exista el directorio de las imágenes lo creará. Si no encuentra ninguna imagen, como es lógico no las listará claro.
