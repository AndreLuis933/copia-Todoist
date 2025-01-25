from sqlalchemy import (
    DateTime,
    Time,
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


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "TODO.db")
ENGINE = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=ENGINE)

Base = declarative_base()


class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    vencimento = Column(Date, nullable=True)
    prioridade = Column(Integer, nullable=False, default=4, server_default="4")
    lembrete = Column(DateTime, nullable=True)
    prazo = Column(Time, nullable=True)
    local = Column(String, nullable=True)
    tag = Column(String, nullable=True)

    def __init__(
        self,
        titulo,
        descricao,
        vencimento=None,
        prioridade=None,
        lembrete=None,
        prazo=None,
        local=None,
        tag=None,
    ):
        self.titulo = titulo
        self.descricao = descricao
        self.vencimento = vencimento
        self.prioridade = prioridade
        self.lembrete = lembrete
        self.prazo = prazo
        self.local = local
        self.tag = tag
