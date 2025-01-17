import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True 
    
    container1=ft.Container(
                width=300,
                height=300,
                bgcolor=ft.colors.RED,
                border_radius=10,
            )
    container2=ft.Container(
                width=250,
                height=250,
                bgcolor=ft.colors.GREEN,
                border_radius=10,
                left=25,
                top=25,
            )
    container3=ft.Container(
                width=200,
                height=200,
                bgcolor=ft.colors.BLUE,
                border_radius=10,
                left=50,
                top=50,
            )

    stack = ft.Stack(
        controls=[
            container1,
            container2,
            container3,
        ],
        width=page.window.width,
        height=page.window.height,
    )

    page.add(stack)

ft.app(target=main)