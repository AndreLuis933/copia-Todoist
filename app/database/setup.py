from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    LargeBinary,
)
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime, timezone
import os



BASE_DIR =os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "TODO.db")
ENGINE = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=ENGINE)

Base = declarative_base()


class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
