import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Icon(ft.icons.ADJUST),
            ft.Icon(ft.icons.ADJUST_SHARP),
            ft.Icon(ft.icons.ADJUST_ROUNDED),
            ft.Icon(ft.icons.ADJUST_OUTLINED),
        ])
    )

ft.app(target=main)
