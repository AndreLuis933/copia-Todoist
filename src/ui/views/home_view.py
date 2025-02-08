from flet import *
from ui.controller.camadas.primeira import ControlerPrimeiraCamada


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
        
        primeira_camada = ControlerPrimeiraCamada()
        segunda_camada = primeira_camada.segunda_camada
        terceira_camada = segunda_camada.terceira_camada

        self.content = Stack(
            [  # 1 camada
                GestureDetector(
                    on_tap=segunda_camada.default,
                    content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
                ),
                primeira_camada,
                # 2 camada
                *segunda_camada.controls,
                # 3 camada
                *terceira_camada.controls,
            ],
            expand=True,
            # width=self.page.window.width,
            # height=self.page.window.height,
        )

        # self.page.on_resized = self.update_layout

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
