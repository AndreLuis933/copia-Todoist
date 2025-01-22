from flet import *


class Tarefa_vencimento(Container):
    def __init__(self, calendario):
        super().__init__()
        self.calendario = calendario
        self.visible = True
        self.current_date = self.calendario.current_date
        self.border_radius = 15
        self.border = border.all(0.7, Colors.GREY_800)
        self.shadow = BoxShadow(blur_radius=5)
        self.bgcolor = "#1E1E1E"
        self.width = 250
        self.left = 220
        self.top = 170
        self.height = 580
        self.content = self.build()
        self.hora = self.build_hora()

    def opcoes_rapidas(self, texto, icone, cor, complemento):
        return Container(
            on_click=lambda _: print(texto),
            padding=padding.only(left=18, right=18),
            ink=True,
            height=35,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        controls=[
                            Icon(icone, color=cor),
                            Text(
                                texto,
                                size=14,
                                weight="bold",
                                expand=True,
                                overflow=TextOverflow.ELLIPSIS,
                                max_lines=1,
                            ),
                        ],
                        expand=True,
                        spacing=10,
                    ),
                    Text(
                        complemento,
                        size=14,
                        weight="bold",
                        color=Colors.GREY_500,
                    ),
                ],
            ),
        )

    def build_hora(self):
        return Container(
            Column(
                [
                    Row(
                        [
                            Text(
                                "Hora",
                                size=14,
                                weight="bold",
                            )
                        ]
                    ),
                    Row(
                        [
                            Text(
                                "Duração",
                                size=14,
                                weight="bold",
                            )
                        ]
                    ),
                    Row(
                        [
                            Text(
                                "Fuso horário",
                                size=14,
                                weight="bold",
                            )
                        ]
                    ),
                    Row(
                        [
                            ElevatedButton(
                                text="Cancelar",
                                on_click=self.show_hora,
                                bgcolor=self.bgcolor,
                                color=Colors.WHITE70,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=6),
                                ),
                            ),
                            ElevatedButton(
                                text="Salvar",
                                width=70,
                                on_click=lambda e: self.envio(e),
                                bgcolor=Colors.RED,
                                color=Colors.WHITE,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=6),
                                ),
                            ),
                        ],
                        alignment=MainAxisAlignment.END,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            visible=True,
            padding=padding.only(left=10, right=10, top=20, bottom=20),
            bgcolor=self.bgcolor,
            border=self.border,
            height=200,
            width=300,
            border_radius=10,
            left=self.left - 20,
            top=self.top + self.height - 270,
        )

    def show_hora(self, e):
        self.hora.visible = not self.hora.visible
        self.page.update()

    def build(self):
        return Column(
            [
                Container(
                    TextField(
                        hint_text="Digite um vencimento",
                        border=InputBorder.NONE,
                        hint_style=TextStyle(color=Colors.GREY_600),
                    ),
                    padding=padding.only(left=16),
                ),
                Divider(height=1),
                self.opcoes_rapidas("Hoje", Icons.TODAY, Colors.GREEN_400, "sab"),
                self.opcoes_rapidas(
                    "Amanha", Icons.WB_SUNNY_OUTLINED, Colors.AMBER_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proximo fim de semana", Icons.CHAIR, Colors.BLUE_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proxima semana", Icons.NEXT_WEEK, Colors.PURPLE_400, "sab"
                ),
                Divider(),
                self.calendario,
                Divider(height=1),
                Container(
                    Row(
                        [
                            Icon(Icons.ACCESS_TIME, color=Colors.GREY_400, size=18),
                            Text("Hora", color=Colors.GREY_400),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                    ),
                    margin=margin.only(top=15, bottom=15, left=5, right=5),
                    border_radius=5,
                    border=border.all(0.7, Colors.GREY_800),
                    height=35,
                    ink=True,
                    on_click=self.show_hora,
                    alignment=alignment.center,
                ),
            ],
            spacing=0,
        )
