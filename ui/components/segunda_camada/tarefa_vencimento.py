from datetime import datetime, time
import re
from flet import *

from ui.components.utils.locale_config import temp_locale
from ..unitarios.dropdow import downdown_custon
from ..utils.horarios_em_15_minutos import (
    gerar_horarios_24h_15min_intervalo,
    gerar_duracoes_ate_23h30,
)
from tzlocal import get_localzone
from ..utils.indentificar_datas import identificar_datas, DIAS_SEMANA, MESES


class Tarefa_vencimento(Container):
    def __init__(self, controler, calendario):
        super().__init__()
        self.controler = controler
        self.calendario = calendario
        self.visible = True
        self.current_date = self.calendario.current_date
        self.border_radius = 15
        self.border = border.all(0.7, Colors.GREY_800)
        self.shadow = BoxShadow(blur_radius=5)
        self.bgcolor = "#282828"
        self.width = 250
        self.left = 220
        self.top = 170
        self.expand = True
        self.datas_rapidas = identificar_datas()
        self.content = self.build()
        self.hora = self.build_hora()

    def update_text(self):
        due_date = self.controler.save.vencimento
        text_element = self.content.controls[0].content
        icon_element = self.content.controls[6]

        if due_date is None:
            text_element.value = None
            icon_element.visible = False
        else:
            with temp_locale("en_US.UTF-8"):
                formatted_date = due_date.strftime("%b %d %I:%M %p")

            formatted_date = formatted_date.replace(" 12:00 AM", "")

            text_element.value = formatted_date
            icon_element.visible = True

        self.update()

    def salvar_hora(self, e):
        valores = [
            self.hora.content.controls[i].controls[1].content.value for i in range(2)
        ]
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

        data = self.controler.save.data
        if not data:
            data = datetime.now()
        self.controler.save.vencimento = datetime.combine(data.date(), horario)
            
        self.controler.save.hora = horario
        self.controler.save.hora = horario
        self.controler.atualizar_lembretes()
        
        print(self.controler.save.hora)
        self.show_hora(e)
        self.update_text()

    def indentificar_datas_formatada(self, texto):
        def formatar_data(data):
            dia_semana = DIAS_SEMANA[data.weekday()]
            dia = f"{data.day:02d}"
            mes = MESES[data.month - 1]
            return f"{dia_semana} {dia} {mes}"

        data = self.datas_rapidas[texto]
        if texto != "Hoje" and texto != "Amanha":
            return formatar_data(data)
        else:
            return formatar_data(data).split()[0]

    def different_tomorrow(self, texto):
        match texto:
            case "Sem vencimento":
                return False
            case "Proxima semana":
                return self.datas_rapidas[texto] != self.datas_rapidas["Amanha"]
            case _:
                return True

    def opcoes_rapidas(self, texto, icone, cor, complemento=None):
        return Container(
            on_click=lambda _: self.calendario.salvar_data(self.datas_rapidas[texto]),
            padding=padding.only(left=18, right=18),
            ink=True,
            visible=self.different_tomorrow(texto),
            height=35,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        controls=[
                            Icon(icone, color=cor),
                            Text(
                                texto,
                                size=14,
                                weight="bold",
                                expand=True,
                                overflow=TextOverflow.ELLIPSIS,
                                max_lines=1,
                            ),
                        ],
                        expand=True,
                        spacing=10,
                    ),
                    Text(
                        complemento,
                        size=14,
                        weight="bold",
                        color=Colors.GREY_500,
                    ),
                ],
            ),
        )

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

    def build_hora(self):
        return Container(
            Column(
                [
                    self.build_hora_container(
                        "Hora", gerar_horarios_24h_15min_intervalo()
                    ),
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
                                on_click=self.show_hora,
                                bgcolor=self.bgcolor,
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
            ),
            visible=False,
            padding=padding.only(left=10, right=10, top=20, bottom=20),
            bgcolor=self.bgcolor,
            border=self.border,
            height=200,
            width=300,
            border_radius=10,
            left=self.left - 20,
            top=self.top + 310,
        )

    def show_hora(self, e):
        self.hora.visible = not self.hora.visible
        self.page.update()

    def build(self):
        return Column(
            [
                Container(
                    TextField(
                        hint_text="Digite um vencimento",
                        text_style=TextStyle(color=Colors.WHITE),
                        border=InputBorder.NONE,
                        hint_style=TextStyle(color=Colors.GREY_600),
                    ),
                    padding=padding.only(left=16),
                ),
                Divider(height=1),
                self.opcoes_rapidas(
                    "Hoje",
                    Icons.TODAY,
                    Colors.GREEN_400,
                    self.indentificar_datas_formatada("Hoje"),
                ),
                self.opcoes_rapidas(
                    "Amanha",
                    Icons.WB_SUNNY_OUTLINED,
                    Colors.AMBER_400,
                    self.indentificar_datas_formatada("Amanha"),
                ),
                self.opcoes_rapidas(
                    "Proxima semana",
                    Icons.NEXT_WEEK,
                    Colors.PURPLE_400,
                    self.indentificar_datas_formatada("Proxima semana"),
                ),
                self.opcoes_rapidas(
                    "Proximo fim de semana",
                    Icons.CHAIR,
                    Colors.BLUE_400,
                    self.indentificar_datas_formatada("Proximo fim de semana"),
                ),
                self.opcoes_rapidas(
                    "Sem vencimento",
                    Icons.BLOCK,
                    Colors.GREY_700,
                ),
                Divider(),
                self.calendario,
                Divider(height=1),
                Container(
                    Row(
                        [
                            Icon(Icons.ACCESS_TIME, color=Colors.GREY_400, size=18),
                            Text("Hora", color=Colors.GREY_400),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                    ),
                    margin=margin.only(top=15, bottom=15, left=5, right=5),
                    border_radius=5,
                    border=border.all(0.7, Colors.GREY_800),
                    height=35,
                    ink=True,
                    on_click=self.show_hora,
                    alignment=alignment.center,
                ),
            ],
            spacing=0,
        )
