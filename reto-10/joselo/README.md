# Reto 10: Filtros de Instagram.
----

 - Uso `pilgram` que a su vez usa `PIL`.
 - Obtengo los filtros de `pilgram.__all__`.
 - Uso `typing.Optional` para tener un `__init__` lo más genérico posible.

### Referencias:

 - [Pilgram en GitHub](https://github.com/akiomik/pilgram)
 - [Filtros Instagram en stackverflow](https://stackoverflow.com/questions/59929801/how-can-i-implement-an-instagram-photo-filter)
----

# Uso de eval
----

 - Uso `eval(f"pilgram.{filtro}")` para obtener la funcion que aplicará el filtro.
 - `eval` no es seguro, pero en este caso conocemos con precisión el texto que se le pasa a `eval`.
 - Para un _"eval seguro"_ ver: [The pitfall of eval function and its safe alternative in Python](https://eulertech.wordpress.com/2018/06/10/the-pitfall-of-eval-function-and-its-safe-alternative-in-python/).
 - Pero por razones de seguridad `ast.literal_eval` no permite la ejecución de llamadas a funcion y no queda otra que usar `eval.
----
