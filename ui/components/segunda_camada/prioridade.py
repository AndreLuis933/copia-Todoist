from flet import *
import flet


class Card_prioridade(Container):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.selected_priority = None
        self.content = self.build()
        self.width = 150
        self.height = 170
        self.left = 350  # Posição fixa à esquerda
        self.top = 200  # Posição fixa no topo

    def show_card(self, e):
        self.visible = not self.visible
        self.update()

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


if __name__ == "__main__":

    def main(page: Page):
        page.window.always_on_top = True
        app = Card_prioridade()

        prioridade_button = ElevatedButton(
            text="Prioridade",
            icon=Icons.FLAG,
            on_click=app.toggle_menu,
        )

        # Layout principal
        completo = Stack(
            controls=[
                Row(
                    Container(
                        content=prioridade_button,
                        alignment=alignment.top_left,
                    ),
                    expand=True,
                    bgcolor=Colors.ON_SURFACE_VARIANT,
                ),
                app,
            ],
            width=page.window_width,
            height=page.window_height,
        )
        page.add(completo)
        page.update()

    flet.app(target=main)
