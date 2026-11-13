# Reto Python

Retos de programación en Python, con enunciado y soluciones. Cada reto plantea un pequeño problema, y cada participante publica su propia solución dentro de la carpeta del reto.

[![Stars](https://img.shields.io/github/stars/atareao/reto-python?style=flat-square)](https://github.com/atareao/reto-python/stargazers)
[![License](https://img.shields.io/github/license/atareao/reto-python?style=flat-square)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/atareao/reto-python?style=flat-square)](https://github.com/atareao/reto-python/commits/main)

## ¿Qué es esto?

Una serie de retos encadenados: cada uno añade una pieza sobre el anterior. Se empieza listando los archivos del directorio de descargas y se termina construyendo pequeñas clases que redimensionan imágenes, aplican filtros, convierten formatos, copian y borran archivos.

El hilo conductor es **Diogenes**, una pequeña aplicación de gestión de imágenes que va creciendo reto a reto.

## Retos

| # | Título | Contenido | Enlace |
|---|--------|-----------|--------|
| 01 | Reto 1 | Listar los archivos (solo archivos) del directorio de descargas, mostrando primero su ruta completa | [reto-01](reto-01) |
| 02 | Reto 2 | Listar solo las imágenes JPEG, alternando mayúsculas y minúsculas según el nombre y numerando los pares con una flecha | [reto-02](reto-02) |
| 03 | Reto 3 | Directorio configurable mediante un fichero TOML en `~/.config/diogenes/diogenes.conf` | [reto-03](reto-03) |
| 04 | Reto 4 | Repetir el reto 3 usando clases: módulos `utils` y `configurator` | [reto-04](reto-04) |
| 05 | Reto 5 | Varios directorios de entrada y salida definidos en el fichero de configuración | [reto-05](reto-05) |
| 06 | Reto 6 | Acciones por directorio: `none`, `move` y `copy` | [reto-06](reto-06) |
| 07 | Reto 7 | Filtros por extensión (`*.jpg`, `*.png`, …) y varias acciones por directorio | [reto-07](reto-07) |
| 08 | Reto 8 | Clase `ResizeImage` con métodos `check` y `execute` para redimensionar imágenes | [reto-08](reto-08) |
| 09 | Reto 9 | Clase `Image2Gray` para convertir una imagen a escala de grises | [reto-09](reto-09) |
| 10 | Reto 10 | Clase `InstagramImage` para aplicar filtros tipo Instagram | [reto-10](reto-10) |
| 11 | Reto 11 | Clase `Convert` para convertir entre JPEG, PNG, BMP y PDF | [reto-11](reto-11) |
| 12 | Reto 12 | Clases `Copy` (copiar/renombrar) y `Remove` (borrar) | [reto-12](reto-12) |

## Estructura de un reto

```
reto-NN/
├── README.md          # Enunciado del reto
├── <participante>/    # Una carpeta por persona con su solución
│   ├── main.py
│   ├── requirements.txt
│   └── ...
└── ...
```

- El **enunciado** está siempre en `reto-NN/README.md`.
- Cada **solución** vive en `reto-NN/<tu-usuario-de-github>/`.
- Algunas soluciones incluyen tests en `reto-NN/<usuario>/test/` y dependencias en `requirements.txt` o `pyproject.toml`.

## Cómo participar

1. Haz un fork del repositorio.
2. Crea la carpeta de tu solución: `reto-NN/<tu-usuario-de-github>/`.
3. Añade tu código (normalmente un `main.py`) y, si usas dependencias externas, un `requirements.txt` o `pyproject.toml`.
4. Abre una pull request contra la rama `main`.

No hay una única solución correcta: el objetivo es comparar enfoques.

## Cómo resolver un reto

1. Lee el enunciado en `reto-NN/README.md`.
2. Crea tu carpeta dentro del reto y escribe tu solución.
3. Ejecútala:

   ```bash
   cd reto-NN/<tu-usuario>
   python main.py
   ```

4. Si tu solución trae tests, instala las dependencias y ejecútalos:

   ```bash
   pip install -r requirements.txt
   pytest
   ```

## Licencia

Distribuido bajo licencia MIT. Consulta [LICENSE](LICENSE) para más información.
