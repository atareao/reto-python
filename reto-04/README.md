# Reto 4

A partir del reto 3 viene el reto 4. Este cuarto reto consiste en repetir exactamente el resultado del reto 3, pero utilizando clases. Es mas, te digo cual tiene que ser el contenido del archivo `main.py`

```
from pathlib import Path
from xdg import xdg_config_home
from configurator import Configurator
from utils import list_images


def main(app, config):
    path = Path(xdg_config_home()) / app
    configurator = Configurator(path, config)
    data = configurator.read()
    list_images(Path(data['directorio']))

if __name__ == '__main__':
    APP = "diogenes"
    config = f"{APP}.conf"
    main(APP, config)
```

Tu reto es crear dos módulos `utils` y `configurator`. El primero de los módulos, `utils`, tiene que contener la función `list_images`. El segundo de los métodos tiene que contener una nueva clase de tu creación llamada `Configurator` con un método para inicializarla y un método para leer el contenido. Eso como mínimo. Aunque ya te digo que necesitarás otro para guardar la configuración.
