"""Modelos Ingrediente (catalogo global) y PrecioIngrediente (precio por rancho)."""
from sqlalchemy import ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Ingrediente(Base):
    """Catalogo de ingredientes. El % de proteina es fijo; no lleva rancho_id
    porque es un catalogo compartido por todos los ranchos."""

    __tablename__ = 'ingredientes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    proteina_pct: Mapped[float] = mapped_column(Numeric(5, 2))


class PrecioIngrediente(Base):
    """Precio por kg que cada productor edita para su rancho."""

    __tablename__ = 'precios_ingredientes'
    __table_args__ = (
        UniqueConstraint('rancho_id', 'ingrediente_id', name='uq_precios_rancho_ingrediente'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    ingrediente_id: Mapped[int] = mapped_column(ForeignKey('ingredientes.id'))
    precio_kg: Mapped[float] = mapped_column(Numeric(10, 2))
