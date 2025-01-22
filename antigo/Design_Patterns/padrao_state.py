import flet as ft
from flet import *

class State:
    componentes = {}
    def __init__(self, apelido= None, componente = None, visible=True):
        if componente:
            self.componentes[apelido] = componente
        self.visible = visible
        
    def get_state(self):
        return self.visible
    
    def set_state(self, visible):
        self.visible = visible



class Teste(Container):
    def __init__(self):
        super().__init__()
        self.state = State('teste',self)
        self.visible = self.state.get_state()
        self.width = 300
        self.height = 300
        self.bgcolor = Colors.GREY
        self.content = self.build()
        
    def build(self):
        return ft.Text("Teste")


def main(page: ft.Page):
    page.window.always_on_top = True
    state = State()
    def toggle(e):

        print(state.componentes['teste'].visible)
        state.set_state()
        #state.componentes['teste'].visible = not state.componentes['teste'].visible
        page.update()
        
    componente = Teste()
    button = ft.ElevatedButton(text="Toggle", on_click=lambda e: toggle(e))

    page.add(componente,button)

ft.app(target=main)