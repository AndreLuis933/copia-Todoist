from flet import *
from ui.components.segunda_camada.lembretes import Lembretes
from ui.components.segunda_camada.prioridade import Card_prioridade
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.calendario import Calendario


class ControlerSegundaCamada:
    def __init__(self):
        self.calendario = Calendario()
        self.prioridade = Card_prioridade()
        self.tarefa = Tarefa_vencimento(self.calendario)
        self.lembretes = Lembretes()
        self.calendario.load_more_months(3)

    def get_controls(self):
        return [self.prioridade, self.tarefa, self.lembretes]

    def hide_all(self):
        for control in self.get_controls():
            control.visible = False
        self.lembretes.dropdown.visible = False
        self.tarefa.hora.visible = False

    def show_lembretes(self, e=None):
        self.hide_all()
        self.lembretes.visible = True
        self.update()
        

    def show_tarefa(self, e=None):
        self.hide_all()
        self.tarefa.visible = True
        self.update()

    def show_prioridade(self, e=None):
        self.hide_all()
        self.prioridade.visible = True
        self.update()
        

    def default(self, e=None):
        self.hide_all()
        self.update()

    def update(self):
        for control in self.get_controls():
            if control.page:
                control.page.update()
        
    
