import time
from flet import *


def create_animate_slidbar(page):
    state = None

    class SlidbarState:
        def __init__(self):
            self.slidbar = page.controls[0].controls[0]
            self.icons_texto = self.slidbar.content.controls[0].content
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






import time
from flet import *


def create_animate_slidbar(page):
    def animate_slidbar(e):
        slidbar = page.controls[0].controls[0]
        titulo_texto = slidbar.content.controls[0].content.controls[0].content.controls[1].controls
        icons_texto = slidbar.content.controls[0].content.controls[3:]
        
        if slidbar.width != 62:
            for item in titulo_texto:
                item.opacity = 0
                item.update()

            for items in icons_texto:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()

            time.sleep(0.2)
            slidbar.width = 62
            slidbar.update()
        else:
            time.sleep(0.2)
            slidbar.width = 200
            slidbar.update()

            for item in titulo_texto:
                item.opacity = 1
                item.update()

            for items in icons_texto:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()

    return animate_slidbar








import time
from flet import *

def create_animate_slidbar(page):
    def animate_slidbar(e):
        if page.controls[0].controls[0].width != 62:
            close_slidbar(page)
        else:
            open_slidbar(page)

    return animate_slidbar

def close_slidbar(page):
    slidbar = page.controls[0].controls[0]
    for item in slidbar.content.controls[0].content.controls[0].content.controls[1].controls[:]:
        item.opacity = 0
        item.update()

    for items in slidbar.content.controls[0].content.controls[3:]:
        if isinstance(items, Container):
            items.content.controls[1].opacity = 0
            items.content.update()

    time.sleep(0.2)
    slidbar.width = 62
    slidbar.update()

def open_slidbar(page):
    slidbar = page.controls[0].controls[0]
    time.sleep(0.2)
    slidbar.width = 200
    slidbar.update()

    for item in slidbar.content.controls[0].content.controls[0].content.controls[1].controls[:]:
        item.opacity = 1
        item.update()

    for items in slidbar.content.controls[0].content.controls[3:]:
        if isinstance(items, Container):
            items.content.controls[1].opacity = 1
            items.content.update()