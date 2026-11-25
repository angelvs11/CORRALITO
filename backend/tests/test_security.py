"""Pruebas del hash de contrasenas."""
from app.core.security import hashear_contrasena, verificar_contrasena


def test_hash_y_verificacion():
    h = hashear_contrasena('secreto123')
    assert h != 'secreto123'
    assert verificar_contrasena('secreto123', h)
    assert not verificar_contrasena('otra', h)
