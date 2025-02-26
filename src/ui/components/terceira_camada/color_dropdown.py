from flet import *
from ..animations.high_light import high_light, default_high_light


class ColorDropdown(Container):
    def __init__(self, segunda_camada, terceira_camada):
        super().__init__()
        self.segunda_camada = segunda_camada
        self.terceira_camada = terceira_camada
        self.visible = False
        self.add_projeto = self.segunda_camada.add_projeto
        self.bgcolor = "#262626"
        self.border_radius = 10
        self.border = border.all(0.5, Colors.OUTLINE)
        self.padding = padding.only(bottom=5)
        self.width = self.add_projeto.width - 30
        self.height = 300
        self.top = self.add_projeto.top + 230
        self.left = self.add_projeto.left + 15
        self.content = self.build()

    def color_options(self, cor, nome, border=None):
        return Container(
            Row(
                [
                    Container(
                        bgcolor=cor,
                        width=12,
                        height=12,
                        border_radius=20,
                    ),
                    Text(nome),
                    Container(expand=True),
                    Icon(
                        Icons.CHECK,
                        size=12,
                        color=Colors.WHITE,
                        visible=False,
                    ),
                ]
            ),
            padding=padding.only(top=5, bottom=5, left=10, right=10),
            on_hover=lambda e: high_light(e, "trasparent", "#383838"),
            on_click=lambda e: self.change_color(e),
            border=border,
        )

    def change_color(self, e):
        self.add_projeto.chose_color = e.control.content.controls[0].bgcolor
        for control in self.content.controls:
            control.content.controls[3].visible = False
        e.control.content.controls[3].visible = True
        default_high_light(e, "trasparent")
        self.terceira_camada.hide_all()
        self.add_projeto.update_color()

    def build(self):
        return Column(
            [
                self.color_options(cor, nome)
                for cor, nome in self.add_projeto.colors_dict.items()
            ],
            scroll=ScrollMode.ALWAYS,
            spacing=0,
        )
