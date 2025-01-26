from datetime import datetime
import locale

# Criar o objeto datetime
dt = datetime(2025, 1, 26, 19, 45, 0)

# Converter para o formato desejado
formatted_date = dt.strftime('%b %d %I:%M %p')
print(locale.getlocale())
print(formatted_date)