"""Modelo Corral: division fisica del rancho donde se ubican los animales."""
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Corral(Base):
    """Corral o potrero de un rancho."""

    __tablename__ = 'corrales'
    __table_args__ = (UniqueConstraint('rancho_id', 'nombre', name='uq_corrales_rancho_nombre'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    nombre: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str | None] = mapped_column(String(255))
