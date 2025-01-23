from zoneinfo import ZoneInfo
from datetime import datetime

def obter_fuso_horario_atual():
    fuso_local = datetime.now(ZoneInfo("localtime")).tzinfo
    return str(fuso_local)

# Uso
print(f"Seu fuso horário atual é: {obter_fuso_horario_atual()}")