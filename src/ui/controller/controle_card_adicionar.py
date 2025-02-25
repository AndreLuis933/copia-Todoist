from flet import *
from ui.components.primeira_camada.card_adicionar_tarefa import Card_adicionar_tarefa


class ControleCardAdicionarTarefa:
    def __init__(self, controler_primeira, controler_segunda, hover_control):
        self.controler_primeira = controler_primeira
        self.controler_segunda = controler_segunda
        self.hover_control = hover_control
    
    def show_card(self):
        return Card_adicionar_tarefa(self.controler_primeira, self.controler_segunda, self.hover_control)
        


