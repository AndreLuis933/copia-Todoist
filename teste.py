from datetime import datetime
from dateutil.relativedelta import relativedelta

# Supondo que mes_desejado seja o número de meses que você quer avançar
mes_desejado = 0  # Exemplo: avançar 1 mês

# Calculando a nova data
date = datetime.now() + relativedelta(months=mes_desejado)
year, month = date.year, date.month

print(date)