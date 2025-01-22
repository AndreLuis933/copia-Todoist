from flet import *
from ..utils.horarios_em_15_minutos import horarios_15_minutos
from ..unitarios.dropdow import downdown_custon


class Lembretes(Container):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.padding = 10
        self.bgcolor = Colors.GREY_900
        self.width = 300
        self.height = 300
        self.left = 470
        self.top = 170
        self.border_radius = 10
        self.horarios = horarios_15_minutos()
        self.opcoes_dropdown_2 = [
            "No horário da tarefa",
            "10 min antes",
            "30 min antes",
            "45 min antes",
            "1 hora antes",
            "2 horas antes",
            "3 horas antes",
            "1 dia antes",
            "2 dias antes",
            "3 dias antes",
            "1 semana antes",
        ]
        self.content = self.build()

    def envio(self, e):
        selecionada = self.content.controls[1].selected_index
        tab = self.content.controls[1].tabs[selecionada]

        print(tab.content.content.controls[0].content.value)

    def tabs(self, title, content_dropdown, description):
        return Tab(
            text=title,
            content=Container(
                Column(
                    [
                        downdown_custon(content_dropdown,Icons.ACCESS_TIME_FILLED),
                        Text(
                            description,
                            size=14,
                        ),
                    ]
                ),
                padding=10,
                border_radius=20,
            ),
        )

    def build(self):
        return Column(
            [
                Text("Lembretes", size=20, weight="bold"),
                Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        self.tabs(
                            "Data & Hora",
                            self.horarios,
                            "Defina uma notificação para um horário específico (09h00) ou data e horário (seg 18h00).",
                        ),
                        self.tabs(
                            "Antes da Tarefa",
                            self.opcoes_dropdown_2,
                            "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                        ),
                    ],
                    width=300,
                    height=190,
                ),
                Row(
                    [
                        ElevatedButton(
                            text="Adicionar lembrete",
                            on_click=lambda e: self.envio(e),
                            bgcolor=Colors.RED,
                            color=Colors.WHITE,
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=4),
                            ),
                        )
                    ],
                    alignment=MainAxisAlignment.END,
                ),
            ],
            spacing=0,
        )
