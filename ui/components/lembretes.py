from flet import *
from datetime import datetime, timedelta


class Lembretes(Container):
    def __init__(self):
        super().__init__()
        self.visible = True
        self.padding = 10
        self.bgcolor = Colors.GREY_900
        self.width = 300
        self.height=270
        self.left = 470  
        self.top = 200
        self.border_radius = 10
        self.horarios = self.horarios_15_minutos()
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
        self.dropdown = self.dropdown_artificial()

    def show_card(self, e):
        self.visible = not self.visible
        self.update()

    def horarios_15_minutos(self):
        now = datetime.now()

        minutes_to_add = (15 - now.minute % 15) % 15
        if minutes_to_add == 0:
            minutes_to_add = 15

        current_time = now + timedelta(minutes=minutes_to_add)
        current_time = current_time.replace(second=0, microsecond=0)

        horarios = []

        end_time = now + timedelta(days=1)
        end_time = end_time.replace(
            hour=now.hour, minute=current_time.minute, second=0, microsecond=0
        )

        while current_time < end_time:
            horarios.append(current_time.strftime("%I:%M %p"))
            current_time += timedelta(minutes=15)

        return horarios

    def show_dropdown(self, e):
        self.dropdown.visible = not self.dropdown.visible
        self.dropdown.update()

    def envio(self, e):
        selecionada  =self.content.controls[0].selected_index
        tab = self.content.controls[0].tabs[selecionada]
        if selecionada == 0:
            print(tab.content.content.controls[0].value)
        else:
            print(tab.content.controls[0].content.value)

    def tab1(self):
        return Tab(
            text="Data & Hora",
            content=Container(
                content=Column(
                    [
                        TextField(
                            icon=Icons.ACCESS_TIME,
                            value=self.horarios[0],
                            width=300,
                            on_focus=self.show_dropdown,
                        ),
                        Text(
                            "Defina uma notificação para um horário específico (09h00) ou data e horário (seg 18h00).",
                            size=14,
                        ),
                    ]
                ),
                padding=10,
                border_radius=20,
                # alignment="center",
            ),
        )

    def tab2(self):
        return Tab(
            text="Antes da Tarefa",
            content=Column(
                [
                    Container(
                        Dropdown(
                            icon=Icons.ACCESS_TIME_FILLED,
                            value=self.opcoes_dropdown_2[0],
                            options=[
                                dropdown.Option(texto)
                                for texto in self.opcoes_dropdown_2
                            ],
                            width=300,
                            alignment=alignment.center,
                        ),
                    ),
                    Text(
                        "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                        size=14,
                    ),
                ]
            ),
        )

    def atualizar_tab1(self, e):
        selecionada  =self.content.controls[0].selected_index
        tab = self.content.controls[0].tabs[selecionada]
        if selecionada == 0:
            tab.content.content.controls[0].value = e.control.text
        self.update()

    def dropdown_artificial(self):
        return Container(
            Column(
                [
                    ElevatedButton(
                        text,
                        width=240,
                        on_click=lambda e: self.atualizar_tab1(e),
                        style=ButtonStyle(shape=RoundedRectangleBorder(radius=0)),
                    )
                    for text in self.horarios
                ],
                spacing=1,
                scroll=ScrollMode.ALWAYS,
            ),
            bgcolor=Colors.ON_SURFACE_VARIANT,
            visible=False,
            padding=1,
            margin=margin.only(top=110, left=50),
            height=260,
            width=240,
            left = self.left,
            top = self.top,
        )

    def build(self):
        return Column(
            [
                Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        self.tab1(),
                        self.tab2(),
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
            ]
        )


if __name__ == "__main__":

    def main(page: Page):

        page.window.height = 600
        page.window.width = 800
        page.window.always_on_top = True

        container = Lembretes()
        dropdown = container.dropdown

        page.add(
            Stack(
                [
                    container,
                    dropdown,
                ]
            )
        )

    app(target=main)
