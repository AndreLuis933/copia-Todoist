"""Modifica a representaçao das clases que herdam do flet para facilitar o debug da aplicação."""
# import config_repr

import flet as ft

from app.database.setup import init_db
from ui.components.utils.locale_config import set_default_locale
from ui.controller.app_controller import AppController

set_default_locale()


def main(page: ft.Page):
    page.title = "Todo App"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e1e"

    # Opoços para facilitar o desenvolvimento
    # page.window.width = 840
    # page.window.height = 750
    # page.window.always_on_top = True

    controller = AppController(page)
    controller.route_change("/")

    page.update()


if __name__ == "__main__":
    init_db()
    ft.app(
        target=main,
        # configuraçoes para rodar em ambiente docker, para rodar local so comnetar essas linhas abaixo
        assets_dir="assets",
        view=None,
        port=8000,
        host="0.0.0.0",
    )
