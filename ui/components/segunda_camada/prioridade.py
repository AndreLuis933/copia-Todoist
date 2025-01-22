from flet import *


class Card_prioridade(Container):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.selected_priority = None
        self.content = self.build()
        self.width = 150
        self.height = 170
        self.left = 350
        self.top = 170  

    def select_priority(self, e, priority):
        self.selected_priority = priority
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
            on_click=lambda e: self.select_priority(e, texto),
            ink=True,
        )

    def build(self):
        return Container(
            content=Column(
                controls=[
                    self.cards_prioridade(Icons.FLAG, Colors.RED, "Prioridade 1"),
                    self.cards_prioridade(Icons.FLAG, Colors.ORANGE, "Prioridade 2"),
                    self.cards_prioridade(Icons.FLAG, Colors.BLUE, "Prioridade 3"),
                    self.cards_prioridade(Icons.FLAG, Colors.GREY, "Prioridade 4"),
                ],
                spacing=8,
            ),
            bgcolor=Colors.SURFACE,
            border=border.all(0.5, Colors.OUTLINE),
            border_radius=border_radius.all(10),
            padding=padding.all(8),
        )
