"""Pruebas del modelo de datos (CORE-01): crea todas las tablas en SQLite en memoria."""
from sqlalchemy import create_engine, inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.core.db import Base
import app.models  # noqa: F401  (registra los modelos en Base.metadata)
from app.models import Animal, Rancho, Usuario

TABLAS = {
    'asociaciones', 'ranchos', 'usuarios', 'corrales', 'animales', 'nacimientos',
    'pesajes', 'eventos_sanitarios', 'ingredientes', 'precios_ingredientes',
    'formulas', 'formulas_ingredientes', 'bajas', 'bitacora_correcciones',
}


def _sesion():
    """Sesion sobre una BD SQLite en memoria con todas las tablas."""
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine)()


def test_se_crean_todas_las_tablas():
    engine, _ = _sesion()
    assert TABLAS <= set(inspect(engine).get_table_names())


def test_animal_tiene_columnas_separadas():
    columnas = Animal.__table__.columns.keys()
    for col in ('sexo', 'etapa', 'estado_reproductivo', 'estado', 'fecha_baja', 'motivo_baja', 'rancho_id'):
        assert col in columnas


def test_folio_unico_por_rancho():
    _, db = _sesion()
    db.add(Rancho(nombre='R1'))
    db.flush()
    db.add(Animal(rancho_id=1, folio='A1', sexo='hembra'))
    db.add(Animal(rancho_id=1, folio='A1', sexo='macho'))
    try:
        db.flush()
        assert False, 'debio fallar por folio repetido'
    except IntegrityError:
        db.rollback()


def test_rol_invalido_se_rechaza():
    _, db = _sesion()
    db.add(Usuario(nombre='X', correo='x@x.com', contrasena_hash='h', rol='dios'))
    try:
        db.flush()
        assert False, 'debio fallar por rol invalido'
    except IntegrityError:
        db.rollback()
