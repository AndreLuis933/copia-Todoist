from flet import *
from components.slidbar import Slidbar
from components.adicionar_tarefa import (
    Calendario,
    Compartilhado,
    Tarefa_vencimento,
    Button_adicionar_tarefa,
    Card_adicionar_tarefa,
)


class HomeView:
    def __init__(self, page: Page):
        self.page = page

    def encontrar(self, e):
        print(self.page.views)
        pass

    def build(self):

        calendario = Calendario()
        compartilhado = Compartilhado()
        tarefa = Tarefa_vencimento(calendario)
        button = Button_adicionar_tarefa(compartilhado)
        card_container = Card_adicionar_tarefa(compartilhado, tarefa)
        calendario.load_more_months(3)

        content = Stack(
            [
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
                                button,
                                card_container,
                                tarefa,
                            ],
                            spacing=20,
                            expand=True,
                        ),
                    ],
                ),
            ],
            expand=True,
        )

        return content


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
