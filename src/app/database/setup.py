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
    Boolean,
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
    vencimento = Column(DateTime, nullable=True)
    prioridade = Column(Integer, nullable=False, default=4, server_default="4")
    prazo = Column(DateTime, nullable=True)
    local = Column(String, nullable=True)
    tag = Column(String, nullable=True)
    completa = Column(Boolean, nullable=False, default=False)

    lembretes = relationship("Lembrete", back_populates="tarefa")

    def __init__(
        self,
        titulo,
        descricao,
        vencimento=None,
        prioridade=None,
        prazo=None,
        local=None,
        tag=None,
        completa=False,
    ):
        self.titulo = titulo
        self.descricao = descricao
        self.vencimento = vencimento
        self.prioridade = prioridade
        self.prazo = prazo
        self.local = local
        self.tag = tag
        self.completa = completa


class Lembrete(Base):
    __tablename__ = "lembretes"
    id = Column(Integer, primary_key=True)
    data = Column(DateTime, nullable=False)
    dada_exibida = Column(String, nullable=False)
    tab_selecionada = Column(Integer, nullable=False)
    tarefa_id = Column(Integer, ForeignKey("tarefas.id"))

    tarefa = relationship("Tarefa", back_populates="lembretes")

    def __init__(self, data,dada_exibida,tab_selecionada, tarefa):
        self.data = data
        self.dada_exibida = dada_exibida
        self.tab_selecionada = tab_selecionada
        self.tarefa = tarefa


class MyProjects(Base):
    __tablename__ = "myprojects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    space_work = Column(Integer, nullable=False)
    visualize = Column(String, nullable=False)
    favorite = Column(Boolean,default=False)

    def __init__(self, name, color, space_work, favorite, visualize):
        self.name = name
        self.color = color
        self.space_work = space_work
        self.favorite = favorite
        self.visualize = visualize
