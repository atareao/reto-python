# PLAN-001 — Corregir vulnerabilidades Dependabot (reto-python)

## Objetivo
Reducir las alertas Dependabot abiertas del repo `atareao/reto-python` de 112 a 0.
Estado inicial: 8 críticas, 63 altas, 41 medias.

## Contexto
Repo de retos de Python con múltiples proyectos independientes por contribuidor.
Rama de trabajo: `feature/fix-dependabot-alerts` (desde `main`). Entrega: un PR a `main `.
Herramientas: sin `poetry` ni `pip-audit` instalados; Python 3.14.8; red disponible.

## Hallazgos (agrupados)
- **Grupo A — Pillow (95 alertas)**: `reto-10/joselo/requirements.txt` y `reto-11/joselo/requirements.txt` fijan `Pillow==9.1.1`. Versión segura: `>=13.0.0 `.
- **Grupo B — poetry eleloi (16 alertas)**: `reto-03,05,06,07/eleloi/poetry.lock` con `black==22.3.0` (seguro `>=26.10.1`), `pydantic==1.9.0` (seguro `>=1.10.13`), `pytest==7.1.2` (seguro `>=9.0.3`).
- **Grupo C — constraint (1 alerta)**: `reto-04/eleloi/pyproject.toml` declara `black = "^22.3.0"` (permite <24.3.0). Sin lock asociado.

## Tareas
- [ ] T1 (Grupo A): editar `reto-10/joselo/requirements.txt` y `reto-11/joselo/requirements.txt`: `Pillow==9.1.1` → `Pillow>=13.0.0`. Mantener `numpy==1.22.4` y `pilgram==1.2.1` (sin alertas). Verificar que la spec de dependencias de `pilgram==1.2.1` admite Pillow 13.
- [ ] T2 (Grupo B): en `reto-03,05,06,07/eleloi/pyproject.toml` subir constraints:
  - `black = "^22.3.0"` → "^26.10.1"
  - `pyd'antic = "^1.9.0"` → "^1.10.13"
  - `pytest = "^7.1.2"` → "^9.0.3" (reto-03, 06, 07)
  - reto-05 usa `pytest-cov = "^3.0.0"` y `coverage = "^6.3.2"`; si bloquean pytest 9, subirlos mínimamente (`pytest-cov ^6`, `coverage ^7`) para permitir la resolución.
- [ ] T3 (Grupo B): regenerar los 4 `poetry.lock` con poetry (instalar poetry en un venv en `/tmp/opencode`). Formato lock v1.1 actual; poetry moderno generará lock-version 2.x (diff grande pero válido).
- [ ] T4 (Grupo C): editar `reto-04/eleloi/pyproject.toml`: `black = "^22.3.0"` → "^26.10.1".
- [ ] T5: validar que en cada lock regenerado `black>=26.10.1`, `pydantic>=1.10.13`, `pytest>=9.0.3`, y que Pillow en los requirements es `>=13.0.0 `.
- [ ] T6: commit en rama `feature/fix-dependabot-alerts` y PR a `main `.

## Validación / Criterios de aceptación
- `rg` confirma `Pillow>=13.0.0` en ambos requirements.
- `rg` confirma versiones seguras en los 4 locks.
- Los `pyproject.toml` de eleloi declaran los constraints nuevos.
- Tras merge, las 112 alertas Dependabot pasan a `fixed `.
- No se rompe ningún proyecto: los tests de `reto-05/06/07/eleloi` (pytest) deben poder ejecutarse si el entorno lo permite (opcional, informativo).

## Fuera de alcance
- Refactors de código, cambios funcionales, `reto-12/atareao` (venv sin trackear, sin alertas).