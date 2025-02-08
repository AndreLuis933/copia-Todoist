from flet import *
from ui.components.primeira_camada.slidbar import Slidbar
from ui.components.primeira_camada.card_adicionar_tarefa import Card_adicionar_tarefa
from ui.components.primeira_camada.button_adicionar_tarefa import (
    Button_adicionar_tarefa,
)
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
        self.segunda_camada = ControlerSegundaCamada(self)
        self.hover_control = HoverAdicionarTarefa(self.segunda_camada)
        self.button = Button_adicionar_tarefa(self.hover_control)
        self.card_container = Card_adicionar_tarefa(
            self, self.segunda_camada, self.hover_control
        )
        self.lista_tarefas = TodoApp(self)
        self.slidbar = Slidbar(self)
        self.controls = self.build()

    def adicionar_prefixo(self, prefixo):
        row = self.card_container.content.controls[0].content.controls[0].controls[0]
        row.controls.append(self.card_container.prefixos(prefixo))
        self.update()

    def build(self):
        return [
            self.slidbar,
            Column(
                controls=[
                    Container(
                        Row(
                            [
                                Icon(Icons.TUNE, color=Colors.WHITE60),
                                Icon(Icons.CHAT_BUBBLE_OUTLINE, color=Colors.WHITE60),
                                Icon(Icons.MORE_HORIZ, color=Colors.WHITE60),
                            ],
                            alignment=MainAxisAlignment.END,
                        ),
                        padding=padding.only(top=10, right=10, bottom=25),
                    ),
                    Text("Entrada", size=25, weight="bold", max_lines=1,color=Colors.WHITE),
                    Divider(height=2, opacity=0),
                    self.button,
                    self.card_container,
                    Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
                    self.lista_tarefas,
                ],
                expand=True,
            ),
        ]
