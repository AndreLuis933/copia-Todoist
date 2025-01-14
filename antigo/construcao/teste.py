import flet as ft

def main(page: ft.Page):
    page.window_always_on_top = True
    # Função que será executada ao clicar no botão
    def adicionar_tarefa(e):
        print("Tarefa adicionada!")

    # Botão personalizado
    botao = ft.ElevatedButton(
        text="Adicionar tarefa",
        bgcolor=ft.colors.RED_900,  # Cor de fundo
        color=ft.colors.WHITE,  # Cor do texto
        on_click=adicionar_tarefa,  # Função chamada ao clicar
        opacity=0.3,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),  # Bordas arredondadas
            #padding=ft.EdgeInsets.all(10),  # Espaçamento interno
        ),
    )

    # Adiciona o botão à página
    page.add(botao)

# Executa o app
ft.app(target=main)