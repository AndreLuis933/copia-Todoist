import flet as ft

def main(page: ft.Page):
    def on_item_selected(e):
        selected_item = e.control.data
        print(f"Selecionado: {selected_item}")

    def show_options(e):
        # Posiciona o menu próximo ao botão
        menu.offset = ft.Offset(0, your_button.height)
        menu.show_menu(e)
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
    )

    # Seu botão existente
    your_button = ft.ElevatedButton("Seu Botão Existente", on_click=show_options)

    # Container para organizar os elementos
    container = ft.Container(
        content=ft.Column([
            your_button,
            menu
        ])
    )

    # Adicionando o container à página
    page.add(container)

ft.app(target=main)