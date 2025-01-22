from flet import *


def downdown_custon(lista, icon=None, height=None):
    return Dropdown(
        icon=icon,
        value=lista[0],
        padding=0,
        text_size=10,
        bgcolor=Colors.GREY_900,
        alignment=alignment.center,
        height=height,
        max_menu_height=500,
        options=[dropdown.Option(texto) for texto in lista],
    )
