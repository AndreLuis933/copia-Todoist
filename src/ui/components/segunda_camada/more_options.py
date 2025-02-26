from flet import *
from ..animations.high_light import high_light


class MoreOptions(Container):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.selected_priority = None
        self.width = 250
        self.left = 600
        self.top = 170
        self.bgcolor = "#272727"
        self.border = border.all(0.5, Colors.OUTLINE)
        self.border_radius = border_radius.all(10)
        self.content = self.build()

    def cards_prioridade(self, icon, texto, adicional=None):
        return Container(
            content=Row(
                controls=[
                    Icon(icon, color=Colors.WHITE, size=22),
                    Row(
                        [
                            Text(texto, size=14),
                            Text(adicional if adicional else "", size=14),
                        ],
                        expand=True,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
            ),
            padding=padding.only(top=3, bottom=3, left=16, right=8),
            height=40,
            on_click=lambda e: None,
            bgcolor="#272727",
            on_hover=lambda e: high_light(e,'#272727','#383838'),
        )

    def build(self):
        return Column(
            controls=[
                self.cards_prioridade(Icons.LABEL, "Etiquetas",adicional='@'),
                self.cards_prioridade(Icons.LOCATION_ON, "Local"),
                self.cards_prioridade(Icons.ADJUST, "Prazo"),
                Divider(height=5),
                self.cards_prioridade(Icons.EXTENSION, "Adicionar extenção..."),
                Divider(height=5),
                Container(
                    Text(
                        "Editar ações de tarefas",
                        color=Colors.RED,
                    ),
                    padding=padding.only(top=6, bottom=14, left=16, right=8),
                    on_click=lambda e: print("Editar ações de tarefas"),
                    on_hover=lambda e: high_light(e,'#272727','#383838'),
                    width=self.width,
                ),
            ],
            spacing=0,
        )

    # Magic methods    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}"