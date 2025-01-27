from flet import *
from ..utils.horarios_em_15_minutos import gerar_horarios_24h_15min_intervalo
from ..utils.is_today_or_tomorrow import is_today_or_tomorrow
from ..unitarios.dropdow import downdown_custon


class Lembretes(Container):
    def __init__(self, controler):
        super().__init__()
        self.controler = controler
        self.visible = True
        self.padding = 10
        self.bgcolor = Colors.GREY_900
        # self.width = 300
        # self.height = 300
        # self.left = 470
        # self.top = 170
        self.top = 1
        self.border_radius = 10
        self.horarios = gerar_horarios_24h_15min_intervalo()
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

    def adicionar_lembrete(self, data_string,date, indice):
        return Container(
            Column(
                [
                    Row(
                        [
                            Icon(Icons.ACCESS_TIME_FILLED, color=Colors.WHITE54),
                            Text(data_string, size=14,color=Colors.WHITE),
                            Container(expand=True),
                            Container(
                                Icon(Icons.CLOSE, size=14, color=Colors.WHITE54),
                                on_click=lambda e: self.deletar(e,date,indice),
                            ),
                        ],
                    ),
                    Divider(height=2),
                ],
            ),
            padding=padding.only(top=6, left=10, right=10),
            width=270,
        )

    def deletar(self,e, date, indice):        
        #self.content.controls[1].controls.pop(indice)
        self.content.controls[1].controls.remove(self.content.controls[1].controls[indice])
        self.controler.save.lembrete.remove(date)
        self.update()
        
    def envio(self, e):
        selecionada = self.content.controls[2].controls[0].selected_index
        tab = self.content.controls[2].controls[0].tabs[selecionada]
        
        resultado = tab.content.content.controls[0].value
        if not selecionada:
            date, resultado = is_today_or_tomorrow(resultado)
        indice = len(self.content.controls[1].controls)
        self.content.controls[1].controls.append(self.adicionar_lembrete(resultado,date,indice))
        self.controler.save.lembrete.append(date)
        self.update()
        #print(self.controler.save.lembrete)

    def tabs(self, title, content_dropdown, description):
        return Tab(
            text=title,
            content=Container(
                Column(
                    [
                        downdown_custon(content_dropdown, Icons.ACCESS_TIME_FILLED),
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
                Text(
                    "Lembretes",
                    size=16,
                    weight="bold",
                ),
                Column(),
                Column(
                    [
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
                    width=270,
                ),
            ],
        )
