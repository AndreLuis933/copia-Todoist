from datetime import datetime, timedelta

DIAS_SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
DIAS_SEMANA_COMPLETOS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira","Sexta-feira", "Sábado", "Domingo"]
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

def identificar_datas():
    hoje = datetime.now()
    
    resultados = {
        "Hoje": hoje,
        "Amanha": hoje + timedelta(days=1),
        "Proxima semana": hoje + timedelta(days=(7 - hoje.weekday()) % 7),
        "Proximo fim de semana": hoje + timedelta(days=(5 - hoje.weekday() + 7) % 7 or 7),
        'Sem vencimento': None,
    }
    
    return resultados