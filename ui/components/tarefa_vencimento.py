from flet import *


class Tarefa_vencimento(Container):
    def __init__(self, calendario):
        super().__init__()
        self.calendario = calendario
        self.current_date = self.calendario.current_date
        self.padding = 15
        self.border_radius = 10
        self.shadow = BoxShadow(blur_radius=5)
        self.visible = False
        self.width = 250
        self.height = 700
        self.left = 220  # Posição fixa à esquerda
        self.top = 170  # Posição fixa no topo
        self.content = self.build()

    def show_card(self, e):
        self.visible = True
        self.update()

    def hide_card(self, e):
        self.visible = False
        self.update()

    def opcoes_rapidas(self, texto, icone, cor, complemento):
        return Container(
            bgcolor=Colors.GREY_900,
            on_click=lambda _: print(texto),
            padding=padding.all(10),
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

    def build(self):
        return Column(
            [
                TextField(
                    hint_text="Digite um vencimento",
                ),
                Divider(),
                self.opcoes_rapidas("Hoje", Icons.TODAY, Colors.GREEN_400, "sab"),
                self.opcoes_rapidas(
                    "Amanha", Icons.WB_SUNNY_OUTLINED, Colors.AMBER_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proxima semana", Icons.NEXT_WEEK, Colors.PURPLE_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proximo fim de semana", Icons.CHAIR, Colors.BLUE_400, "sab"
                ),
                Divider(),
                # Calendário
                Text(f"{self.current_date.strftime('%b %Y')}", size=16, weight="bold"),
                self.calendario,
                Divider(),
                ElevatedButton("Fechar", on_click=self.hide_card),
            ]
        )
