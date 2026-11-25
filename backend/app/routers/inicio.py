"""Pagina de inicio."""
from fastapi import APIRouter, Request

from app.core.plantillas import plantillas

router = APIRouter()


@router.get('/')
def inicio(request: Request):
    """Pantalla de bienvenida con el menu principal."""
    return plantillas.TemplateResponse(request, 'inicio/inicio.html', {})
