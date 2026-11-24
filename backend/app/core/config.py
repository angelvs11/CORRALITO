"""Configuracion: lee las variables de entorno (o el archivo .env)."""
import os
from pathlib import Path

from dotenv import load_dotenv

# El .env vive en la raiz del repo (junto a .env.example). En el servidor
# las variables vienen del entorno y el archivo no existe.
load_dotenv(Path(__file__).resolve().parents[3] / '.env')


def _armar_database_url():
    """Devuelve la URL de la BD: DATABASE_URL, o se arma con las variables DB_*."""
    url = os.environ.get('DATABASE_URL')
    if url:
        # Acepta postgresql:// y la convierte al driver psycopg
        return url.replace('postgresql://', 'postgresql+psycopg://', 1)
    usuario = os.environ.get('DB_USER', '')
    clave = os.environ.get('DB_PASSWORD', '')
    host = os.environ.get('DB_HOST', 'localhost')
    puerto = os.environ.get('DB_PORT', '5432')
    nombre = os.environ.get('DB_NAME', 'oviapp')
    return f'postgresql+psycopg://{usuario}:{clave}@{host}:{puerto}/{nombre}'


class Configuracion:
    """Valores de configuracion de la app."""

    def __init__(self):
        self.database_url = _armar_database_url()
        self.aws_region = os.environ.get('AWS_REGION', 'us-east-1')
        self.s3_bucket_fotos = os.environ.get('S3_BUCKET_FOTOS', '')
        self.secret_key = os.environ.get('SECRET_KEY', '')


config = Configuracion()
