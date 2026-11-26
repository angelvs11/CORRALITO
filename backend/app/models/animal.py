"""Modelo Animal: ficha del ovino. Nunca se borra; se da de baja por estado."""
from datetime import date, datetime

from sqlalchemy import CheckConstraint, Date, DateTime, ForeignKey, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

SEXOS = ('hembra', 'macho')
ESTADOS = ('activo', 'vendido', 'muerto', 'desecho')


class Animal(Base):
    """Ovino del rancho. folio, arete y siniiga son campos de negocio, no llaves."""

    __tablename__ = 'animales'
    __table_args__ = (
        UniqueConstraint('rancho_id', 'folio', name='uq_animales_rancho_folio'),
        UniqueConstraint('rancho_id', 'arete', name='uq_animales_rancho_arete'),
        CheckConstraint("sexo IN ('hembra', 'macho')", name='ck_animales_sexo'),
        CheckConstraint(
            "estado IN ('activo', 'vendido', 'muerto', 'desecho')",
            name='ck_animales_estado'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    corral_id: Mapped[int | None] = mapped_column(ForeignKey('corrales.id'), nullable=True)
    folio: Mapped[str] = mapped_column(String(50))
    arete: Mapped[str | None] = mapped_column(String(50))
    siniiga: Mapped[str | None] = mapped_column(String(50), index=True)
    raza: Mapped[str | None] = mapped_column(String(80))
    sexo: Mapped[str] = mapped_column(String(10))
    color: Mapped[str | None] = mapped_column(String(50))
    fecha_nacimiento: Mapped[date | None] = mapped_column(Date)
    madre_id: Mapped[int | None] = mapped_column(ForeignKey('animales.id'), nullable=True, index=True)
    padre_id: Mapped[int | None] = mapped_column(ForeignKey('animales.id'), nullable=True, index=True)

    # Tres columnas separadas (regla de AGENTS.md)
    estado: Mapped[str] = mapped_column(String(10), default='activo')
    etapa: Mapped[str | None] = mapped_column(String(30))  # etapa de vida: cria, destetado, etc.
    estado_reproductivo: Mapped[str | None] = mapped_column(String(30))  # lactancia, mantenimiento...

    criador: Mapped[str | None] = mapped_column(String(150))
    propietario: Mapped[str | None] = mapped_column(String(150))
    motivo_ingreso: Mapped[str | None] = mapped_column(String(100))
    foto_url: Mapped[str | None] = mapped_column(String(500))

    fecha_baja: Mapped[date | None] = mapped_column(Date)
    motivo_baja: Mapped[str | None] = mapped_column(Text)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())

    rancho = relationship('Rancho')
    corral = relationship('Corral')
    madre = relationship('Animal', foreign_keys=[madre_id], remote_side=[id])
    padre = relationship('Animal', foreign_keys=[padre_id], remote_side=[id])
