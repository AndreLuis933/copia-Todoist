from tzlocal import get_localzone

def obter_fuso_horario_atual():
    # Obtém o fuso horário local
    fuso_local = get_localzone()
    return f"{fuso_local}\nSeu fuso horário atual"

# Uso
print(obter_fuso_horario_atual())