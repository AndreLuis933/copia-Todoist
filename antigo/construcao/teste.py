import flet as ft

class Tarefa(ft.UserControl):
    def __init__(self, tarefa_nome, tarefa_status_alterada, tarefa_excluida):
        super().__init__()
        self.concluida = False
        self.tarefa_nome = tarefa_nome
        self.tarefa_status_alterada = tarefa_status_alterada
        self.tarefa_excluida = tarefa_excluida

    def build(self):
        self.display_tarefa = ft.Checkbox(
            value=False,
            label=self.tarefa_nome,
            on_change=self.status_alterado
        )
        self.edit_nome = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_tarefa,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar Tarefa",
                            on_click=self.editar_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Excluir Tarefa",
                            on_click=self.excluir_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_nome,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Atualizar Tarefa",
                    on_click=self.salvar_clicked,
                ),
            ],
        )
        return ft.Column(controls=[self.display_view, self.edit_view])

    def editar_clicked(self, e):
        self.edit_nome.value = self.display_tarefa.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def salvar_clicked(self, e):
        self.display_tarefa.label = self.edit_nome.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_alterado(self, e):
        self.concluida = self.display_tarefa.value
        self.tarefa_status_alterada(self)

    def excluir_clicked(self, e):
        self.tarefa_excluida(self)

class TodoApp(ft.UserControl):
    def build(self):
        self.nova_tarefa = ft.TextField(hint_text="Adicione uma tarefa", expand=True)
        self.tarefas = ft.Column()

        self.filtro = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="todas"), ft.Tab(text="ativas"), ft.Tab(text="concluídas")],
        )

        return ft.Column(
            width=600,
            controls=[
                ft.Row([ft.Text(value="Minhas Tarefas", style=ft.TextThemeStyle.HEADLINE_MEDIUM)]),
                ft.Row(
                    controls=[
                        self.nova_tarefa,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.adicionar_clicked),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filtro,
                        self.tarefas,
                    ],
                ),
            ],
        )

    def adicionar_clicked(self, e):
        if self.nova_tarefa.value:
            tarefa = Tarefa(self.nova_tarefa.value, self.tarefa_status_alterada, self.tarefa_excluida)
            self.tarefas.controls.append(tarefa)
            self.nova_tarefa.value = ""
            self.update()

    def tarefa_status_alterada(self, tarefa):
        self.update()

    def tarefa_excluida(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.update()

    def update(self):
        status = self.filtro.tabs[self.filtro.selected_index].text
        for tarefa in self.tarefas.controls:
            tarefa.visible = (
                status == "todas"
                or (status == "ativas" and not tarefa.concluida)
                or (status == "concluídas" and tarefa.concluida)
            )
        super().update()

    def tabs_changed(self, e):
        self.update()

def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed="green")
    page.update()

    todo = TodoApp()
    page.add(todo)

ft.app(target=main)