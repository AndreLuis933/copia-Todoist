import flet as ft

def main(page: ft.Page):
    def on_item_selected(e):
        selected_item = e.control.data
        print(f"Selecionado: {selected_item}")

    def show_options(e):
        menu.visible = True
        #menu.open = True
        page.update()

    # Criando as opções do menu
    menu_items = [
        ft.PopupMenuItem(text="Opção 1", data="Opção 1"),
        ft.PopupMenuItem(text="Opção 2", data="Opção 2"),
        ft.PopupMenuItem(text="Opção 3", data="Opção 3"),
    ]

    for item in menu_items:
        item.on_click = on_item_selected

    # Criando o menu
    menu = ft.PopupMenuButton(
        items=menu_items,
        visible=False  # O menu em si fica invisível
    )

    # Seu botão existente
    your_button = ft.ElevatedButton("Seu Botão Existente", on_click=show_options)

    # Adicionando o botão e o menu à página
    page.add(your_button, menu)

ft.app(target=main)