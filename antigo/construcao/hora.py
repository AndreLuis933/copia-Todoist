from datetime import datetime, timedelta

# Captura o horário atual
now = datetime.now()

# Ajusta o próximo horário múltiplo de 15 minutos
minutes_to_add = (15 - now.minute % 15) % 15
if minutes_to_add == 0:
    minutes_to_add = 15

# Ajusta o tempo inicial ao próximo múltiplo de 15 minutos
current_time = now + timedelta(minutes=minutes_to_add)
current_time = current_time.replace(second=0, microsecond=0)

# Cria uma lista para armazenar os horários
horarios = []

# Define o final do período (mesmo horário no dia seguinte)
end_time = now + timedelta(days=1)
end_time = end_time.replace(hour=now.hour, minute=current_time.minute, second=0, microsecond=0)

# Itera de 15 em 15 minutos até o mesmo horário no dia seguinte
while current_time < end_time:
    horarios.append(current_time.strftime("%H:%M"))
    current_time += timedelta(minutes=15)

# Imprime os horários
for horario in horarios:
    print(horario)