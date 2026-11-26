"""Modelos Formula (racion alimenticia) y FormulaIngrediente (su composicion)."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Formula(Base):
    """Formula de alimentacion de un rancho."""

    __tablename__ = 'formulas'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    nombre: Mapped[str] = mapped_column(String(150))
    descripcion: Mapped[str | None] = mapped_column(String(255))
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())


class FormulaIngrediente(Base):
    """Ingrediente dentro de una formula, con su porcentaje de inclusion."""

    __tablename__ = 'formulas_ingredientes'
    __table_args__ = (
        UniqueConstraint('formula_id', 'ingrediente_id', name='uq_formula_ingrediente'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    formula_id: Mapped[int] = mapped_column(ForeignKey('formulas.id'), index=True)
    ingrediente_id: Mapped[int] = mapped_column(ForeignKey('ingredientes.id'))
    porcentaje: Mapped[float] = mapped_column(Numeric(5, 2))
