import flet as ft

def main(page: ft.Page):
    stack = ft.Stack([
        ft.Container(width=200, height=200, bgcolor=ft.colors.RED),
        ft.Container(width=100, height=100, bgcolor=ft.colors.BLUE),
    ])
    
    page.add(stack)

ft.app(target=main)