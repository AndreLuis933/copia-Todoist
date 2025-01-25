from flet import *
from app.database.operations import listar_tarefas

class TodoApp(Column):
    def __init__(self):
        super().__init__()
        # self.width = 600
        self.scroll = ScrollMode.ALWAYS
        self.expand = True
        self.adicionar_tarefas()

    def adicionar_tarefas(self):
        self.controls.clear()
        for tarefa_id in listar_tarefas():
            _, *tarefa = tarefa_id
            tarefa = self.build_tarefa(*tarefa)
            self.controls.append(tarefa)
            self.controls.append(Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4))

    def create_conditional_component(self, condition, component):
        return component if condition else Container(visible=False)

    def create_icon_text_row(self, icon, text, condition):
        return self.create_conditional_component(
            condition,
            Container(
                Row(
                    [
                        Icon(name=icon, size=14, color=Colors.WHITE60),
                        Text(text, color=Colors.WHITE70, size=13),
                    ],
                    spacing=2,
                )
            ),
        )

    def build_tarefa(
        self,
        titulo,
        prioridade,
        descricao=None,
        vencimento=None,
        prazo=None,
        lembrete=None,
        local=None,
        tag=None,
    ):
        
        match prioridade:
            case 1:
                border_width = 2
                color=Colors.RED
            case 2:
                border_width = 1.7
                color=Colors.ORANGE
            case 3:
                border_width = 1.4
                color=Colors.BLUE
            case 4:
                border_width = 1
                color=Colors.GREY_500
        
        components = {
            "titulo": Text(
                titulo,
                color=Colors.WHITE,
            ),
            "descricao": self.create_conditional_component(
                descricao,
                Text(
                    descricao,
                    color=Colors.WHITE70,
                    size=13,
                    overflow=TextOverflow.ELLIPSIS,
                    max_lines=1,
                    width=(self.width - 50) if self.width else None,
                ),
            ),
            "vencimento": self.create_icon_text_row(
                Icons.CALENDAR_TODAY,
                vencimento,
                vencimento,
            ),
            "prazo": self.create_icon_text_row(
                Icons.ADJUST,
                prazo,
                prazo,
            ),
            "lembrete": self.create_conditional_component(
                lembrete,
                Container(
                    Icon(name=Icons.ALARM, size=14, color=Colors.WHITE60),
                ),
            ),
            "local": self.create_conditional_component(
                local,
                Container(
                    Icon(name=Icons.LOCATION_ON, size=14, color=Colors.WHITE60),
                ),
            ),
            "tag": self.create_icon_text_row(
                Icons.LABEL,
                tag,
                tag,
            ),
        }

        components["tag"].opacity = 0.5

        return Column(
            [
                Row(
                    [
                        Container(
                            width=20,
                            height=20,
                            border=border.all(border_width, color),
                            border_radius=20,
                            content=Row(
                                [
                                    Icon(
                                        name=Icons.CHECK,
                                        color=color,
                                        size=10,
                                        visible=False,
                                    )
                                ],
                                alignment=MainAxisAlignment.CENTER,
                                vertical_alignment=CrossAxisAlignment.CENTER,
                            ),
                            on_hover=self.hover_chekbox,
                        ),
                        Column(
                            [
                                components["titulo"],
                                components["descricao"],
                                Row(
                                    [
                                        components["vencimento"],
                                        components["prazo"],
                                        components["lembrete"],
                                        components["local"],
                                        components["tag"],
                                    ],
                                    spacing=10,
                                ),
                            ],
                            spacing=5,
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
        )

    def hover_chekbox(self, e):
        icon = e.control.content.controls[0]
        icon.visible = not icon.visible
        icon.update()

    def editar_clicked(self, e):
        tarefa = e.control.data
        edit_view = tarefa.controls[1]
        display_view = tarefa.controls[0]

        edit_view.controls[0].value = display_view.controls[1].controls[0].value
        display_view.visible = False
        edit_view.visible = True
        tarefa.update()

    def salvar_clicked(self, e):
        tarefa = e.control.data
        edit_view = tarefa.controls[1]
        display_view = tarefa.controls[0]

        display_view.controls[1].controls[0].value = edit_view.controls[0].value
        display_view.visible = True
        edit_view.visible = False
        tarefa.update()

    def tarefa_status_alterada(self, tarefa):
        # Implemente a lógica de alteração de status aqui
        self.update()

    def tarefa_excluida(self, tarefa):
        self.controls.remove(tarefa)
        self.update()
