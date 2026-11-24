"""Pruebas de /api/salud (la BD se simula: no hace falta tenerla)."""
from fastapi.testclient import TestClient

from app.main import app
from app.routers import salud

cliente = TestClient(app)


def test_salud_con_bd(monkeypatch):
    monkeypatch.setattr(salud, 'base_de_datos_ok', lambda: True)
    r = cliente.get('/api/salud')
    assert r.status_code == 200
    assert r.json() == {'estado': 'ok', 'base_de_datos': 'ok'}


def test_salud_sin_bd(monkeypatch):
    monkeypatch.setattr(salud, 'base_de_datos_ok', lambda: False)
    r = cliente.get('/api/salud')
    assert r.status_code == 200
    assert r.json()['base_de_datos'] == 'sin_conexion'
