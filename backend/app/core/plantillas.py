"""Motor de plantillas Jinja2 compartido por todos los routers."""
from pathlib import Path

from fastapi.templating import Jinja2Templates

plantillas = Jinja2Templates(directory=str(Path(__file__).resolve().parents[1] / 'templates'))
