import flet as ft
from controller.app_controller import AppController


def main(page: ft.Page):

    AppController(page)


if __name__ == "__main__":
    ft.app(target=main)
