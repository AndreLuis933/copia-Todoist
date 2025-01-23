from flet import *

class HoverAdicionarTarefa:
    def __init__(self, controler_segunda_camada):
        self.button_hovered = False
        self.ativor_envio = False
        self.button = None
        self.card_container = None
        self.controler_segunda_camada = controler_segunda_camada

    def toggle_card(self, e):
        self.button.visible = not self.button.visible
        self.card_container.visible = not self.card_container.visible
        # Reinicia o estado do hover
        self.controler_segunda_camada.hide_all()
        self.button_hovered = False
        self.ativor_envio = False
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
        
        botao = self.card_container.content.controls[3].controls[1]
        if self.ativor_envio:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
            botao.update()
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True
            botao.update() 

    def ativar_envio(self, e):
        self.ativor_envio = e.data == "true"
        self.update_button_appearance()
        self.card_container.update()


