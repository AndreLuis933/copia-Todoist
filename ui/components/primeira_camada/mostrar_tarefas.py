from flet import *


class Tarefa(Column):
    def __init__(self, tarefa_nome, tarefa_status_alterada, tarefa_excluida):
        super().__init__()
        self.concluida = False
        self.tarefa_nome = tarefa_nome
        self.tarefa_status_alterada = tarefa_status_alterada
        self.tarefa_excluida = tarefa_excluida
        self.buton_color = Colors.LIGHT_BLUE
        self.controls = self.build()

    def build(self):
        return [
            Row(
                [
                    Container(
                        width=20,
                        height=20,
                        border=border.all(2, self.buton_color),
                        border_radius=20,
                        content=Row(
                            [
                                Icon(
                                    name=Icons.CHECK,
                                    color=self.buton_color,
                                    size=10,
                                    visible=False,
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                        ),
                        on_hover=self.hover_chekbox,
                        # on_click=toggle_selection,
                    ),
                    Column(
                        [
                            Text(self.tarefa_nome),
                            # Text(self.tarefa_nome),
                        ],
                    ),
                ],
                vertical_alignment=CrossAxisAlignment.START,
            ),
            Row(
                visible=False,
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[
                    TextField(expand=1),
                    IconButton(
                        icon=Icons.DONE_OUTLINE_OUTLINED,
                        icon_color=Colors.GREEN,
                        tooltip="Atualizar Tarefa",
                        on_click=self.salvar_clicked,
                    ),
                ],
            ),
        ]

    def hover_chekbox(self, e):
        icon = e.control.content.controls[0]
        if icon.visible:
            icon.visible = False
        else:
            icon.visible = True
        icon.update()

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


class TodoApp(Column):
    def __init__(self):
        super().__init__()
        self.adicionar_tarefas()

    def adicionar_tarefas(self):
        tarefas_padrao = [
            # "Comprar leite",
            # "Fazer exercícios",
            # "Ler um livro",
            # "Ligar para o médico",
        ]
        for tarefa_nome in tarefas_padrao:
            tarefa = Tarefa(
                tarefa_nome, self.tarefa_status_alterada, self.tarefa_excluida
            )
            self.controls.append(tarefa)
            self.controls.append(Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4))

    def tarefa_status_alterada(self, tarefa):
        self.update()

    def tarefa_excluida(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.update()
