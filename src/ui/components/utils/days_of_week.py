from .indentificar_datas import DIAS_SEMANA_COMPLETOS
from .locale_config import temp_locale
from datetime import datetime, timedelta
from flet import Colors


def dia_da_semana_e_cor(data):
    atual = datetime.now()

    def formatad_data(data):
        mon = data.strftime("%b").capitalize()
        with temp_locale("en_US.UTF-8"):
            formatted_date = mon + data.strftime(" %d %I:%M %p")
            formatted_date = formatted_date.replace(" 12:00 AM", "")

            return formatted_date

    def dias_da_semana():
        dias_semana = ["Hoje", "Amanhã"]

        for i in range(2, 8):
            dia = atual + timedelta(days=i)
            indice_dia = dia.weekday()
            dias_semana.append(DIAS_SEMANA_COMPLETOS[indice_dia])

        return dias_semana

    color = Colors.ON_SURFACE_VARIANT

    formatted_date = formatad_data(data)
    diferenca = (data.date() - atual.date()).days
    
    if 0 <= diferenca < 7:
        dia = dias_da_semana()[diferenca]
        formatted_date = dia
        if diferenca == 0:
            color = "#25b84c"
        elif diferenca == 1:
            color = "#ff9a14"
        else:
            color = "#a970ff"

    elif diferenca < 0:
        color = '#ec6553'

    return formatad_data(data), formatted_date, color
