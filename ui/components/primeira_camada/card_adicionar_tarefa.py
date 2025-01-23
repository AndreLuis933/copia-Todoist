from flet import *
from app.database.operations import salvar_tarefa

class Card_adicionar_tarefa(Container):
    def __init__(self, controler, hover_control):
        super().__init__()
        self.controler = controler
        self.hover_control = hover_control
        self.hover_control.card_container = self
        self.visible = False
        self.padding = padding.only(left=16, right=16, bottom=8)
        self.border_radius = border_radius.all(10)
        self.border = border.all(0.3, Colors.OUTLINE)
        self.content = self.build()

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

    def enviar(self, e):
        title_field = self.content.controls[0].content.controls[0]
        description_field = self.content.controls[0].content.controls[1]

        title = title_field.value
        description = description_field.value
        values = [title, description]

        salvar_tarefa(values)

        title_field.value = None
        description_field.value = None

        self.hover_control.toggle_card(e)
        self.update()

    def build(self):
        return Column(
            [
                Container(
                    Column(
                        controls=[
                            TextField(
                                hint_text="Nome da tarefa",
                                autofocus=True,
                                on_change=lambda e: self.hover_control.ativar_envio(e),
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
                            self.controler.show_tarefa,
                        ),
                        self.card_definitions(
                            Icons.FLAG,
                            "Prioridade",
                            self.controler.show_prioridade,
                        ),
                        self.card_definitions(
                            Icons.NOTIFICATIONS,
                            "Lembretes",
                            self.controler.show_lembretes,
                        ),
                        Container(
                            content=Icon(
                                name=Icons.MORE_HORIZ,
                                size=18,
                                color=Colors.ON_SURFACE_VARIANT,
                            ),
                            padding=padding.symmetric(horizontal=8, vertical=6),
                            border_radius=border_radius.all(5),
                            ink=True,
                            on_click=lambda e: self.controler.show_more_options(e),
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
                            on_click=lambda e: self.enviar(e),
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
