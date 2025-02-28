from flet import *
from ..animations.slidbar.fechar_slidbar import AnimateSlidbar
from ..animations.high_light import high_light
from app.database.operations import listar_projetc


class Slidbar(Container):
    def __init__(self, controler):
        super().__init__()
        self.controler = controler
        self.func = AnimateSlidbar(self)
        self.width = 220
        self.bgcolor = "#222222"
        self.animate = animation.Animation(500, "decelerate")
        self.alignment = alignment.top_left
        self.padding = 10
        self.content = self.build()
        self.add_project()
        self.func.open_close_slidbar()

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
                Container(
                    Image(
                        src=r"icons\screen.png", width=25, height=25, color=Colors.WHITE
                    ),
                    on_click=self.func.open_close_slidbar,
                ),
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
        color_icon=Colors.WHITE,
        color_text=Colors.WHITE,
        func=None,
    ):
        if not func:
            func = lambda e: self.page.go("/s")
        return Container(
            width=self.width - 20,
            height=35,
            border_radius=10,
            on_hover=lambda e: high_light(e, 'trasparent', "white10"),
            on_click=func,
            padding=0,
            content=Row(
                [
                    Container(
                        Image(
                            src=icon_name,
                            width=height,
                            height=height,
                            color=color_icon,
                            opacity=opacity,
                        ),
                        padding=padding.only(left=padding_left),
                    ),
                    Text(
                        value=text,
                        color=color_text,
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
                ],
            ),
        )

    def Categorias(self, text, add=False):
        return Container(
            Row(
                [
                    Text(
                        text,
                        size=14,
                        weight="w500",
                        color=Colors.WHITE70,
                    ),
                    Container(expand=True),
                    Container(
                        Icon(Icons.ADD, size=20, color=Colors.WHITE70),
                        on_click=lambda e: self.controler.segunda_camada.show_add_projeto(),
                        visible=add,
                    ),
                    Container(
                        Image(
                            src=r"icons\down_arrow.png",
                            width=18,
                            height=18,
                            color=Colors.WHITE70,
                        ),
                        on_click=lambda _: self.func.close_projects(text),
                    ),
                ],
            ),
            alignment=alignment.center,
            height=35,
            width=self.width - 20,
            on_click=lambda e: None,
            on_hover=lambda e: high_light(e, 'trasparent', "white10"),
            padding=padding.symmetric(horizontal=10),
        )

    def add_project(self):
        favoritos = self.content.controls[1].controls[7].content
        projetes = self.content.controls[1].controls[10].content
        projetes.controls.clear()
        favoritos.controls.clear()
        for tarefa_id in listar_projetc():
            id, name, color, space_work, favorite, visualize = tarefa_id
            if favorite:
                favoritos.controls.append(
                    self.ContainedIcon(r"icons\hastag.png", name, 1, 15, 20, color)
                )
            else:
                projetes.controls.append(
                    self.ContainedIcon(r"icons\hastag.png", name, 1, 15, 20, color)
                )

        if not favoritos.controls:
            self.content.controls[1].controls[5].visible = False
            self.content.controls[1].controls[6].visible = False
        else:
            self.content.controls[1].controls[5].visible = True
            self.content.controls[1].controls[6].visible = True

    def build(self):
        return Column(
            [
                Column(
                    [
                        self.UserData("perfil.jpg", "Andre"),
                        Divider(height=5, color="transparent"),
                        self.ContainedIcon(
                            r"icons\add.png",
                            "Adicionar tarefa",
                            1,
                            25,
                            8,
                            Colors.RED,
                            Colors.RED,
                            self.controler.hover_control.card_save,
                        ),
                    ],
                    spacing=0,
                ),
                Column(
                    [
                        self.ContainedIcon(r"icons\search.png", "Buscar"),
                        self.ContainedIcon(r"icons\inbox.png", "Entrada"),
                        self.ContainedIcon(r"icons\calendar.png", "Hoje"),
                        self.ContainedIcon(r"icons\calculator.png", "Em breve"),
                        self.ContainedIcon(r"icons\menu.png", "Filtros e Etiquetas"),
                        Divider(height=10, color="transparent"),
                        self.Categorias("Favoritos", False),
                        Container(Column(spacing=0)),
                        Divider(height=10, color="transparent"),
                        self.Categorias("Meus projetos", True),
                        Container(Column(spacing=0)),
                        Container(expand=True),
                    ],
                    spacing=0,
                    horizontal_alignment="center",
                    scroll=ScrollMode.ALWAYS,
                    expand=True,
                ),
                self.ContainedIcon(r"icons\chart.png", "Navegar pelos modelos"),
            ]
        )
