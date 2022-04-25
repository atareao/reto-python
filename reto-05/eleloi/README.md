# Reto 5

Está bien tener un directorio, pero seguro que en un futuro quieres tener mas directorios. Así que vamos a dar un paso mas y permitir que el usuario defina tantos directorios como quiera.

Para hacer esto, es necesario modificar nuestro archivo de configuración para dotarle de mas posibilidades. No solo vamos a definir un directorio de entrada sino que además tienes que definir un directorio de salida.

Así el archivo de configuración pasará a ser de la siguiente forma

```
[directorios]

[directorios.1]
in = "/home/lorenzo/ImágenesIn1"
out = "/home/lorenzo/ImágenesOut1"

[directorios.2]
in = "/home/lorenzo/ImágenesIn2"
out = "/home/lorenzo/ImágenesOut2"
```

Igual que hiciste en el reto anterior, en caso de que no exista el directorio y el archivo de configuración, tienes que crearlos. Sin embargo, a diferencia del caso anterior, no definirás ningún directorio. El archivo de configuración tendrá el siguiente aspecto,

```
[directorios]
```

En el caso de que exista el archivo de configuración y tenga diferentes directorios, tendrás que comprobar que existen y en caso de que no existan tienes que crearlos.


