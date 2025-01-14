from flet import *


class Card_adicionar_tarefa(Container):
    def __init__(self, compartilhado, tarefa_vencimento):
        super().__init__()
        self.visible = True
        self.compartilhado = compartilhado
        self.tarefa_vencimento = tarefa_vencimento
        self.compartilhado.card_container = self
        self.padding = padding.all(16)
        self.border_radius = border_radius.all(10)
        self.border = border.all(0.3, Colors.OUTLINE)
        self.content = self.build()

    def on_vencimento_click(self, e):
        self.tarefa_vencimento.show_card(e)

    def build(self):
        return Column(
            controls=[
                TextField(label="Nome da tarefa"),
                TextField(label="Descrição", multiline=True),
                Row(
                    controls=[
                        Container(
                            content=Row(
                                controls=[
                                    Icon(
                                        name=Icons.CALENDAR_TODAY,
                                        size=18,
                                        color=Colors.ON_SURFACE_VARIANT,
                                    ),
                                    Text(
                                        "Vencimento",
                                        size=14,
                                        color=Colors.ON_SURFACE,
                                    ),
                                ],
                                spacing=4,
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER,
                            ),
                            padding=padding.symmetric(horizontal=12, vertical=6),
                            border_radius=border_radius.all(5),
                            ink=True,
                            on_click=self.on_vencimento_click,
                            border=border.all(0.3, Colors.OUTLINE),
                        ),
                        ElevatedButton(
                            text="Prioridade",
                            icon=Icons.FLAG,
                        ),
                        ElevatedButton(
                            text="Lembretes",
                            icon=Icons.NOTIFICATIONS,
                        ),
                        IconButton(icon=Icons.MORE_VERT),
                    ],
                    spacing=8,
                ),
                Row(
                    controls=[
                        ElevatedButton(
                            text="Cancelar",
                            on_click=self.compartilhado.toggle_card,
                            bgcolor=Colors.BLACK,
                            color=Colors.WHITE,
                        ),
                        ElevatedButton(
                            text="Adicionar tarefa",
                            bgcolor=Colors.RED,
                            color=Colors.WHITE,
                            disabled=True,
                        ),
                    ],
                    alignment=MainAxisAlignment.END,
                ),
            ],
            spacing=12,
        )
