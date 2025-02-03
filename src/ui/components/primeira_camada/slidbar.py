from flet import *
from functools import partial
from ..animations.slidbar.fechar_slidbar import create_animate_slidbar
from ..animations.slidbar.high_light_slidbar import HighLight


class Slidbar(Container):
    def __init__(self):
        super().__init__()
        self.func = create_animate_slidbar(self)
        self.HighLight = HighLight
        self.width = 220
        self.bgcolor = "#222222"
        # self.border_radius = 10
        self.animate = animation.Animation(500, "decelerate")
        self.alignment = alignment.top_left
        self.padding = 10
        self.content = self.build()

    def show_slidbar(self):
        return Container(
                Image(src=r"icons\screen.png", width=25, height=25, color=Colors.WHITE),
                on_click=partial(self.func),
            )
        

    def UserData(self, photo: str, name: str):
        return Row(
            controls=[
                Container(
                    Row(
                        [
                            Container(
                                width=42,
                                height=42,
                                alignment=alignment.center,
                                content=Image(src=photo, border_radius=20),
                            ),
                            Text(
                                value=name,
                                size=14,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,
                            ),
                            Container(
                                Image(
                                    src=r"icons\down-arrow.png",
                                    width=13,
                                    height=13,
                                    color=Colors.WHITE,
                                ),
                                margin=margin.only(right=8),
                            ),
                        ],
                        spacing=5,
                    ),
                    ink=True,
                    on_click=lambda e: print("home"),
                ),
                Container(
                    Image(
                        src=r"icons\bell.png", width=20, height=20, color=Colors.WHITE
                    ),
                    on_click=lambda e: print("home"),
                ),
                self.show_slidbar(),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )

    def ContainedIcon(
        self,
        icon_name: str,
        text: str,
        opacity=1,
        height=18,
        padding_left=10,
        color=Colors.WHITE,
    ):
        return Container(
            width=self.width - 20,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.page.go("/s"),
            content=Row(
                controls=[
                    Container(
                        Image(
                            src=icon_name,
                            width=height,
                            height=height,
                            color=color,
                            opacity=opacity,
                        ),
                        padding=padding.only(left=padding_left),
                    ),
                    Text(
                        value=text,
                        color=color,
                        size=14,
                        opacity=1,
                        animate_opacity=200,
                    ),
                    Container(expand=True),
                    Container(
                        Text(
                            value="",
                            color=Colors.WHITE54,
                            opacity=0.6,
                        ),
                        padding=padding.only(right=10),
                    ),
                ]
            ),
        )

    def build(self):
        return Column(
            horizontal_alignment="center",
            controls=[
                self.UserData("perfil.jpg", "Andre"),
                Divider(height=5, color="transparent"),
                self.ContainedIcon(
                    r"icons\add.png", "Adicionar tarefa", 1, 25, 8, Colors.RED
                ),
                self.ContainedIcon(r"icons\search.png", "Buscar"),
                self.ContainedIcon(r"icons\inbox.png", "Entrada"),
                self.ContainedIcon(r"icons\calendar.png", "Hoje"),
                self.ContainedIcon(r"icons\calculator.png", "Em breve"),
                self.ContainedIcon(r"icons\menu.png", "Filtros e Etiquetas"),
                Divider(height=10, color="transparent"),
                Container(
                    Row(
                        [
                            Text(
                                "My Projects",
                                size=14,
                                weight="w500",
                                color=Colors.WHITE70,
                            ),
                            Container(expand=True),
                            Container(
                                Icon(Icons.ADD, size=20, color=Colors.WHITE70),
                                on_click=lambda e: print("Adicionar"),
                            ),
                            Container(
                                Image(
                                    src=r"icons\down-arrow.png",
                                    width=18,
                                    height=18,
                                    color=Colors.WHITE70,
                                ),
                                on_click=lambda e: print("esconder"),
                            ),
                        ],
                    ),
                    alignment=alignment.center,
                    height=45,
                    width=self.width - 20,
                    on_click=lambda e: print("My Projects"),
                    on_hover=lambda e: self.HighLight(e),
                    padding=padding.symmetric(horizontal=10),
                ),
                self.ContainedIcon(r"icons\hastag.png", "Casa", 0.5, 15, 20),
                self.ContainedIcon(r"icons\hastag.png", "Estudos", 0.5, 15, 20),
                self.ContainedIcon(r"icons\hastag.png", "Investimentos", 0.5, 15, 20),
                Container(expand=True),
                self.ContainedIcon(r"icons\chart.png", "Browse templates"),
            ],
            spacing=0,
        )
