from datetime import datetime, timedelta

def is_today_or_tomorrow(time_str):
    now = datetime.now()

    given_time = datetime.strptime(time_str, "%I:%M %p")

    today_time = now.replace(
        hour=given_time.hour, minute=given_time.minute, second=0, microsecond=0
    )

    if now > today_time:
        # Se o horário já passou, será amanhã
        result_time = today_time + timedelta(days=1)
        return [result_time, f"Amanhã {time_str}"]
    else:
        # Se o horário ainda não passou, será hoje
        return [today_time, f"Hoje {time_str}"]

# Exemplo de uso
time_str = "08:00 PM"
result_datetime, result_string = is_today_or_tomorrow(time_str)
print(f"Datetime: {result_datetime}")
print(f"String: {result_string}")