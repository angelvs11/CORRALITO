"""Seguridad: hash de contrasenas con bcrypt (passlib)."""
from passlib.context import CryptContext

_contexto = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hashear_contrasena(contrasena):
    """Devuelve el hash bcrypt de una contrasena (nunca se guarda en texto plano)."""
    return _contexto.hash(contrasena)


def verificar_contrasena(contrasena, hash_guardado):
    """True si la contrasena coincide con el hash guardado."""
    return _contexto.verify(contrasena, hash_guardado)
