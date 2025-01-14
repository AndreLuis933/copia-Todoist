import flet as ft

def main(page: ft.Page):
    page.window_always_on_top = True
    # Função que será executada ao clicar no botão
    def adicionar_tarefa(e):
        print("Tarefa adicionada!")

    # Botão personalizado
    botao = ft.ElevatedButton(
        text="Adicionar tarefa",
        bgcolor=ft.colors.RED_900, 
        color=ft.colors.WHITE,  
        opacity=0.3,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8), 
        ),
    )

    # Adiciona o botão à página
    page.add(botao)

# Executa o app
ft.app(target=main)