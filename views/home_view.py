from flet import *
from components.slidbar import Slidbar
from animations.animation import create_animate_slidbar


class HomeView:
    def __init__(self, page: Page):
        self.page = page

    def encontrar(self, e):
        print(self.page.views)
        pass

    def build(self):
        slidbar_container = Container(
            width=200,
            height=580,
            bgcolor="black",
            border_radius=10,
            animate=animation.Animation(500, "decelerate"),
            alignment=alignment.center,
            padding=10,
            content=Slidbar(create_animate_slidbar(self.page), self.page),
        )
        main_layout = Row(
            controls=[
                slidbar_container,
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
