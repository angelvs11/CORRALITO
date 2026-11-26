"""Modelo EventoSanitario: cartilla sanitaria (vacunas, desparasitaciones, tratamientos)."""
from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class EventoSanitario(Base):
    """Evento de sanidad aplicado a un animal."""

    __tablename__ = 'eventos_sanitarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animales.id'), index=True)
    fecha: Mapped[date] = mapped_column(Date)
    tipo: Mapped[str] = mapped_column(String(40))  # vacuna, desparasitacion, tratamiento...
    producto: Mapped[str | None] = mapped_column(String(150))
    dosis: Mapped[str | None] = mapped_column(String(80))
    fecha_proxima: Mapped[date | None] = mapped_column(Date)
    observaciones: Mapped[str | None] = mapped_column(Text)
    registrado_por: Mapped[int | None] = mapped_column(ForeignKey('usuarios.id'), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
