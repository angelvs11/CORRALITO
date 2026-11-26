"""Modelo Usuario: productor, trabajador (cuenta rama), asociacion o tecnico."""
from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

ROLES = ('productor', 'trabajador', 'asociacion', 'tecnico')


class Usuario(Base):
    """Usuario del sistema. asociacion/tecnico pueden no tener rancho propio."""

    __tablename__ = 'usuarios'
    __table_args__ = (
        CheckConstraint(
            "rol IN ('productor', 'trabajador', 'asociacion', 'tecnico')",
            name='ck_usuarios_rol'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int | None] = mapped_column(
        ForeignKey('ranchos.id'), nullable=True, index=True)
    asociacion_id: Mapped[int | None] = mapped_column(
        ForeignKey('asociaciones.id'), nullable=True, index=True)
    nombre: Mapped[str] = mapped_column(String(150))
    correo: Mapped[str] = mapped_column(String(200), unique=True)
    contrasena_hash: Mapped[str] = mapped_column(String(255))  # bcrypt (passlib)
    rol: Mapped[str] = mapped_column(String(20))
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())

    rancho = relationship('Rancho')
    asociacion = relationship('Asociacion')
