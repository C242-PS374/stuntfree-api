from typing import Generator
from contextlib import contextmanager

from sqlmodel import SQLModel, Session, create_engine

class Database:
    def __init__(self, db_url: str) -> None:
        # Create engine with connection pooling
        self._engine = create_engine(
            db_url,
            echo=False,  # Set to True to see SQL queries
            pool_pre_ping=True  # Enable connection health checks
        )

    def create_database(self) -> None:
        """Create all tables defined in SQLModel classes"""
        SQLModel.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """Provide a transactional scope around a series of operations"""
        session = Session(self._engine)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.expunge_all()
            session.close()