"""Modelo Asociacion: agrupa ranchos (la usa el rol asociacion)."""
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Asociacion(Base):
    """Asociacion ganadera a la que pertenecen varios ranchos."""

    __tablename__ = 'asociaciones'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(150), unique=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
