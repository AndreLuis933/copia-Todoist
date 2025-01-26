from datetime import datetime, timedelta


def is_today_or_tomorrow(time_str):
    now = datetime.now()

    given_time = datetime.strptime(time_str, "%I:%M %p")

    today_time = now.replace(
        hour=given_time.hour, minute=given_time.minute, second=0, microsecond=0
    )

    if now > today_time:

        result_time = today_time + timedelta(days=1)
        return [result_time, f"Amanhã {time_str}"]
    else:

        return [today_time, f"Hoje {time_str}"]
