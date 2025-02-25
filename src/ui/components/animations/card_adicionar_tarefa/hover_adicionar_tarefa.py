from flet import *


class HoverAdicionarTarefa:
    def __init__(self, controler_segunda_camada):
        self.controler_segunda_camada = controler_segunda_camada
        self.button_hovered = False
        self.ativor_envio = False
        self.button = None
        self.card_container = []
        self.edit = None

    def show_card_edit(self):
        for card in self.card_container:
            if card.edit and card.edit.data != self.edit.content.task_id:
                card.edit_back(card.edit,card.task_id)
            if card.data !=self.edit.content.task_id and card.data:
                self.card_container.remove(card)
            else:
                card.visible = False
        self.edit.content.visible = True
        self.button.visible = True
    
    def card_add(self,e):
        for card in self.card_container:
            if card.edit:
                card.edit_back(card.edit,card.task_id)
            if card.data:
                self.card_container.remove(card)
        
        self.edit = None
        
        self.button.visible = not self.button.visible
        self.card_container[0].visible = not self.card_container[0].visible
        self.controler_segunda_camada.hide_all()
        self.button_hovered = False
        self.ativor_envio = False
        self.update_button_appearance()
        self.update_button_appearance_envio()
        self.button.page.update()
        
    def toggle_card(self, e):

        if self.edit:
             self.edit.content.visible = not self.edit.content.visible
             for i in self.card_container:
                 if i.data ==self.edit.content.task_id:
                     self.card_container.remove(i)
                     break
             self.edit.content.edit_back(self.edit,self.edit.content.task_id)
             self.edit = None
        elif self.button.visible !=  any([card.visible for card in self.card_container]):
            self.button.visible = not self.button.visible
            self.card_container[0].visible = not self.card_container[0].visible
        
        
        # Reinicia o estado do hover
        self.controler_segunda_camada.hide_all()
        self.button_hovered = False
        self.ativor_envio = False
        self.update_button_appearance()
        self.update_button_appearance_envio()
        self.button.page.update()

    def mudar_cor(self, e):
        self.button_hovered = e.data == "true"
        self.update_button_appearance()
        self.button.update()

    def update_button_appearance(self):
        if self.button_hovered:
            self.button.content.controls[1].color = Colors.RED
            self.button.content.controls[0].controls[1].name = Icons.ADD_CIRCLE
            self.button.content.controls[0].controls[0].visible = True
        else:
            self.button.content.controls[1].color = Colors.WHITE54
            self.button.content.controls[0].controls[1].name = Icons.ADD
            self.button.content.controls[0].controls[0].visible = False

    def update_button_appearance_envio(self):
        atual = self.edit.content if self.edit else self.card_container[0]
        botao = atual.content.controls[3].controls[-1]
        if self.ativor_envio:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True

    def ativar_envio(self, e):
        self.ativor_envio = len(e.data.strip()) > 0
        self.update_button_appearance_envio()
        self.button.page.update()
