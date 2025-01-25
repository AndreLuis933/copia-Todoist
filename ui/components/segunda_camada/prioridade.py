from flet import *
from ..animations.prioridade.high_light import high_light


class Card_prioridade(Container):
    def __init__(self, controler):
        super().__init__()
        self.visible = False
        self.controler = controler
        self.selected_priority = None
        self.width = 150
        self.left = 350
        self.top = 170
        self.bgcolor = "#1E1E1E"
        self.border = border.all(0.5, Colors.OUTLINE)
        self.border_radius = border_radius.all(10)
        self.content = self.build()

    def select_priority(self, e, priority):
        self.controler.save.prioridade = int(priority.split()[1])
        self.visible = False
        print(f"Prioridade selecionada: {priority}")
        self.update()

    def cards_prioridade(self, icon, cor, texto):
        return Container(
            content=Row(
                controls=[
                    Icon(icon, color=cor, size=22),
                    Text(texto, size=14),
                ],
            ),
            padding=padding.symmetric(vertical=4, horizontal=8),
            height=40,
            on_click=lambda e: self.select_priority(e, texto),
            bgcolor="#272727",
            on_hover=high_light,
        )

    def build(self):
        return Column(
            controls=[
                self.cards_prioridade(Icons.FLAG, Colors.RED, "Prioridade 1"),
                self.cards_prioridade(Icons.FLAG, Colors.ORANGE, "Prioridade 2"),
                self.cards_prioridade(Icons.FLAG, Colors.BLUE, "Prioridade 3"),
                self.cards_prioridade(Icons.FLAG, Colors.GREY, "Prioridade 4"),
            ],
            spacing=0,
        )
