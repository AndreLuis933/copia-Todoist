from flet import *


class HoverAdicionarTarefa:
    def __init__(self, controler_segunda_camada):
        self.controler_segunda_camada = controler_segunda_camada
        self.button_hovered = False
        self.ativor_envio = False
        self.button = None
        self.card_container = []
        self.edit = None
        self.atual = None

    def apply_edit_back(self, card):
        """Aplica a função edit_back ao cartão fornecido."""
        card.edit_back(card.edit, card.task_id)

    def card_edit(self):
        """Lógica para editar um cartão."""
        for card in self.card_container:
            if card.data and card.data != self.edit.content.task_id:
                self.apply_edit_back(card)
                self.card_container.remove(card)
            else:
                card.visible = False
        self.edit.content.visible = True
        self.button.visible = True

    def card_add(self, e):
        """Lógica para adicionar um cartão."""
        for card in self.card_container:
            if card.data:
                self.apply_edit_back(card)
                card.edit_back(card.edit, card.task_id)
                self.card_container.remove(card)

        self.edit = None
        self.button.visible = not self.button.visible
        self.card_container[0].visible = not self.card_container[0].visible

        self.toggle_card()

    def obter_card_visivel(self):
        for card in self.card_container:
            if card.visible:
                return card
        return None  # Retorna None se nenhum card estiver visível

    def card_save(self, e):
        """Lógica para salvar um cartão."""
        visives = [card.visible for card in self.card_container]
        cards_visiveis = [card for card in self.card_container if card.visible]
        print(self.obter_card_visivel())
        print(cards_visiveis)
        
        
        if self.edit:
            self.edit.content.visible = not self.edit.content.visible
            for card in self.card_container:
                if card.data == self.edit.content.task_id:
                    self.card_container.remove(card)
                    break
            self.apply_edit_back(self.edit.content)
            self.edit = None
        elif self.button.visible != any(visives):
            self.button.visible = not self.button.visible
            self.card_container[0].visible = not self.card_container[0].visible

        self.toggle_card()

    def toggle_card(self):
        """Reinicia o estado do hover."""
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
        #atual = self.card_container[0]
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
