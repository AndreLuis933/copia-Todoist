from datetime import datetime, timedelta
from .locale_config import temp_locale

def horarios_15_minutos():
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
