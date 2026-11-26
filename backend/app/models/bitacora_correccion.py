"""Modelo BitacoraCorreccion: rastro de correcciones hechas por asociacion/tecnico."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class BitacoraCorreccion(Base):
    """Valor anterior, valor nuevo, motivo, usuario y fecha de cada correccion."""

    __tablename__ = 'bitacora_correcciones'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rancho_id: Mapped[int] = mapped_column(ForeignKey('ranchos.id'), index=True)
    tabla: Mapped[str] = mapped_column(String(60))
    registro_id: Mapped[int] = mapped_column()
    campo: Mapped[str] = mapped_column(String(60))
    valor_anterior: Mapped[str | None] = mapped_column(Text)
    valor_nuevo: Mapped[str | None] = mapped_column(Text)
    motivo: Mapped[str] = mapped_column(Text)
    foto_evidencia_url: Mapped[str | None] = mapped_column(String(500))
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'))
    fecha: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())
