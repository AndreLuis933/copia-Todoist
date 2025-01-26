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
        priority = int(priority.split()[1])
        for i in range(4):
            self.content.controls[i].content.controls[2].visible = False

        self.content.controls[priority - 1].content.controls[2].visible = True
        self.controler.save.prioridade = priority
        self.controler.hide_all()
        high_light(e)
        self.page.update()

    def cards_prioridade(self, icon, cor, texto, visible=False):
        return Container(
            content=Row(
                controls=[
                    Icon(icon, color=cor, size=22),
                    Text(texto, size=14),
                    Icon(Icons.CHECK, size=14, color=Colors.RED, visible=visible),
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
                self.cards_prioridade(
                    Icons.FLAG, Colors.GREY, "Prioridade 4", visible=True
                ),
            ],
            spacing=0,
        )
