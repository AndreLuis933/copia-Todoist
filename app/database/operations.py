from .setup import Tarefa, Session


def salvar_tarefa(tarefas):
    tarefa = Tarefa(nome=tarefas[0], descricao=tarefas[1])
    session = Session()
    try:
        session.add(tarefa)
        session.commit()
        print("Tarefa salva com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar tarefa: {e}")
        session.rollback()
    finally:
        session.close()
        
def listar_tarefas():
    session = Session()
    tarefas = session.query(Tarefa).all()
    session.close()
    return tarefas