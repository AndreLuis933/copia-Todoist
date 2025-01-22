from flet import *


def downdown_custon(lista, icon=None, height=None):
    return Dropdown(
        icon=icon,
        value=lista[0],
        content_padding=padding.symmetric(horizontal=10, vertical=2),
        text_size=15,
        text_style=TextStyle(color=Colors.WHITE, font_family='Poppins', weight='w500'),
        alignment=alignment.center,
        #border=border.all(0, '#3d3d3d'),
        item_height=48,
        height=height,
        max_menu_height=500,
        options=[dropdown.Option(texto) for texto in lista],
    )
