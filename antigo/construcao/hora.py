import flet as ft

opcoes_dropdown_2 = ["5 minutos", "10 minutos", "15 minutos", "30 minutos", "1 hora"]

tab2 = ft.Tab(
    text="Antes da Tarefa",
    content=ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            padding=10,
                            border=ft.border.all(1, ft.colors.GREY_400),
                            border_radius=ft.border_radius.all(5),

                        ),
                        ft.Container(
                            content=ft.Dropdown(
                                icon=ft.icons.ACCESS_TIME_FILLED,
                                value=opcoes_dropdown_2[0],
                                options=[
                                    ft.dropdown.Option(texto) for texto in opcoes_dropdown_2
                                ],
                                width=300,
                            ),
                            padding=ft.padding.only(top=5),
                        ),
                    ],
                    spacing=0,
                ),
                width=300,
            ),
            ft.Text(
                "Defina uma notificação para um período antes da tarefa, como 5 ou 10 minutos.",
                size=14,
            ),
        ],
        spacing=20,
    ),
)