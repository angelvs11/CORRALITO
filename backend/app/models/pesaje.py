"""Modelo Pesaje: registro de peso de un animal."""
from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Pesaje(Base):
    """Peso en kg. Ganancia diaria = (peso final - peso inicial) / dias."""

    __tablename__ = 'pesajes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animales.id'), index=True)
    fecha: Mapped[date] = mapped_column(Date)
    peso_kg: Mapped[float] = mapped_column(Numeric(6, 2))
    tipo: Mapped[str | None] = mapped_column(String(30))  # nacimiento, destete, rutina...
    registrado_por: Mapped[int | None] = mapped_column(ForeignKey('usuarios.id'), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
