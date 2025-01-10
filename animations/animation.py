import time
from flet import *


def create_animate_slidbar(page):
    state = None

    class SlidbarState:
        def __init__(self):
            self.slidbar = page
            self.icons_texto = self.slidbar.content.content
            self.titulo_texto = self.icons_texto.controls[0].content.controls[1]
            self.is_open = True

    def toggle_opacity(controls, show):
        opacity = 1 if show else 0
        for item in controls:
            if isinstance(item, Container):
                item.content.controls[1].opacity = opacity
            else:
                item.opacity = opacity
            item.update()

    def animate_slidbar(e):
        nonlocal state
        if state is None:
            state = SlidbarState()

        if state.is_open:
            # Fechar a barra lateral
            toggle_opacity(state.titulo_texto.controls, False)
            toggle_opacity(state.icons_texto.controls[3:], False)
            time.sleep(0.2)
            state.slidbar.width = 62
        else:
            # Abrir a barra lateral
            state.slidbar.width = 200
            time.sleep(0.2)
            toggle_opacity(state.titulo_texto.controls, True)
            toggle_opacity(state.icons_texto.controls[3:], True)

        state.slidbar.update()
        state.is_open = not state.is_open

    return animate_slidbar
