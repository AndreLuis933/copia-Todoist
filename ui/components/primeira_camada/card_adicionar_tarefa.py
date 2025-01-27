from flet import *
from app.database.operations import salvar_tarefa


class Card_adicionar_tarefa(Container):
    def __init__(self, controler_primeira, controler_segunda, hover_control):
        super().__init__()
        self.controler_primeira = controler_primeira
        self.controler_segunda = controler_segunda
        self.hover_control = hover_control
        self.hover_control.card_container = self
        self.visible = True
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
        title_field = self.content.controls[0].content.controls[0].controls[1]
        description_field = self.content.controls[0].content.controls[1]

        title = title_field.value.strip()
        description = description_field.value.strip()

        self.controler_primeira.save.title = title
        self.controler_primeira.save.description = description
        self.controler_primeira.save.save_clicked()
        self.hover_control.toggle_card(e)

    def prefixos(self, text, func=None):
        return Container(
            content=Text(
                text,
                color="white",
                weight=FontWeight.BOLD,
                size=16,
            ),
            bgcolor="#7a2c2c",
            padding=padding.only(left=5, right=10, top=0, bottom=2),
            alignment=alignment.bottom_left,
            margin=margin.only(left=0, right=0, top=15, bottom=0),
            on_click=lambda _: func,
            height=35,
        )

    def build(self):
        return Column(
            [
                Container(
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        [
                                            #self.prefixos("Jan 27 1:30 PM"),
                                            #self.prefixos("p2"),
                                        ],
                                        spacing=5,
                                    ),
                                    TextField(
                                        hint_text="Nome da tarefa",
                                        autofocus=True,
                                        border=InputBorder.NONE,
                                        on_change=lambda e: self.hover_control.ativar_envio(
                                            e
                                        ),
                                        height=30,
                                    ),
                                ],
                                spacing=0,
                                alignment=MainAxisAlignment.START,
                                height=40,
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
                            self.controler_segunda.show_tarefa,
                        ),
                        self.card_definitions(
                            Icons.FLAG,
                            "Prioridade",
                            self.controler_segunda.show_prioridade,
                        ),
                        self.card_definitions(
                            Icons.NOTIFICATIONS,
                            "Lembretes",
                            self.controler_segunda.show_lembretes,
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
                            on_click=lambda e: self.controler_segunda.show_more_options(
                                e
                            ),
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
