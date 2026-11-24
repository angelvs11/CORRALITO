"""Crea la app y registra los routers."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import inicio, salud

app = FastAPI(title='OviApp')
app.mount('/static', StaticFiles(directory=str(Path(__file__).parent / 'static')), name='static')

# Cada modulo agrega aqui su router: app.include_router(animales.router)
app.include_router(salud.router)
app.include_router(inicio.router)
