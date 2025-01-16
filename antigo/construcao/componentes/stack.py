import flet as ft

def main(page: ft.Page):
    def toggle_container(e):
        container.visible = not container.visible
        alternative_content.visible = not container.visible
        page.update()

    container = ft.Container(
        content=ft.Text("Este é o conteúdo original"),
        width=200,
        height=100,
        bgcolor=ft.colors.BLUE,
        visible=False
    )

    alternative_content = ft.Container(
        content=ft.Text("Este é o conteúdo alternativo"),
        width=200,
        height=100,
        bgcolor=ft.colors.GREEN,
        visible=True
    )

    page.add(
        ft.ElevatedButton("Alternar visibilidade", on_click=toggle_container),
        container,
        alternative_content
    )

ft.app(target=main)