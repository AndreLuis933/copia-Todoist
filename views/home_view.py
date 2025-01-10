from flet import *
from components.slidbar import Slidbar
from animations.animation import create_animate_slidbar


class HomeView:
    def __init__(self, page: Page):
        self.page = page

    def encontrar(self, e):
        print(e.page.views)
        pass

    def build(self):
        main_layout = Row(
            controls=[
                Slidbar(self.page),
                ElevatedButton(
                    "Slidbar",
                    bgcolor="white",
                    on_click=self.encontrar,
                ),
            ],
        )

        return main_layout


class Teste:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        return ElevatedButton(
            "mudar",
            bgcolor="white",
            on_click=lambda _: self.page.go("/"),
        )
