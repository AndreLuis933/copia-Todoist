from flet import *
from ..utils.horarios_em_15_minutos import gerar_horarios_24h_15min_intervalo
from ..utils.is_today_or_tomorrow import is_today_or_tomorrow
from ..unitarios.dropdow import downdown_custon
from ..utils.ajuste_tempo import ajusta_tempo
from datetime import datetime, timedelta


class Lembretes(Container):
    def __init__(self, controler):
        super().__init__()
        self.controler = controler
        self.visible = False
        self.padding = 10
        self.bgcolor = Colors.GREY_900
        self.left = 470
        self.top = 170
        # self.top = 1
        self.border_radius = 10
        self.horarios = gerar_horarios_24h_15min_intervalo()
        self.opcoes_dropdown_2 = {
            "No horário da tarefa": (timedelta(), "0m antes"),
            "10 min antes": (timedelta(minutes=-10), "10m antes"),
            "30 min antes": (timedelta(minutes=-30), "30m antes"),
            "45 min antes": (timedelta(minutes=-45), "45m antes"),
            "1 hora antes": (timedelta(hours=-1), "1h antes"),
            "2 horas antes": (timedelta(hours=-2), "2h antes"),
            "3 horas antes": (timedelta(hours=-3), "3h antes"),
            "1 dia antes": (timedelta(days=-1), "1d antes"),
            "2 dias antes": (timedelta(days=-2), "2d antes"),
            "3 dias antes": (timedelta(days=-3), "3d antes"),
            "1 semana antes": (timedelta(weeks=-1), "1w antes"),
        }
        self.content = self.build()
        self.ativor_envio = True
        self.close = False

    def adicionar_lembrete(self, date, data_string, tab):
        return Container(
            Column(
                [
                    Row(
                        [
                            Icon(Icons.ACCESS_TIME_FILLED, color=Colors.WHITE54),
                            Text(data_string, size=14, color=Colors.WHITE),
                            Container(expand=True),
                            Container(
                                Icon(Icons.CLOSE, size=14, color=Colors.WHITE54),
                                on_click=lambda _: self.deletar(date, data_string, tab),
                            ),
                        ],
                    ),
                    Divider(height=2),
                ],
            ),
            padding=padding.only(top=6, left=10, right=10),
            width=270,
        )

    def deletar(self, date, data_string, tab):
        def encontrar_chave_por_valor(dicionario, valor_procurado):
            for chave, (_, valor) in dicionario.items():
                if valor == valor_procurado:
                    return chave
            return None  # Retorna None se não encontrar

        controle = self.content.controls[1].controls
        for i, container in enumerate(controle):
            if controle[i].content.controls[0].controls[1].value == data_string:
                controle.remove(container)
                break

        dropdown = (
            self.content.controls[2].controls[0].tabs[tab].content.content.controls[0]
        )
        options = dropdown.options
        condisao = (
            encontrar_chave_por_valor(self.opcoes_dropdown_2, data_string)
            if tab
            else data_string.split(" ", maxsplit=1)[1]
        )
        for option in options:
            if option.key == condisao:
                option.visible = True
                break

        self.controler.save.lembrete.remove((date, data_string, tab))

        dropdown.visible = True
        self.ativor_envio = True
        self.close = False
        self.update_button_appearance_envio()
        self.update()

    def clear_all_elements(self):
        controles = self.content.controls[1].controls
        for controle in controles[:]:
            controle.content.controls[0].controls[3].on_click(None)
        self.update()

    def update_button_appearance_envio(self):
        botao = self.content.controls[2].controls[1].controls[0]
        if self.ativor_envio:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True

    def adicionar_todos_lembretes(self, lembretes):
        for lembrete in lembretes:
            self.content.controls[1].controls.append(self.adicionar_lembrete(*lembrete))
            self.controler.save.lembrete.append(lembrete)

    def envio(self, e):
        selecionada = self.content.controls[2].controls[0].selected_index
        tab = self.content.controls[2].controls[0].tabs[selecionada]

        def proximo_visivel(options, resultado):
            if not options:
                return None

            inicio = next(
                (i for i, opt in enumerate(options) if opt.key == resultado), -1
            )
            if inicio == -1:
                return None

            options[inicio].visible = False

            for i in range(1, len(options) + 1):
                indice = (inicio + i) % len(options)
                if options[indice].visible:
                    return options[indice].key

            return None

        dropdown = tab.content.content.controls[0]
        resultado = dropdown.value
        options = dropdown.options
        if not selecionada:
            date, exibir = is_today_or_tomorrow(resultado)
        else:
            atual = self.opcoes_dropdown_2.get(resultado)
            if not atual:
                dropdown.visible = False
                self.update()
                return

            delta, exibir = atual
            date = self.controler.save.vencimento + delta

        self.content.controls[1].controls.append(
            self.adicionar_lembrete(date, exibir, selecionada)
        )
        self.controler.save.lembrete.append((date, exibir, selecionada))
        proximo = proximo_visivel(options, resultado)

        if proximo:
            dropdown.value = proximo
        else:
            dropdown.visible = False
            self.ativor_envio = False
            self.close = True
        self.update_button_appearance_envio()
        self.update()

    def texto_alternativo(self):
        return (
            Container(
                Column(
                    [
                        Text(
                            "Primeiro adicione um horário à tarefa.",
                            size=14,
                        ),
                    ]
                ),
            )
            if self.controler.save.hora is None
            else None
        )

    def tabs(self, title, content_dropdown, description, condicao=None):
        return Tab(
            text=title,
            content=(
                Container(
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
                )
                if not condicao
                else condicao
            ),
        )

    def ativar_envio(self, e):
        if e.data == "0":
            self.ativor_envio = True
        else:
            if self.close:
                self.ativor_envio = False

        self.update_button_appearance_envio()
        self.update()

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
                            on_change=lambda e: self.ativar_envio(e),
                            tabs=[
                                self.tabs(
                                    "Data & Hora",
                                    self.horarios,
                                    "Defina uma notificação para um horário específico (09h00) ou data e horário (seg 18h00).",
                                ),
                                self.tabs(
                                    "Antes da Tarefa",
                                    list(self.opcoes_dropdown_2.keys()),
                                    "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                                    self.texto_alternativo(),
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
