from flet import *



def downdown_custon(lista, icon=None):
    return Dropdown(
        icon=icon,
        value=lista[0],
        bgcolor=Colors.GREY_900,
        alignment=alignment.center,
        max_menu_height=500,
        options=[dropdown.Option(texto) for texto in lista],
    )
