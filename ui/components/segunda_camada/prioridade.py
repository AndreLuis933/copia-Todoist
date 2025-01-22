from flet import *


class Card_prioridade(Container):
    def __init__(self):
        super().__init__()
        self.visible = True
        self.selected_priority = None
        self.content = self.build()
        self.width = 150
        self.height = 160
        self.left = 350
        self.top = 170
        self.bgcolor = "#1E1E1E"
        self.border = border.all(0.5, Colors.OUTLINE)
        self.border_radius = border_radius.all(10)

    def select_priority(self, e, priority):
        self.selected_priority = priority
        self.visible = False
        print(f"Prioridade selecionada: {priority}")
        self.update()

    def  high_light(self, e):
        pass
        if e.data == "true":
            e.control.bgcolor = '#383838'
            e.control.update()
        else:
            e.control.bgcolor = '#272727'
            e.control.update()

    def cards_prioridade(self, icon, cor, texto):
        return Container(
            content=Row(
                controls=[
                    Icon(icon, color=cor, size=22),
                    Text(texto, size=14),
                ],
            ),
            padding=padding.symmetric(vertical=4, horizontal=8),
            height=int(self.height)/4,
            on_click=lambda e: self.select_priority(e, texto),
            bgcolor='#272727',
            on_hover=self.high_light,
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
