import flet as ft


def main(page: ft.Page):
    page.title = "Container com Botão"
    page.bgcolor = ft.colors.BLACK

    def close_container(_):
        if container.visible:
            container.visible = False
            show_button.visible = True
            page.update()

    def show_container(_):
        container.visible = True
        show_button.visible = False
        page.update()

    container = ft.Container(
        content=ft.Text("Clique fora para me fechar!", color=ft.colors.WHITE),
        width=300,
        height=200,
        bgcolor=ft.colors.BLUE_500,
        border_radius=10,
        padding=20,
        visible=False,
    )

    show_button = ft.ElevatedButton("Mostrar Container", on_click=show_container)

    content = ft.Stack(
        [
            ft.GestureDetector(
                on_tap=close_container,
                content=ft.Container(expand=True, bgcolor=ft.colors.TRANSPARENT),
            ),
            ft.Column(
                [show_button, container],
            ),
        ],
        expand=True,
    )

    page.add(content)


ft.app(target=main)
