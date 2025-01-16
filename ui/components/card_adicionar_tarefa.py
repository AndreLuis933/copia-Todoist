from flet import *


class Card_adicionar_tarefa(Container):
    def __init__(self, hover_control, tarefa_vencimento, prioridade):
        super().__init__()
        self.hover_control = hover_control
        self.prioridade = prioridade
        self.hover_control.card_container = self
        self.tarefa_vencimento = tarefa_vencimento
        self.visible = False
        self.padding = padding.only(left=16, right=16, bottom=8)
        self.border_radius = border_radius.all(10)
        self.border = border.all(0.3, Colors.OUTLINE)
        self.content = self.build()

    def ativar_envio(self, e):
        botao = self.content.controls[3].controls[1]
        if e.data:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
            botao.update()
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True
            botao.update()

    def card_definitions(self, icon, label=None, on_click=None):
        return Container(
            content=Row(
                controls=[
                    Icon(
                        name=icon,
                        size=18,
                        color=Colors.ON_SURFACE_VARIANT,
                    ),
                    Text(
                        label,
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
            on_click=lambda e: on_click(e) if on_click else None,
            border=border.all(0.3, Colors.OUTLINE),
        )

    def build(self):
        return Column(
            controls=[
                Container(
                    Column(
                        controls=[
                            TextField(
                                hint_text="Nome da tarefa",
                                autofocus=True,
                                on_change=lambda e: self.ativar_envio(e),
                                border=InputBorder.NONE,
                                height=30,
                            ),
                            TextField(
                                hint_text="Descrição",
                                multiline=True,
                                text_size=14,
                                border=InputBorder.NONE,
                                height=35,
                            ),
                        ],
                        spacing=0,
                    ),
                    padding=0,
                    margin=0,
                ),
                Row(
                    controls=[
                        self.card_definitions(
                            Icons.CALENDAR_TODAY,
                            "Vencimento",
                            self.tarefa_vencimento.show_card,
                        ),
                        self.card_definitions(
                            Icons.FLAG,
                            "Prioridade",
                            self.prioridade.toggle_menu,
                        ),
                        self.card_definitions(Icons.NOTIFICATIONS, "Lembretes"),
                        Container(
                            content=Icon(
                                name=Icons.MORE_HORIZ,
                                size=18,
                                color=Colors.ON_SURFACE_VARIANT,
                            ),
                            padding=padding.symmetric(horizontal=8, vertical=6),
                            border_radius=border_radius.all(5),
                            ink=True,
                            on_click=lambda e: None,
                            border=border.all(0.3, Colors.OUTLINE),
                        ),
                    ],
                    spacing=8,
                ),
                Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4),
                Row(
                    controls=[
                        ElevatedButton(
                            text="Cancelar",
                            on_click=self.hover_control.toggle_card,
                            bgcolor=Colors.GREY_800,
                            color=Colors.WHITE70,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=8),
                            ),
                        ),
                        ElevatedButton(
                            text="Adicionar tarefa",
                            on_click=lambda e: print("adicionar tarefa"),
                            disabled=True,
                            bgcolor=Colors.RED_900,
                            color=Colors.WHITE,
                            opacity=0.3,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=8),
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.END,
                ),
            ],
            spacing=12,
        )
