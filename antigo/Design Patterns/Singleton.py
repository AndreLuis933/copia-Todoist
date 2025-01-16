import flet as ft

class AppState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "light"
            cls._instance.user = None
        return cls._instance

# Uso
def change_theme(page: ft.Page):
    state = AppState()
    state.theme = "dark" if state.theme == "light" else "light"
    page.theme_mode = state.theme
    page.update()

def main(page: ft.Page):
    state = AppState()
    page.theme_mode = state.theme
    page.add(ft.ElevatedButton("Mudar Tema", on_click=lambda _: change_theme(page)))

ft.app(target=main)