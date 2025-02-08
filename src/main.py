import flet as ft
from ui.controller.app_controller import AppController
from ui.components.utils.locale_config import set_default_locale
from app.database.setup import ENGINE, Base, DB_PATH
import os

def database_exists():
    return os.path.exists(DB_PATH)

def create_tables():
    Base.metadata.create_all(ENGINE)
    print("Tabelas criadas.")


set_default_locale()


def main(page: ft.Page):
    page.title = "Todo App"
    page.window.always_on_top = True
    #page.window.min_width = 500
    page.window.height = 450
    page.window.width = 440
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#1e1e1e'
    #page.window.icon = "icon.png"

    AppController(page)
    page.go("/")


if __name__ == "__main__":
    if not database_exists():
        create_tables()
    ft.app(target=main)
