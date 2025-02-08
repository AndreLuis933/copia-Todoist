from flet import *
from tzlocal import get_localzone
from ..unitarios.dropdow import downdown_custon
from ..utils.horarios_em_15_minutos import (
    gerar_horarios_24h_15min_intervalo,
    gerar_duracoes_ate_23h30,
)
from datetime import datetime, time
import re


class Tarefa_hora(Container):
    def __init__(self, segunda_camada, terceira_camada):
        super().__init__()
        self.segunda_camada = segunda_camada
        self.terceira_camada = terceira_camada
        self.tarefa = segunda_camada.tarefa
        self.visible = False
        self.padding = padding.only(left=10, right=10, top=20, bottom=20)
        self.bgcolor = self.tarefa.bgcolor
        self.border = self.tarefa.border
        self.height = 200
        self.width = 300
        self.border_radius = 10
        self.left = self.tarefa.left - 20
        self.top = self.tarefa.top + 310
        self.content = self.build()

    def build_hora_container(self, text, lista):
        return Row(
            [
                Text(
                    text,
                    size=14,
                    weight="bold",
                ),
                Container(
                    downdown_custon(lista, height=30),
                    width=180,
                ),
            ],
            spacing=0,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )

    def salvar_hora(self, e):
        valores = [self.content.controls[i].controls[1].content.value for i in range(2)]
        hora, duracao = valores

        match = re.match(r"(\d{1,2}):(\d{2})\s*(AM|PM)?", hora, re.IGNORECASE)

        if match:
            horas, minutos, periodo = match.groups()
            horas = int(horas)
            minutos = int(minutos)

            if periodo.upper() == "PM" and horas != 12:
                horas += 12
            elif periodo.upper() == "AM" and horas == 12:
                horas = 0

            horario = time(horas % 24, minutos)

        if duracao != "Sem duração":
            print(duracao)

        data = self.segunda_camada.save.data
        if not data:
            data = datetime.now().date()
        self.segunda_camada.save.vencimento = datetime.combine(data, horario)

        self.segunda_camada.save.hora = horario
        self.segunda_camada.atualizar_lembretes()

        self.terceira_camada.hide_all()
        self.segunda_camada.tarefa.update_text()

    def build(self):
        return Column(
            [
                self.build_hora_container("Hora", gerar_horarios_24h_15min_intervalo()),
                self.build_hora_container("Duração", gerar_duracoes_ate_23h30()),
                Row(
                    [
                        Text(
                            "Fuso horário",
                            size=14,
                            weight="bold",
                        ),
                        Container(
                            TextField(
                                get_localzone(),
                                height=30,
                                text_size=14,
                                width=180,
                                text_align=TextAlign.CENTER,
                                content_padding=padding.only(top=5, bottom=5),
                                read_only=True,
                            ),
                            padding=0,
                        ),
                    ],
                    spacing=0,
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                Row(
                    [
                        ElevatedButton(
                            text="Cancelar",
                            on_click=lambda e: self.terceira_camada.hide_all(),
                            bgcolor=self.tarefa.bgcolor,
                            color=Colors.WHITE70,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=6),
                            ),
                        ),
                        ElevatedButton(
                            text="Salvar",
                            width=70,
                            on_click=lambda e: self.salvar_hora(e),
                            bgcolor=Colors.RED,
                            color=Colors.WHITE,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=6),
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.END,
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )
