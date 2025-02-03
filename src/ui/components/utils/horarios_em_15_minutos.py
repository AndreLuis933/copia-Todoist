from datetime import datetime, timedelta
from .locale_config import temp_locale

def gerar_horarios_24h_15min_intervalo():
    with temp_locale('en_US.UTF-8'):
        now = datetime.now()

        minutes_to_add = (15 - now.minute % 15) % 15
        if minutes_to_add == 0:
            minutes_to_add = 15

        current_time = now + timedelta(minutes=minutes_to_add)
        current_time = current_time.replace(second=0, microsecond=0)

        horarios = []

        end_time = now + timedelta(days=1)
        end_time = end_time.replace(
            hour=now.hour, minute=current_time.minute, second=0, microsecond=0
        )

        while current_time < end_time:
            horarios.append(current_time.strftime("%I:%M %p"))
            current_time += timedelta(minutes=15)
    return horarios

def gerar_duracoes_ate_23h30():
    intervalos = ['Sem duração']
    total_minutos = 23 * 60 + 30  # Total de minutos até 23h30
    minutos = 15

    while minutos <= total_minutos:
        horas = minutos // 60
        minutos_restantes = minutos % 60

        if horas > 0 and minutos_restantes > 0:
            intervalos.append(f"{horas}h{minutos_restantes}m")
        elif horas > 0:
            intervalos.append(f"{horas}h")
        else:
            intervalos.append(f"{minutos_restantes}m")
        
        # Após a primeira hora, os intervalos passam a ser de 30 minutos
        if minutos < 60:
            minutos += 15
        else:
            minutos += 30

    return intervalos