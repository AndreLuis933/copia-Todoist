import flet as ft
from flet import *

def main(page: ft.Page):
    page.window.always_on_top = True 
    
    def on_container_tap(e):
        if e.control == container3:
            print("Clicado na camada 3")
        elif e.control == container2:
            print("Clicado na camada 2")
        elif e.control == container1:
            print("Clicado na camada 1")

    def on_background_tap(e):
        print("Clicado na camada 0 (fundo)")

    container1 = ft.Container(
        width=300,
        height=300,
        bgcolor=ft.colors.RED,
        border_radius=10,
        on_click=on_container_tap
    )
    container2 = ft.Container(
        width=250,
        height=250,
        bgcolor=ft.colors.GREEN,
        border_radius=10,
        left=25,
        top=25,
        on_click=on_container_tap
    )
    container3 = ft.Container(
        width=200,
        height=200,
        bgcolor=ft.colors.BLUE,
        border_radius=10,
        left=50,
        top=50,
        on_click=on_container_tap
    )

    stack = ft.Stack(
        controls=[
            GestureDetector(
                on_tap=on_background_tap,
                content=Container(expand=True, bgcolor=Colors.TRANSPARENT),
            ),
            container1,
            container2,
            container3,
        ],
        width=page.window.width,
        height=page.window.height,
    )

    page.add(stack)

ft.app(target=main)