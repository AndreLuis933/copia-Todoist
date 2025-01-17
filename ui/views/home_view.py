from flet import *
from ui.components.slidbar import Slidbar
from ui.components.card_adicionar_tarefa import Card_adicionar_tarefa
from ui.components.calendario import Calendario
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.button_adicionar_tarefa import Button_adicionar_tarefa
from ui.components.utils.hover_adicionar_tarefa import HoverAdicionarTarefa
from ui.components.segunda_camada.prioridade import Card_prioridade
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.mostrar_tarefas import TodoApp
from ui.components.segunda_camada.lembretes import Lembretes


class HomeView:
    def __init__(self, page: Page):
        self.page = page
        self.content = None

    def encontrar(self, e):
        print(self.page.views)
        pass

    def update_layout(self, e=None):
        if self.content:
            self.content.width = self.page.window.width
            self.content.height = self.page.window.height
            self.page.update()

    def build(self):

        calendario = Calendario()
        lembretes = Lembretes()
        prioridade = Card_prioridade()
        tarefa = Tarefa_vencimento(calendario)
        hover_control = HoverAdicionarTarefa()
        button = Button_adicionar_tarefa(hover_control)
        card_container = Card_adicionar_tarefa(
            hover_control, tarefa, prioridade, lembretes
        )
        calendario.load_more_months(3)

        self.content = Stack(
            [  # 1 camada
                GestureDetector(
                    on_tap=tarefa.hide_card,
                    content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
                ),
                Row(
                    expand=True,
                    alignment=alignment.top_left,
                    controls=[
                        Slidbar(),
                        Column(
                            controls=[
                                Text("Entrada", size=20, weight="bold"),
                                Divider(height=2, opacity=0),
                                button,
                                card_container,
                                Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
                                TodoApp(),
                            ],
                            expand=True,
                        ),
                    ],
                ),
                # 2 camada
                Container(
                    content=Stack(
                        [
                            prioridade,
                            tarefa,
                            lembretes,
                        ]
                    ),
                    expand=True,
                    visible=True,
                ),
                # 3 camada
                lembretes.dropdown,
            ],
            width=self.page.window.width,
            height=self.page.window.height,
        )

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
