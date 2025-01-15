import flet as ft

def main(page: ft.Page):
    def on_item_selected(e):
        print(f"Selecionado: {e.control.content.value}")

    popup_button = ft.PopupMenuButton(
        content=ft.Text("Abrir Opções"),
        items=[
            ft.PopupMenuItem(text="Opção 1", on_click=on_item_selected),
            ft.PopupMenuItem(text="Opção 2", on_click=on_item_selected),
            ft.PopupMenuItem(text="Opção 3", on_click=on_item_selected),
        ],
        on_cancel=lambda _: print("Menu cancelado"),
        #on_dismiss=lambda _: print("Menu fechado"),
    )

    page.add(popup_button)

ft.app(target=main)