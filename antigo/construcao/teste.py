import flet as ft

def main(page: ft.Page):
    # Variável para controlar o estado atual (Data & Hora ou Antes da Tarefa)
    current_view = "date_time"

    # Função para alternar o conteúdo do container
    def switch_to_date_time(e):
        nonlocal current_view
        current_view = "date_time"
        update_content()

    def switch_to_before_task(e):
        nonlocal current_view
        current_view = "before_task"
        update_content()

    # Função para atualizar o conteúdo do container
    def update_content():
        if current_view == "date_time":
            container.content = ft.Column(
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
        elif current_view == "before_task":
            container.content = ft.Column(
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
            )
        page.update()

    # Container com tamanho fixo
    container = ft.Container(
        width=300,
        height=200,
        padding=15,
        bgcolor=ft.colors.SURFACE_VARIANT,
        border_radius=10,
    )

    # Inicializa o conteúdo do container
    update_content()

    # Botões de alternância
    toggle_buttons = ft.Row(
        [
            ft.TextButton(
                "Data & Hora",
                on_click=switch_to_date_time,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor=ft.colors.ON_SURFACE if current_view == "date_time" else ft.colors.SURFACE_VARIANT,
                    color=ft.colors.WHITE if current_view == "date_time" else ft.colors.ON_SURFACE,
                ),
            ),
            ft.TextButton(
                "Antes da tarefa",
                on_click=switch_to_before_task,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    bgcolor=ft.colors.ON_SURFACE if current_view == "before_task" else ft.colors.SURFACE_VARIANT,
                    color=ft.colors.WHITE if current_view == "before_task" else ft.colors.ON_SURFACE,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Adiciona todos os elementos na página
    page.add(
        ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.Icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.Icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        width=400,
        height=400,
    )
    )

# Inicializa o aplicativo
ft.app(target=main)