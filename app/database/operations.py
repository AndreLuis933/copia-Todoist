from .setup import Tarefa, Session
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from inspect import signature

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()


def salvar_tarefa(tarefas):
    with session_scope() as session:
        tarefa = Tarefa(titulo=tarefas[0], descricao=tarefas[1])
        session.add(tarefa)
        session.commit()
        print("Tarefa salva com sucesso!")

        
def listar_tarefas():
    with session_scope() as session:
        print(list(signature(Tarefa.__init__).parameters.keys())[1:])
        tarefas = session.query(Tarefa).all()
        tarefas_lista = []
        for tarefa in tarefas:
            tarefa_dict = {
                'id': tarefa.id,
                'titulo': tarefa.nome,
                'descricao': tarefa.descricao,
            }
            tarefas_lista.append(tarefa_dict)
        return tarefas_lista