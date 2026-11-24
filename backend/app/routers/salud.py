"""Endpoint de salud: sirve para saber si el backend y la BD estan arriba."""
from fastapi import APIRouter

from app.core.db import base_de_datos_ok

router = APIRouter()


@router.get('/api/salud')
def salud():
    """Estado del backend y de la conexion a la base de datos."""
    bd = base_de_datos_ok()
    return {
        'estado': 'ok' if bd else 'degradado',
        'base_de_datos': 'ok' if bd else 'sin_conexion',
    }
