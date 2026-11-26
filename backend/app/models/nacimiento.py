"""Modelo Nacimiento: evento de parto de una madre (la tarjeta lo llama partos)."""
from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Nacimiento(Base):
    """Parto registrado. El productor no lo edita ni borra; solo asociacion/tecnico
    corrigen, dejando rastro en bitacora_correcciones."""

    __tablename__ = 'nacimientos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    madre_id: Mapped[int] = mapped_column(ForeignKey('animales.id'), index=True)
    padre_id: Mapped[int | None] = mapped_column(ForeignKey('animales.id'), nullable=True)
    fecha_parto: Mapped[date] = mapped_column(Date, index=True)
    crias_nacidas: Mapped[int] = mapped_column(Integer, default=1)  # prolificidad = crias / partos
    crias_vivas: Mapped[int | None] = mapped_column(Integer)
    fecha_destete: Mapped[date | None] = mapped_column(Date)  # se llena al confirmar el destete
    foto_url: Mapped[str | None] = mapped_column(String(500))
    observaciones: Mapped[str | None] = mapped_column(Text)
    registrado_por: Mapped[int | None] = mapped_column(ForeignKey('usuarios.id'), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())

    madre = relationship('Animal', foreign_keys=[madre_id])
    padre = relationship('Animal', foreign_keys=[padre_id])
