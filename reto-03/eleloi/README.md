El archivo de configuración tendrá el siguiente contenido

```
directorio = "/home/lorenzo/Descargas"
```

Crear el archivo de configuración en el caso de que no exista, y asignar como
directorio el directorio por defecto el directorio de descargas, del primero de
los retos.

El archivo de configuración se tiene que encontrar en
`/home/lorenzo/.config/diogenes/`, y su nombre será `diogenes.conf`.

En el caso de que exista el archivo de configuración tiene que leer el contenido
del mismo y listar los imágenes _jpeg_ que se encuentran en él. En el caso de
que no exista el directorio de las imágenes lo creará. Si no encuentra ninguna
imagen, como es lógico no las listará claro.
