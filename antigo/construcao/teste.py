import flet as ft
from flet import *
from datetime import datetime, timedelta


def main(page: ft.Page):

    page.window.width = 350
    page.window.height = 430
    page.window.always_on_top = True

    def horarios_15_minutos():
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

    opcoes_dropdown_2 = [
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

    def show_dropdown(e):
        dropdown.visible = not dropdown.visible
        page.update()

    horarios = horarios_15_minutos()

    dropdown = ft.Container(
        ft.Column(
            [
                ft.ElevatedButton(
                    text,
                    width=240,
                    on_click=lambda e: print(e.control.text),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                )
                for text in horarios
            ],
            spacing=1,
            scroll=ft.ScrollMode.ALWAYS,
        ),
        bgcolor=ft.colors.SURFACE_VARIANT,
        visible=False,
        padding=1,
        margin=ft.margin.only(top=110, left=50),
        height=260,
        width=240,
    )

    tab1 = ft.Tab(
        text="Data & Hora",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.TextField(
                        icon=Icons.ACCESS_TIME,
                        value=horarios[0],
                        width=300,
                        on_focus=show_dropdown,
                    ),
                    ft.Text(
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

    tab2 = ft.Tab(
        text="Antes da Tarefa",
        content=ft.Column(
            [
                Container(
                    ft.Dropdown(
                        icon=Icons.ACCESS_TIME_FILLED,
                        value=opcoes_dropdown_2[0],
                        options=[
                            ft.dropdown.Option(texto) for texto in opcoes_dropdown_2
                        ],
                        width=300,
                        alignment = ft.alignment.center
                    ),
                ),
                ft.Text(
                    "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                    size=14,
                ),
            ]
        ),
    )

    tabs = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            tab1,
            tab2,
        ],
        width=300,
        height=190,
    )
    def envio(e):
        print(e.control.text)
    
    container = ft.Container(
        content=Column(
            [
                # ft.Column(
                #     [
                #         ft.ElevatedButton(
                #             text,
                #             width=240,
                #             on_click=lambda e: print(e.control.text),
                #             style=ft.ButtonStyle(
                #                 shape=ft.RoundedRectangleBorder(radius=0)
                #             ),
                #         )
                #         for text in horarios[0:3]
                #     ],
                #     spacing=1,
                # ),
                tabs,
                Row(
                    [
                        ElevatedButton(
                            text="Adicionar lembrete",
                            on_click=lambda e: envio(e),
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
        ),
        padding=10,
        bgcolor=ft.colors.GREY_900,
        width=300,
    )

    # Adiciona todos os elementos na página
    page.add(
        ft.Stack(
            [
                container,
                dropdown,
            ]
        )
    )


# Inicializa o aplicativo
ft.app(target=main)
