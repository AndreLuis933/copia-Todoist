from app.database.operations import listar_tarefas, salvar_tarefa


for i in range(20):
    salvar_tarefa(['teste', 'teste', None, 1, None, None, None, None])


