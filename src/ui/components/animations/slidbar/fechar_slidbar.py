import time
from flet import *


def create_animate_slidbar(page):
    state = None

    class SlidbarState:
        def __init__(self):
            self.slidbar = page
            self.icons_texto = self.slidbar.content
            self.titulo_texto = self.icons_texto.controls[0]
            self.is_open = True
            

    def toggle_opacity(controls, show):
        opacity = 1 if show else 0
                    
        for item in controls:
            if isinstance(item, Container) and not item.content is None:
                if isinstance(item.content, Image):
                    if 'screen' not in item.content.src:
                        item.opacity = opacity
                else:
                    item.opacity = opacity
                    
            item.update()

        time.sleep(0.2)
        for item in controls:
            if isinstance(item, Container) and not item.content is None:
                if isinstance(item.content, Image):
                    if 'screen' not in item.content.src:
                        item.visible = show
                else:
                    item.visible = show

            item.update()

    def animate_slidbar(e):
        nonlocal state
        if state is None:
            state = SlidbarState()
        slidbar = state.slidbar
        total = state.titulo_texto.controls
        total.extend(state.icons_texto.controls[2:])

        if state.is_open:
            # Fechar a barra lateral

            toggle_opacity(total, False)
            #toggle_opacity(state.icons_texto.controls[2:], False)
            slidbar.bgcolor = Colors.TRANSPARENT
            time.sleep(0.2)
            slidbar.width = 50
            #slidbar.height = 50
        else:
            # Abrir a barra lateral
            slidbar.width = 220
            slidbar.height = None
            slidbar.bgcolor = "#222222"
            time.sleep(0.2)
            toggle_opacity(total, True)
            #toggle_opacity(state.icons_texto.controls[2:], True)

        state.slidbar.update()
        state.is_open = not state.is_open
        page.update()

    return animate_slidbar
