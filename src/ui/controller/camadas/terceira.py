from flet import *
from ...components.terceira_camada.color_dropdown import ColorDropdown
from ...components.terceira_camada.tarefa_hora import Tarefa_hora


class ControlerTerceiraCamada:
    def __init__(self, segunda_camada, primeira_camada):
        self.primeira_camada = primeira_camada
        self.segunda_camada = segunda_camada
        self.color_dropdown = ColorDropdown(self.segunda_camada, self)
        self.tarefa_hora = Tarefa_hora(self.segunda_camada, self)
        self.controls = [
            self.detector(),
            self.color_dropdown,
            self.tarefa_hora,
        ]

    def active_detector(self):
        self.controls[0].visible = True

    def detector(self):
        return GestureDetector(
            visible=False,
            on_tap=self.default,
            content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
        )

    def hide_all(self):
        for control in self.controls:
            control.visible = False
        self.controls[0].visible = False
        self.update()

    def default(self, e=None):
        self.hide_all()
        self.update()

    def update(self):
        for control in self.controls:
            if control.page:
                control.page.update()
                break
