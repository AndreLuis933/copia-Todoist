import flet as ft
from flet import *


def main(page: ft.Page):
    page.window.always_on_top = True

    def on_tap(layer):
        print(f"Clicado na camada {layer}")

    container1 = ft.Container(
        width=300,
        height=300,
        bgcolor=ft.colors.RED,
        border_radius=10,
    )
    container2 = ft.Stack(
        [
            ft.Container(
                width=250,
                height=250,
                bgcolor=ft.colors.GREEN,
                border_radius=10,
                top=25,
                left=25,
            )
        ],
        width=250,
        height=250,
        top=25,
        left=25,
    )

    container3 = ft.Stack(
        [
            ft.Container(
                width=200,
                height=200,
                bgcolor=ft.colors.BLUE,
                border_radius=10,
                left=50,
                top=50,
            )
        ]
    )

    # Controles transparentes para detecção de clique
    detector0 = ft.GestureDetector(
        on_tap=lambda _: on_tap(0),
        content=ft.Container(expand=True, bgcolor=ft.colors.TRANSPARENT),
    )
    detector1 = ft.GestureDetector(
        on_tap=lambda _: on_tap(1),
        content=container1,
    )
    detector2 = ft.GestureDetector(
        on_tap=lambda _: on_tap(2),
        content=container2,
    )
    detector3 = ft.GestureDetector(
        on_tap=lambda _: on_tap(3),
        content=container3,
    )
    container2t = ft.Container(
        width=250,
        height=250,
        bgcolor=ft.colors.GREEN,
        border_radius=10,
    )
    container2t.top = 25
    container2t.left = 25

    stack = ft.Stack(
        controls=[
            detector0,  # Fundo
            container1,
            detector1,
            container2,
            detector2,
            container3,
            # detector3,
        ],
        width=page.window.width,
        height=page.window.height,
    )

    page.add(stack)


ft.app(target=main)
