from datetime import datetime, timedelta
from flet import *

from ui.components.utils.locale_config import temp_locale
from ..utils.indentificar_datas import (
    identificar_datas,
    DIAS_SEMANA,
    DIAS_SEMANA_COMPLETOS,
    MESES,
)
from ..utils.formatad_data import formatad_data
from ..utils.days_of_week import dia_da_semana_e_cor
from ..utils.card_manager import CardManager

class Tarefa_vencimento(Container):
    def __init__(self, controler, calendario):
        super().__init__()
        self.controler = controler
        self.calendario = calendario
        self.visible = False
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

    def update_text(self):
        card = CardManager.get_current_card()
        due_date = self.controler.save.vencimento
        text_element = self.content.controls[0].content
        icon_element = self.content.controls[6]

        if due_date is None:
            card.adicionar_prefixo(0, None)
            card.atualizar_definitions(0, "Vencimento")
            text_element.value = None
            icon_element.visible = False
        else:

            data, formatted_date, color = dia_da_semana_e_cor(due_date)

            text_element.value = data
            icon_element.visible = True
            card.adicionar_prefixo(0, data, self.calendario.salvar_data)

            card.atualizar_definitions(
                0, formatted_date, color, self.calendario.salvar_data, color
            )

        self.update()

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
        if texto == "Sem vencimento":
            return False
        elif texto == "Proxima semana":
            return self.datas_rapidas[texto] != self.datas_rapidas["Amanha"]
        else:
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
                    on_click=self.controler.show_tarefa_hora,
                    alignment=alignment.center,
                ),
            ],
            spacing=0,
        )
