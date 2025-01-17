from datetime import datetime, timedelta

# Captura o horário atual
now = datetime.now()

# Cria uma lista para armazenar os horários
horarios = []

# Define um horário de início baseado no horário atual
current_time = now.replace(second=0, microsecond=0)

# Define o final do dia
end_of_day = current_time.replace(hour=23, minute=59)

# Itera de 15 em 15 minutos até o final do dia
while current_time <= end_of_day:
    horarios.append(current_time.strftime("%H:%M"))
    current_time += timedelta(minutes=15)

# Imprime os horários
for horario in horarios:
    print(horario)