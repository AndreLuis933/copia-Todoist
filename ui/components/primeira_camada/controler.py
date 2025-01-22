from flet import *
from .slidbar import Slidbar
from .card_adicionar_tarefa import Card_adicionar_tarefa
from .button_adicionar_tarefa import Button_adicionar_tarefa
from .mostrar_tarefas import TodoApp
from ..animations.card_adicionar_tarefa.hover_adicionar_tarefa import HoverAdicionarTarefa
from ..segunda_camada.controler import ControlerSegundaCamada

class ControlerPrimeiraCamada(Row):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.alignment = alignment.top_left
        self.segunda_camada = ControlerSegundaCamada()
        self.hover_control = HoverAdicionarTarefa(self.segunda_camada)
        self.button = Button_adicionar_tarefa(self.hover_control)
        self.card_container = Card_adicionar_tarefa(
            self.segunda_camada, self.hover_control
        )
        self.controls = self.build()
        
    
    def build(self):
        return [
                        Slidbar(),
                        Column(
                            controls=[
                                Text("Entrada", size=20, weight="bold"),
                                Divider(height=2, opacity=0),
                                self.button,
                                self.card_container,
                                Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
                                TodoApp(),
                            ],
                            expand=True,
                        ),
                    ]
                