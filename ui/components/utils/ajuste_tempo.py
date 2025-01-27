from datetime import timedelta

def ajusta_tempo(descricao):
    ajustes = {
        "No horário da tarefa": timedelta(),
        "10 min antes": timedelta(minutes=-10),
        "30 min antes": timedelta(minutes=-30),
        "45 min antes": timedelta(minutes=-45),
        "1 hora antes": timedelta(hours=-1),
        "2 horas antes": timedelta(hours=-2),
        "3 horas antes": timedelta(hours=-3),
        "1 dia antes": timedelta(days=-1),
        "2 dias antes": timedelta(days=-2),
        "3 dias antes": timedelta(days=-3),
        "1 semana antes": timedelta(weeks=-1),
    }
    
    ajuste = ajustes.get(descricao)
    if ajuste is not None:
        return ajuste
    else:
        raise ValueError("Descrição de tempo inválida.")