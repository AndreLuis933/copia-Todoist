import flet as ft
from flet import *


def main(page: ft.Page):

    highlighted_text = ft.Container(
        content=ft.Text(
            "Jan 27 1:30 PM",
            color="white",
            weight=ft.FontWeight.BOLD,
            size=14,
            opacity=1,
        ),
        bgcolor=ft.colors.RED_800,
        opacity=0.4,
        padding=ft.padding.only(left=5, right=10, top=0, bottom=2),
        alignment=ft.alignment.bottom_left,
        margin=margin.only(left=0, right=0, top=15, bottom=0),
        on_click=lambda _: None,
        height=35,
    )

    text_field = TextField(
        hint_text="Nome da tarefa",
        autofocus=True,
        border=InputBorder.NONE,
        height=30,
    )

    container = ft.Row(
        controls=[
            highlighted_text,
            text_field,
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.START,
        height=40,
    )

    page.add(container)


ft.app(target=main)
