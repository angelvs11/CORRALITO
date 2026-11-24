# backend

API en Python 3.12 con FastAPI + SQLAlchemy 2.x + Alembic y pantallas Jinja2 mobile-first (stack definido en SETUP-03; reglas en `AGENTS.md`).

Responsables: Samuel (nucleo), Fredy (nacimientos, pesajes, Excel), Javier (alimentacion, sanidad), Monica (indicadores, reportes), Ioannis (esqueleto e infraestructura).

## Estructura

| Ruta | Contenido |
|---|---|
| `app/main.py` | Crea la app y registra los routers |
| `app/core/` | `config.py` (lee .env), `db.py` (sesion, `get_db`, `Base`), `security.py` (bcrypt), `plantillas.py` (Jinja2) |
| `app/models/` | Un archivo por entidad |
| `app/schemas/` | Modelos Pydantic de entrada/salida |
| `app/routers/` | Un archivo por modulo (ya estan `salud` e `inicio`) |
| `app/services/` | Logica de negocio |
| `app/templates/` | `base.html` (menu mobile-first) y una carpeta por modulo |
| `app/static/` | css, js, imagenes |
| `alembic/` | Migraciones |
| `tests/` | `test_<modulo>.py` |

## Correrlo en local

1. En la raiz del repo, copia `.env.example` como `.env` (no se sube a GitHub).
2. Levanta PostgreSQL local (opcional, para probar la BD): `cd backend && docker compose up -d`.
3. Instala y corre:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abre `http://localhost:8000/` (inicio) y `http://localhost:8000/api/salud`. Con la BD arriba debe decir `base_de_datos: ok`.

## Pruebas

```bash
pytest
```

No necesitan base de datos.

## Como agregar tu parte

- **Un router:** crea `app/routers/<modulo>.py` con `router = APIRouter()` y registralo en `app/main.py` (`app.include_router(<modulo>.router)`). Usa `Depends(get_db)` para la sesion.
- **Un modelo:** crea `app/models/<entidad>.py` heredando de `Base` (`app.core.db`), importalo en `app/models/__init__.py` y genera la migracion:
  ```bash
  alembic revision --autogenerate -m "descripcion"
  alembic upgrade head
  ```
- **Una pantalla:** crea `app/templates/<modulo>/<pantalla>.html` con `{% extends 'base.html' %}` y respondela con `plantillas.TemplateResponse(request, '<modulo>/<pantalla>.html', {...})` (`from app.core.plantillas import plantillas`).
- **Una prueba:** `tests/test_<modulo>.py`.

Los cambios a `models/` y `core/` son compartidos: van en un PR propio y se avisan al equipo.
