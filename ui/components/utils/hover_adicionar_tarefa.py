from flet import *

class HoverAdicionarTarefa:
<<<<<<< HEAD
    def __init__(self):
        self.button_hovered = False
        self.button = None
        self.card_container = None
=======
    def __init__(self, controler_segunda_camada):
        self.button_hovered = False
        self.button = None
        self.card_container = None
        self.controler_segunda_camada = controler_segunda_camada
>>>>>>> trabalho-temporario

    def toggle_card(self, e):
        self.button.visible = not self.button.visible
        self.card_container.visible = not self.card_container.visible
        # Reinicia o estado do hover
<<<<<<< HEAD
=======
        self.controler_segunda_camada.hide_all()
>>>>>>> trabalho-temporario
        self.button_hovered = False
        self.update_button_appearance()
        self.button.page.update()

    def mudar_cor(self, e):
        self.button_hovered = e.data == "true"
        self.update_button_appearance()
        self.button.page.update()

    def update_button_appearance(self):
        if self.button_hovered:
            self.button.content.controls[1].color = Colors.RED
            self.button.content.controls[0].controls[1].name = Icons.ADD_CIRCLE
            self.button.content.controls[0].controls[0].visible = True
        else:
            self.button.content.controls[1].color = Colors.WHITE
            self.button.content.controls[0].controls[1].name = Icons.ADD
            self.button.content.controls[0].controls[0].visible = False
