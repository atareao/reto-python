# Reto 12

Prácticamente hemos llegado al final de estos *mini* retos, donde hemos hecho una gran variedad de operaciones. Pero nos quedan los mas importantes, copiar o borrar. Por supuesto que me dirás que esto ya los hicimos en su momento. Sin embargo, no tienen la estructura de estos últimos.

¿Como la estructura? Si te das cuenta, esto de la estructura, es algo que hemos mantenido desde hace algunos retos, y es algo clave para lo que veremos en los siguientes retos, pero no me quiero adelantar.

De esta manera, este reto 12, consiste en hacer dos clases similares a las que hemos visto hasta el momento. Una de las clases será para copiar archivos o incluso para renombrar archivos, mientras que la segunda será para borrar archivos.

De nuevo, y tal y como he comentadao, cada una de estas clases tiene que tener al menos dos métodos, el primero `check`, será el que se encargue de que se cumplen todas las condiciones, mientras que el segundo de los métodos, `execute`, realizará la acción.

Así la clase resultante `Copy`, al aplicarla será algo similar a lo que te muestro a continuación.

```
def main():
    filein = Path('/home/lorenzo/kk/bb.jpg')
    fileout = Path(f/home/lorenzo/kk/bb_{filter_name}.jpg)
    action = Copy(filein, fileout)
    if action.check():
        action.execute()
```

Mientras que la case `Remove` será algo como lo siguiente,

```
def main():
    filein = Path('/home/lorenzo/kk/bb.jpg')
    action = Remove(filein)
    if action.check():
        action.execute()
```
