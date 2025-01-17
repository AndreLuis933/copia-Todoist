from flet import *

class Lembretes(Container):
    def __init__(self):
        super().__init__()
        self.visible = True
        self.selected_priority = None
        self.content = self.build()
        self.width = 150
        self.height = 170
        self.left = 475  # Posição fixa à esquerda
        self.top = 200  # Posição fixa no topo

    def show_card(self, e):
        self.visible = not self.visible
        self.update()

    def build(self):
        return Container(
            content=Column(
                controls=[
                ],
                spacing=8,
            ),
            bgcolor=Colors.SURFACE,
            border=border.all(0.5, Colors.OUTLINE),
            border_radius=border_radius.all(10),
            padding=padding.all(8),
        )
