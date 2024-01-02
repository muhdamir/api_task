from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = "admin"
PASSWORD = "secret"
HOST = "localhost"
PORT = "8083"
DATABASE = "dev"

engine = create_engine(
    url=f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}",
    echo=True,
    pool_pre_ping=True,
)

SessionFactory = sessionmaker(
    bind=engine,
    autoflush=True,
)


def get_session():
    session = SessionFactory()
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        session.close()
