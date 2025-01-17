import flet as ft


def main(page: ft.Page):

    page.window.width = 600
    page.window.height = 600
    page.window.always_on_top = True

    tab1 = ft.Tab(
        text="Data & Hora",
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.ACCESS_TIME),
                            ft.TextField(
                                hint_text="08:30 PM",
                                width=200,
                            ),
                        ],
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
        width=400,
        height=400,
    )
    container = ft.Container(
        content=tabs,
        width=400,
        height=400,
        bgcolor=ft.colors.GREY_900,
    )

    # Adiciona todos os elementos na página
    page.add(container)


# Inicializa o aplicativo
ft.app(target=main)
