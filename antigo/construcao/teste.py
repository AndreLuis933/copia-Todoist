import flet as ft



def main(page: ft.Page):
    page.title = "Container com Botão"
 
    page.add(ft.Text("Clique fora para me fechar!", color=ft.Colors.WHITE))


ft.app(target=main)
