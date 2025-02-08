import locale
from contextlib import contextmanager

# Definir a localização padrão para pt_BR.UTF-8
DEFAULT_LOCALE = "pt_BR.UTF-8"

# Configurar a localização padrão

def set_default_locale():
    locale.setlocale(locale.LC_TIME, DEFAULT_LOCALE)

@contextmanager
def temp_locale(temp_locale):    
    try:
        locale.setlocale(locale.LC_TIME, temp_locale)
        yield
    finally:
        set_default_locale()