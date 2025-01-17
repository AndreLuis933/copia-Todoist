import flet as ft
from flet import *


def main(page: ft.Page):
    page.window.always_on_top = True
    page.window.height = 600
    page.window.width = 800

    def hide_all(e):
        layer2_container.visible = False
        dropdown.visible = False
        page.update()

    def on_layer2_tap(e):
        # Verifica se o clique foi dentro de algum componente específico
        if not click_inside_components(e):
            dropdown.visible = False
            page.update()
        e.stop_propagation()

    def click_inside_components(e):
        # Implemente a lógica para verificar se o clique foi dentro de algum componente
        # Retorne True se o clique foi dentro, False caso contrário
        return False  # Placeholder

    def show_layer2(e):
        layer2_container.visible = True
        page.update()

    # Componentes da primeira camada
    slidbar = ft.Container(width=200, height=600, bgcolor=ft.colors.BLUE_100)
    button = ft.ElevatedButton("Abrir Layer 2", on_click=show_layer2)
    todo_app = ft.Container(height=300, bgcolor=ft.colors.GREEN_100)

    # Componentes da segunda camada
    prioridade = ft.Container(width=100, height=100, bgcolor=ft.colors.RED_100)
    tarefa = ft.Container(width=100, height=100, bgcolor=ft.colors.YELLOW_100)
    lembretes = ft.Container(width=100, height=100, bgcolor=ft.colors.PURPLE_100)

    # Container para a segunda camada
    layer2_container = ft.Container(
        content=ft.Stack([prioridade, tarefa, lembretes]),
        visible=False,
        expand=True,
    )

    # GestureDetector para a segunda camada
    layer2_gesture = ft.GestureDetector(content=layer2_container, on_tap=on_layer2_tap)

    # Componente da terceira camada
    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Opção 1"),
            ft.dropdown.Option("Opção 2"),
        ],
        visible=False,
    )

    # Estrutura principal
    main_stack = ft.Stack(
        [
            # Primeira camada
            GestureDetector(
                on_tap=lambda e: print(e),
                content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
            ),
            ft.Row(
                expand=True,
                alignment=ft.alignment.top_left,
                controls=[
                    slidbar,
                    ft.Column(
                        controls=[
                            ft.Text("Entrada", size=20, weight="bold"),
                            ft.Divider(height=2, opacity=0),
                            button,
                            ft.Divider(
                                height=0.3, color=ft.colors.OUTLINE, opacity=0.4
                            ),
                            todo_app,
                        ],
                        expand=True,
                    ),
                ],
            ),
            # Segunda camada
            # layer2_gesture,
            # Terceira camada
            dropdown,
        ]
    )

    page.add(main_stack)


ft.app(target=main)
