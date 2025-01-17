import flet as ft

def main(page: ft.Page):
    # Função chamada ao selecionar uma opção do dropdown
    def on_time_selected(e):
        time_input.value = e.control.value  # Atualiza o valor do campo de entrada
        dropdown.visible = False  # Esconde o dropdown
        page.update()

    # Função chamada ao clicar no campo de entrada
    def show_dropdown(e):
        dropdown.visible = True  # Exibe o dropdown
        page.update()

    # Campo de entrada para exibir o horário selecionado
    time_input = ft.TextField(
        hint_text="08:30 PM",
        width=200,
        on_focus=show_dropdown,  # Exibe o dropdown ao clicar no campo
        read_only=True,  # Impede a digitação direta
    )

    # Dropdown com horários disponíveis
    dropdown = ft.Column(
        [
            ft.TextButton("9:00 PM", on_click=on_time_selected),
            ft.TextButton("9:15 PM", on_click=on_time_selected),
            ft.TextButton("9:30 PM", on_click=on_time_selected),
            ft.TextButton("9:45 PM", on_click=on_time_selected),
            ft.TextButton("10:00 PM", on_click=on_time_selected),
            ft.TextButton("10:30 PM", on_click=on_time_selected),
            ft.TextButton("11:00 PM", on_click=on_time_selected),
        ],
        visible=False,  # Inicialmente oculto
        spacing=5,
        #border_radius=5,
        #bgcolor=ft.colors.SURFACE_VARIANT,
        #padding=10,
        width=200,
    )

    # Container para o campo de entrada e o dropdown
    time_picker_container = ft.Stack(
        [
            time_input,
            ft.Container(
                content=ft.Container(dropdown,bgcolor=ft.colors.SURFACE_VARIANT),
                margin=ft.margin.only(top=50),  # Posiciona o dropdown abaixo do campo
            ),
        ]
    )

    # Adiciona o componente na página
    page.add(
        ft.Column(
            [
                ft.Text("Selecione um horário:", size=20, weight="bold"),
                time_picker_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

# Inicializa o aplicativo
ft.app(target=main)