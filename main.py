import flet as ft
from ui.controller.app_controller import AppController


def main(page: ft.Page):
    page.title = "Todo App"
    page.window.always_on_top = True
    page.window.height = 900
    page.window.width = 550
    page.theme_mode = ft.ThemeMode.DARK

    AppController(page)
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)
