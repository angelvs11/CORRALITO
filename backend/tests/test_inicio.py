"""Pruebas de la pagina de inicio y de los archivos estaticos."""
from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_inicio():
    r = cliente.get('/')
    assert r.status_code == 200
    assert 'OviApp' in r.text
    assert 'viewport' in r.text


def test_css_estatico():
    r = cliente.get('/static/css/estilos.css')
    assert r.status_code == 200
