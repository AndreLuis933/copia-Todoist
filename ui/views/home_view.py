from flet import *
from ui.components.slidbar import Slidbar
from ui.components.card_adicionar_tarefa import Card_adicionar_tarefa
from ui.components.calendario import Calendario
<<<<<<< HEAD
from ui.components.tarefa_vencimento import Tarefa_vencimento
from ui.components.button_adicionar_tarefa import Button_adicionar_tarefa
from ui.components.utils.hover_adicionar_tarefa import HoverAdicionarTarefa
from ui.components.prioridade import Card_prioridade
from ui.components.tarefa_vencimento import Tarefa_vencimento
from ui.components.mostrar_tarefas import TodoApp
=======
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.button_adicionar_tarefa import Button_adicionar_tarefa
from ui.components.utils.hover_adicionar_tarefa import HoverAdicionarTarefa
from ui.components.segunda_camada.prioridade import Card_prioridade
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.mostrar_tarefas import TodoApp
from ui.components.segunda_camada.lembretes import Lembretes
from ui.components.segunda_camada.controler import ControlerSegundaCamada

>>>>>>> trabalho-temporario

class HomeView:
    def __init__(self, page: Page):
        self.page = page
        self.content = None

    def encontrar(self, e):
        print(self.page.views)
        pass
<<<<<<< HEAD
    
=======

>>>>>>> trabalho-temporario
    def update_layout(self, e=None):
        if self.content:
            self.content.width = self.page.window.width
            self.content.height = self.page.window.height
            self.page.update()

    def build(self):

<<<<<<< HEAD
        prioridade = Card_prioridade()
        calendario = Calendario()
        hover_control = HoverAdicionarTarefa()
        tarefa = Tarefa_vencimento(calendario)
        button = Button_adicionar_tarefa(hover_control)
        card_container = Card_adicionar_tarefa(hover_control, tarefa, prioridade)
        calendario.load_more_months(3)

        self.content = Stack(
            [
                GestureDetector(
                    on_tap=tarefa.hide_card,
=======
        segunda_camada = ControlerSegundaCamada()
        hover_control = HoverAdicionarTarefa(segunda_camada)
        button = Button_adicionar_tarefa(hover_control)
        card_container = Card_adicionar_tarefa(
            segunda_camada, hover_control
        )


        self.content = Stack(
            [  # 1 camada
                GestureDetector(
                    on_tap=segunda_camada.default,
>>>>>>> trabalho-temporario
                    content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
                ),
                Row(
                    expand=True,
                    alignment=alignment.top_left,
                    controls=[
                        Slidbar(),
                        Column(
                            controls=[
<<<<<<< HEAD
                                button,
                                card_container,
=======
                                Text("Entrada", size=20, weight="bold"),
                                Divider(height=2, opacity=0),
                                button,
                                card_container,
                                Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
>>>>>>> trabalho-temporario
                                TodoApp(),
                            ],
                            expand=True,
                        ),
                    ],
                ),
<<<<<<< HEAD
                prioridade,
                tarefa,
=======
                # 2 camada
                *segunda_camada.get_controls(),
                    
                # 3 camada
                segunda_camada.lembretes.dropdown,
                segunda_camada.tarefa.hora,
>>>>>>> trabalho-temporario
            ],
            width=self.page.window.width,
            height=self.page.window.height,
        )
<<<<<<< HEAD
        
=======

>>>>>>> trabalho-temporario
        self.page.on_resized = self.update_layout

        return self.content


class Teste:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        botao = ElevatedButton(
            "mudar",
            bgcolor="white",
            on_click=lambda _: botao.page.go("/"),
        )

        return botao
