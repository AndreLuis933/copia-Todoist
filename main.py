import flet as ft
from ui.controller.app_controller import AppController


def main(page: ft.Page):

    AppController(page)
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)
