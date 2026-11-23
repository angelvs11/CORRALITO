# Instrucciones para asistentes de IA (Claude, Copilot, ChatGPT, Cursor)

Lee este archivo completo antes de generar codigo para este repositorio. Todo el equipo usa IA; estas reglas hacen que el codigo de los 6 integrantes embone.

## Proyecto

OviApp: gestion de ranchos ovinos (AgroTech / UAG). Productor, trabajadores (cuentas rama) y Asociacion/Tecnico. Entrega del prototipo: viernes 27 de noviembre de 2026.
Tareas y responsables: https://trello.com/b/Txx6Jo8T/agrotech-oviapp

## Stack (no cambiar sin acuerdo del equipo)

- Python 3.12 + FastAPI
- SQLAlchemy 2.x (ORM) + Alembic (migraciones)
- PostgreSQL (Amazon RDS en produccion; local con Docker o la URL que de Angel)
- Pantallas: plantillas Jinja2 que genera el mismo backend, mobile-first (botones grandes, una columna). Sin frameworks de frontend.
- Contrasenas con bcrypt (passlib); sesion con cookie firmada
- Excel: openpyxl
- Pruebas: pytest + TestClient de FastAPI
- Fotos: Amazon S3 (en local se guardan en una carpeta)

## Estructura de carpetas

```
backend/
  app/
    main.py              # crea la app y registra los routers
    core/                # config.py (lee .env), db.py (sesion SQLAlchemy), security.py
    models/              # un archivo por entidad: rancho.py, usuario.py, animal.py, nacimiento.py, pesaje.py ...
    schemas/             # modelos Pydantic de entrada/salida
    routers/             # un archivo por modulo: auth, ranchos, animales, nacimientos, pesajes, alimentacion, sanidad, indicadores, sabana
    services/            # logica de negocio (calculos, reglas, validaciones)
    templates/<modulo>/  # pantallas HTML
    static/              # css, js, imagenes
  alembic/               # migraciones
  tests/test_<modulo>.py
  requirements.txt
```

## Convenciones

- Tablas y columnas en espanol, snake_case, sin acentos ni enie: `animales`, `fecha_nacimiento`, `anio`. Clases en PascalCase singular: `Animal`, `Nacimiento`.
- Llave primaria: `id` entero autoincremental. Folio, arete, SINIIGA y folio de registro son campos de negocio, nunca llaves.
- Toda tabla de datos del rancho lleva `rancho_id`. Toda consulta filtra por el rancho del usuario en sesion; solo los roles `asociacion` y `tecnico` ven varios ranchos.
- Nunca borrar animales: usar `estado` (activo, vendido, muerto, desecho) + `fecha_baja` + `motivo_baja`.
- Sexo, etapa de vida y estado reproductivo son columnas separadas, no un solo campo.
- API JSON en `/api/<recurso>` (plural); paginas HTML en `/<modulo>/...`.
- Fechas en ISO (YYYY-MM-DD), zona America/Mexico_City.
- Configuracion y secretos solo por variables de entorno (ver `.env.example`). Nunca escribir contrasenas o llaves en el codigo.
- Funciones cortas, con docstring en espanol.

## Reglas de negocio que el codigo debe respetar

- Nacimientos: el productor solo puede registrar partos de los ultimos 30 dias y no puede editar ni borrar un nacimiento guardado. Solo `asociacion`/`tecnico` corrigen, con foto de evidencia y bitacora (valor anterior, valor nuevo, motivo, usuario, fecha).
- Destete: fecha de nacimiento + 75 dias (configurable por rancho). Al confirmar el destete la madre pasa de Lactancia a Mantenimiento.
- Indicadores (Excel del Mtro. Melendez): % prenez = prenadas / expuestas; % partos = paridas / prenadas; prolificidad = crias nacidas / partos; ganancia diaria = (peso final - peso inicial) / dias.
- Ingredientes: el % de proteina es fijo (catalogo); el precio por kg lo edita cada productor.

## Flujo Git

- Rama desde `develop`: `feature/<ID-tarjeta>-descripcion` (ej. `feature/NAC-01-registro-partos`).
- Commits: `tipo(ID): mensaje` (feat, fix, docs, refactor, test, chore).
- Pull Request hacia `develop`; `pytest` debe pasar y otro integrante aprueba.
- Cambios a `models/` o `core/` (compartidos) van en un PR propio y se avisan al equipo.

## Instrucciones para la IA

- Antes de crear un modelo o un router, revisa `models/` y `routers/` para no duplicar.
- Respeta la estructura y las convenciones de arriba aunque el usuario no las mencione.
- Si necesitas una libreria nueva, agregala a `requirements.txt` con version fija.
- Por cada endpoint nuevo, escribe su prueba en `tests/test_<modulo>.py`.
- No modifiques archivos de otro modulo salvo que sea indispensable; si lo haces, dilo en tu respuesta.
