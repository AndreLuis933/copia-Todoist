from flet import *
from ui.components.segunda_camada.lembretes import Lembretes
from ui.components.segunda_camada.prioridade import Card_prioridade
from ui.components.segunda_camada.tarefa_vencimento import Tarefa_vencimento
from ui.components.utils.calendar import Calendario
from ui.components.segunda_camada.more_options import MoreOptions


class ControlerSegundaCamada:
    def __init__(self, primeira_camada):
        self.primeira_camada = primeira_camada
        self.save = self.primeira_camada.save
        self.calendario = Calendario(self)
        self.prioridade = Card_prioridade(self)
        self.tarefa = Tarefa_vencimento(self, self.calendario)
        self.lembretes = Lembretes(self)
        self.more_options = MoreOptions()
        self.calendario.load_more_months(3)
        self.controls = [
            self.detector(),
            self.prioridade,
            self.tarefa,
            self.lembretes,
            self.more_options,
        ]

    def atualizar_lembretes(self):
        self.lembretes.content.controls[2].controls[0].tabs[1] = self.lembretes.tabs(
            "Antes da Tarefa",
            list(self.lembretes.opcoes_dropdown_2.keys()),
            "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
            self.lembretes.texto_alternativo(),
        )
        self.update()

    def detector(self):
        return GestureDetector(
            visible=False,
            on_tap=self.default,
            content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
        )

    def active_detector(self):
        self.controls[0].visible = True

    def hide_all(self):
        for control in self.controls:
            control.visible = False
        self.tarefa.hora.visible = False
        self.controls[0].visible = False
        self.update()

    def show_lembretes(self, e=None):
        self.hide_all()
        self.active_detector()
        self.lembretes.visible = True
        self.update()

    def show_tarefa(self, e=None):
        self.hide_all()
        self.active_detector()
        self.tarefa.visible = True
        self.update()

    def show_prioridade(self, e=None):
        self.hide_all()
        self.active_detector()
        self.prioridade.visible = True
        self.update()

    def show_more_options(self, e=None):
        self.hide_all()
        self.active_detector()
        self.more_options.visible = True
        self.update()

    def default(self, e=None):
        self.hide_all()
        self.update()

    def update(self):
        for control in self.controls:
            if control.page:
                control.page.update()
                break
