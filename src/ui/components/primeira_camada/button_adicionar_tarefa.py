from flet import *


class Button_adicionar_tarefa(Container):
    def __init__(self, hover_control):
        super().__init__()
        self.hover_control = hover_control
        self.hover_control.button = self
        self.visible = True
        self.button_height = 24
        self.on_click = self.hover_control.card_add
        self.on_hover = self.hover_control.mudar_cor
        self.content = self.build()

    def build(self):
        return Row(
            tight=True,
            controls=[
                Stack(
                    [
                        Container(
                            visible=False,
                            bgcolor=Colors.WHITE,
                            height=self.button_height / 2,
                            width=self.button_height / 2,
                            alignment=alignment.center,
                        ),
                        Icon(
                            name=Icons.ADD,
                            color=Colors.RED,
                            opacity=0.9,
                            size=self.button_height,
                        ),
                    ],
                    alignment=alignment.center,
                ),
                Text(
                    "Adicionar tarefa",
                    color=Colors.WHITE54,
                    size=14,
                ),
            ],
            spacing=8,
            alignment=MainAxisAlignment.START,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
