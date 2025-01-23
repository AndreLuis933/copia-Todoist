import flet as ft
from ui.controller.app_controller import AppController
from ui.components.utils.locale_config import set_default_locale
from app.database.setup import ENGINE, Base
import os

def database_exists():
    return os.path.exists(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "TODO.db"
        )
    )


def create_tables():
    Base.metadata.create_all(ENGINE)


if not database_exists():
    print("Criando banco de dados...")
    create_tables()

set_default_locale()

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
