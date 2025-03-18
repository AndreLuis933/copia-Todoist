import os

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

load_dotenv()

Teste = os.getenv("PRODUTION")

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    if Teste
    else "sqlite:///todoist.db"
)


# Criação do engine e da sessão
ENGINE = create_engine(DATABASE_URL)
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
        vencimento,
        prioridade,
        prazo,
        local,
        tag,
        completa,
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

    def __init__(self, data, dada_exibida, tab_selecionada, tarefa):
        self.data = data
        self.dada_exibida = dada_exibida
        self.tab_selecionada = tab_selecionada
        self.tarefa = tarefa


class MyProjects(Base):
    __tablename__ = "myprojects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    space_work = Column(String, nullable=False)
    visualize = Column(String, nullable=False)
    favorite = Column(Boolean, default=False)

    def __init__(self, name, color, space_work, favorite, visualize):
        self.name = name
        self.color = color
        self.space_work = space_work
        self.favorite = favorite
        self.visualize = visualize


def init_db():
    Base.metadata.create_all(ENGINE)
