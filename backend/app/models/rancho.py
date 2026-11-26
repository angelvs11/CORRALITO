"""Modelo Rancho: unidad de aislamiento de datos del sistema."""
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Rancho(Base):
    """Rancho ovino. Todas las tablas de datos cuelgan de aqui via rancho_id."""

    __tablename__ = 'ranchos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    asociacion_id: Mapped[int | None] = mapped_column(
        ForeignKey('asociaciones.id'), nullable=True, index=True)
    nombre: Mapped[str] = mapped_column(String(150))
    municipio: Mapped[str | None] = mapped_column(String(100))
    estado_geografico: Mapped[str | None] = mapped_column(String(100))
    dias_destete: Mapped[int] = mapped_column(Integer, default=75)  # configurable por rancho
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())

    asociacion = relationship('Asociacion')
