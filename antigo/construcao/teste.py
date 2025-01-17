import flet as ft
from flet import *


def main(page: ft.Page):

    page.window.width = 350
    page.window.height = 330
    page.window.always_on_top = True

    def show_dropdown(e):
        dropdown.visible = not dropdown.visible
        page.update()
        
    def HighLight(self, e):
        if e.data == "true":
            e.content.bgcolor = "white10"
            e.content.update()



    time_input = ft.TextField(
        hint_text="08:30 PM",
        width=200,
        on_focus=show_dropdown,  # Exibe o dropdown ao clicar no campo
        read_only=True,  # Impede a digitação direta
    )

    # Dropdown com horários disponíveis
    dropdown = ft.Container(
        content=ft.Container(
            ft.Column(
                [
                    Container(
                        content=ElevatedButton("9:00 PM", expand=True),
                        ink=True,
                        on_click=None,
                        padding=padding.symmetric(vertical=4, horizontal=10),
                        alignment=alignment.center_left,
                        on_hover=HighLight,
                    ),
                    ft.TextButton("9:15 PM",expand=True),
                    ft.TextButton("9:30 PM"),
                    ft.TextButton("9:45 PM"),
                    ft.TextButton("10:00 PM"),
                    ft.TextButton("10:30 PM"),
                    ft.TextButton("11:00 PM"),
                ],
                visible=True,
                spacing=5,
                width=200,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            bgcolor=ft.colors.SURFACE_VARIANT,
        ),
        margin=ft.margin.only(top=100, left=30),
        height=100,
    )

    tab1 = ft.Tab(
        text="Data & Hora",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [ft.Icon(ft.icons.ACCESS_TIME), time_input],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Text(
                        "Defina uma notificação para um horário específico (09h00) ou data e horário (seg 18h00).",
                        size=14,
                    ),
                    ft.ElevatedButton(
                        text="Adicionar lembrete",
                        bgcolor=ft.colors.RED,
                        color=ft.colors.WHITE,
                    ),
                ]
            )
        ),
    )
    tab2 = ft.Tab(
        text="Antes da Tarefa",
        content=ft.Column(
            [
                ft.Dropdown(
                    label="Antes da tarefa",
                    options=[
                        ft.dropdown.Option("5 minutos antes"),
                        ft.dropdown.Option("10 minutos antes"),
                        ft.dropdown.Option("30 minutos antes"),
                    ],
                    width=200,
                ),
                ft.Text(
                    "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                    size=14,
                ),
                ft.ElevatedButton(
                    text="Adicionar lembrete",
                    bgcolor=ft.colors.RED,
                    color=ft.colors.WHITE,
                ),
            ]
        ),
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            tab1,
            tab2,
        ],
        width=300,
        height=250,
    )
    container = ft.Container(
        content=tabs,
        bgcolor=ft.colors.GREY_900,
    )

    # Adiciona todos os elementos na página
    page.add(ft.Stack([container, dropdown]))


# Inicializa o aplicativo
ft.app(target=main)
