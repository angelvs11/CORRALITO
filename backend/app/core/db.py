"""Engine y sesion de SQLAlchemy."""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import config

# El engine no se conecta hasta que se usa: importar esto no requiere BD
engine = create_engine(config.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Todos los modelos de app/models heredan de Base (Alembic la usa)
Base = declarative_base()


def get_db():
    """Dependencia de FastAPI: entrega una sesion por peticion y la cierra."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def base_de_datos_ok():
    """True si la BD responde a un SELECT 1."""
    try:
        with engine.connect() as conn:
            conn.execute(text('SELECT 1'))
        return True
    except Exception:
        return False
