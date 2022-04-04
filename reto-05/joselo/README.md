# Reto 05: diccionarios

### README provisional hasta que atareo cuelgue el suyo.

#### Resumen

 1. ya no hay un directorio sino varias parejas de directorios y por ello
 tampoco hay un directorio por defecto.

 2. Las parejas consisten en un directorio de entrada y otro de salida.
 
 3. Como en el reto 04, hay que comprobar que los directorios existen y en caso 
 contrario hay que crearlos.
 
 4. En el caso de que no exista el directorio de configuración se crea.
 
 5. Si no existe el fichero de configuración, se crea pero no se asignan valores por defecto.
 
 6. El contenido del fichero de configuración debe tener un aspecto como este:
    ```
    [directorios]

    [directorios.1]
    in = "/home/lorenzo/ImágenesIn1"
    out = "/home/lorenzo/ImágenesOut1"

    [directorios.2]
    in = "/home/lorenzo/ImágenesIn2"
    out = "/home/lorenzo/ImágenesOut2"
    ```
  
  7. En el caso de que no exista el fichero de configuración, se crea con el siguiente contenido:
     ```
     [directorios]
     ```
  
  8. Para saber más: [Reto Python 5. Diccionarios](https://atareao.es/tutorial/reto-python/reto-python-diccionarios/)
  
  9. [El vídeo del reto-05](https://www.youtube.com/watch?v=QQKjEUUx31A)
  


