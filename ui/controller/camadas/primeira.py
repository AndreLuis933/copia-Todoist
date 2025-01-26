from flet import *
from ui.components.primeira_camada.slidbar import Slidbar
from ui.components.primeira_camada.card_adicionar_tarefa import Card_adicionar_tarefa
from ui.components.primeira_camada.button_adicionar_tarefa import Button_adicionar_tarefa
from ui.components.primeira_camada.mostrar_tarefas import TodoApp
from ui.components.animations.card_adicionar_tarefa.hover_adicionar_tarefa import (
    HoverAdicionarTarefa,
)
from .segunda import ControlerSegundaCamada
from ...components.utils.save_in_db import SaveInDB

class ControlerPrimeiraCamada(Row):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.alignment = alignment.top_left
        self.save = SaveInDB(self)
        self.lista_tarefas = TodoApp()
        self.segunda_camada = ControlerSegundaCamada(self.save)
        self.hover_control = HoverAdicionarTarefa(self.segunda_camada)
        self.button = Button_adicionar_tarefa(self.hover_control)
        self.card_container = Card_adicionar_tarefa(
            self, self.segunda_camada, self.hover_control
        )
        self.controls = self.build()

    def build(self):
        return [
            Slidbar(),
            Column(
                controls=[
                    Text("Entrada", size=20, weight="bold", max_lines=1),
                    Divider(height=2, opacity=0),
                    self.button,
                    self.card_container,
                    Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
                    self.lista_tarefas,
                ],
                expand=True,
            ),
        ]
