from .setup import Tarefa, Session, Lembrete, MyProjects
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


def salvar_tarefa(tarefas, lembretes):
    with session_scope() as session:
        tarefa = Tarefa(*tarefas)
        session.add(tarefa)
        for lembrete in lembretes:
            lembrete = Lembrete(*lembrete, tarefa=tarefa)
            session.add(lembrete)


def save_projetc(projetos):
    with session_scope() as session:
        projeto = MyProjects(*projetos)
        session.add(projeto)


def listar_projetc():
    with session_scope() as session:
        projetos = session.query(MyProjects).all()
        projetos_lista = []
        for projeto in projetos:
            projeto_dict = [
                projeto.id,
                projeto.name,
                projeto.color,
                projeto.space_work,
                projeto.favorite,
                projeto.visualize,
            ]
            projetos_lista.append(projeto_dict)
        return projetos_lista


def list_tasks(tarefa):
    tarefa_dict = [
        tarefa.id,
        tarefa.titulo,
        tarefa.prioridade,
        tarefa.descricao,
        tarefa.vencimento,
        tarefa.prazo,
        tarefa.local,
        tarefa.tag,
        tarefa.completa,
    ]

    return tarefa_dict


def listar_tarefas():
    with session_scope() as session:
        tarefas = session.query(Tarefa).all()
        tarefas_lista = []
        for tarefa in tarefas:
            tarefas_lista.append(list_tasks(tarefa))
        return tarefas_lista


def search_tarefa(id):
    with session_scope() as session:
        tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
        return list_tasks(tarefa)

def search_lembretes(id):
    with session_scope() as session:
        lembretes = session.query(Lembrete).filter(Lembrete.tarefa_id == id).all()
        return [(lembretes.data, lembretes.dada_exibida, lembretes.tab_selecionada) for lembretes in lembretes]
    
def update_task_db(tarefas, lembretes):
    with session_scope() as session:
        id, titulo, descricao, vencimento, prioridade, prazo, local, tag, completa = tarefas
        
        tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
        
        if not tarefa:
            raise ValueError(f"Tarefa com ID {id} não encontrada.")

        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.vencimento = vencimento
        tarefa.prioridade = prioridade
        tarefa.prazo = prazo
        tarefa.local = local
        tarefa.tag = tag
        tarefa.completa = completa

        
        for lembrete in session.query(Lembrete).filter(Lembrete.tarefa_id == id).all():
            session.delete(lembrete)

        for lembrete in lembretes:
            lembrete = Lembrete(*lembrete, tarefa=tarefa)
            session.add(lembrete)

