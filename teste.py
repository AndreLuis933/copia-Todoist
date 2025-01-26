from datetime import datetime, timedelta

def is_today_or_tomorrow(time_str):
    # Obter o horário atual
    now = datetime.now()
    
    # Converter a string de tempo para um objeto datetime
    given_time = datetime.strptime(time_str, "%I:%M %p")
    
    # Combinar a data de hoje com o horário fornecido
    today_time = now.replace(hour=given_time.hour, minute=given_time.minute, second=0, microsecond=0)
    
    # Se o horário já passou hoje, será amanhã
    if now > today_time:
        return "Amanhã"
    else:
        return "Hoje"

# Exemplo de uso
time_str = "07:00 PM"
result = is_today_or_tomorrow(time_str)
print(f"O horário {time_str} será {result}.")