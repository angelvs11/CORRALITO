"""Modelo Baja: registro de la salida de un animal (el animal no se borra)."""
from datetime import date, datetime

from sqlalchemy import CheckConstraint, Date, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Baja(Base):
    """Baja por venta, muerte o desecho. Debe actualizar animales.estado y fecha_baja."""

    __tablename__ = 'bajas'
    __table_args__ = (
        CheckConstraint("tipo IN ('vendido', 'muerto', 'desecho')", name='ck_bajas_tipo'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animales.id'), index=True)
    fecha: Mapped[date] = mapped_column(Date)
    tipo: Mapped[str] = mapped_column(String(10))
    motivo: Mapped[str | None] = mapped_column(Text)
    precio: Mapped[float | None] = mapped_column(Numeric(10, 2))
    comprador: Mapped[str | None] = mapped_column(String(150))
    registrado_por: Mapped[int | None] = mapped_column(ForeignKey('usuarios.id'), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
