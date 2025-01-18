from flet import *
from ui.components.segunda_camada.lembretes import Lembretes
from ui.components.segunda_camada.prioridade import Card_prioridade
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.calendario import Calendario



class ControlerSegundaCamada:
    def __init__(self):
        self.calendario = Calendario()
        self.prioridade = Card_prioridade(self)
        self.tarefa = Tarefa_vencimento(self.calendario,self)
        self.lembretes = Lembretes(self)
        self.calendario.load_more_months(3)
        self.segunda_camada_visible = True
        self.content = None
        self.show_segunda_camada()
        
    def show_segunda_camada(self):
        if any([self.prioridade.visible, self.tarefa.visible, self.lembretes.visible]):
            self.content.visible = True
        else:
            self.content.visible = False
            
    def show_prioridade(self, e):
        pass
        
    
    def build(self):
        return Container(
                    content=Stack(
                        [
                            self.prioridade,
                            self.tarefa,
                            self.lembretes,
                        ]
                    ),
                    expand=True,
                    visible=self.segunda_camada_visible,
                )