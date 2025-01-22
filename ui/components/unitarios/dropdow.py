from flet import *


def downdown_custon(lista, icon=None, height=None):
    return Dropdown(
        icon=icon,
        value=lista[0],
        content_padding=padding.symmetric(horizontal=10, vertical=2),
        text_size=15,
        text_style=TextStyle(color=Colors.WHITE, font_family='Arial', weight='w450'),
        alignment=alignment.center,
        item_height=48,
        height=height if height else 50,
        max_menu_height=500,
        options=[dropdown.Option(texto) for texto in lista],
    )
