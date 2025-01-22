from flet import *


class DownDownCuston(Container):
    def __init__(self, lista):
        super().__init__()
        self.list = lista
        self.content = self.build()

    def build(self):
        return Dropdown(
            icon=Icons.ACCESS_TIME_FILLED,
            value=self.list[0],
            bgcolor=Colors.GREY_900,
            alignment=alignment.center,
            max_menu_height=500,
            options=[dropdown.Option(texto) for texto in self.list],
        )
