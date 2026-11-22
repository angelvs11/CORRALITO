# CORRALITO - OviApp

Aplicación móvil + panel web para la gestión de ranchos ovinos (AgroTech / UAG).

Tablero de tareas: https://trello.com/b/Txx6Jo8T/agrotech-oviapp

## Equipo

| Integrante | Área |
|---|---|
| Samuel González | Núcleo: BD, login, roles, ficha, inventario, genealogía, offline |
| Fredy Serrano | Nacimientos, pesajes, Sábana Excel |
| Javier Arce | Alimentación, destete, sanidad |
| Mónica Rodríguez | Indicadores, mortalidad, reportes |
| Ángel Valencia | AWS: cuenta, RDS, S3, seguridad |
| Ioannis Kafkarisios | AWS: backend, CI/CD, sincronización |

## Estructura

| Carpeta | Contenido |
|---|---|
| `backend/` | API en Python |
| `mobile/` | App móvil |
| `infra/` | Infraestructura AWS |
| `docs/` | Diagramas y documentación |

## Flujo de trabajo

1. `git checkout develop` y `git pull`
2. `git checkout -b feature/ID-descripcion` (ID = el de la tarjeta de Trello, ej. `feature/NAC-01-registro-partos`)
3. Commits con el formato `tipo(ID): mensaje` (tipos: feat, fix, docs, refactor, test, chore)
4. `git push -u origin feature/ID-descripcion` y abrir Pull Request hacia `develop`
5. Otro integrante revisa y aprueba; se hace merge y la tarjeta pasa a "Hecho"
6. Al cierre de cada entrega: Pull Request de `develop` a `main`

**Reglas:** nunca hacer push directo a `main` ni a `develop`, y nunca subir el archivo `.env`.

## Correr el backend localmente

```bash
cd backend
python -m venv venv
source venv/bin/activate   # en Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest
```
