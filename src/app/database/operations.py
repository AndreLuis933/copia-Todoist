from .setup import Tarefa, Session, Lembrete
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager

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


def salvar_tarefa(tarefas,lembretes):
    with session_scope() as session:
        print(tarefas)
        tarefa = Tarefa(*tarefas)
        session.add(tarefa)
        session.commit()
        for data_lembrete in lembretes:
            lembrete = Lembrete(data=data_lembrete, tarefa=tarefa)
            session.add(lembrete)
        print("Tarefa salva com sucesso!")

        
def listar_tarefas():
    with session_scope() as session:
        tarefas = session.query(Tarefa).all()
        tarefas_lista = []
        for tarefa in tarefas:
            tarefa_dict = [
                tarefa.id,
                tarefa.titulo,
                tarefa.prioridade,
                tarefa.descricao,
                tarefa.vencimento,
                tarefa.prazo,
                #tarefa.lembretes,
                tarefa.local,
                tarefa.tag
            ]
            tarefas_lista.append(tarefa_dict)
        return tarefas_lista