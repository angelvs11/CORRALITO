"""Importa todos los modelos para que Alembic los vea en Base.metadata."""
from app.models.asociacion import Asociacion
from app.models.rancho import Rancho
from app.models.usuario import Usuario
from app.models.corral import Corral
from app.models.animal import Animal
from app.models.nacimiento import Nacimiento
from app.models.pesaje import Pesaje
from app.models.evento_sanitario import EventoSanitario
from app.models.ingrediente import Ingrediente, PrecioIngrediente
from app.models.formula import Formula, FormulaIngrediente
from app.models.baja import Baja
from app.models.bitacora_correccion import BitacoraCorreccion

__all__ = [
    'Asociacion', 'Rancho', 'Usuario', 'Corral', 'Animal', 'Nacimiento',
    'Pesaje', 'EventoSanitario', 'Ingrediente', 'PrecioIngrediente',
    'Formula', 'FormulaIngrediente', 'Baja', 'BitacoraCorreccion',
]
