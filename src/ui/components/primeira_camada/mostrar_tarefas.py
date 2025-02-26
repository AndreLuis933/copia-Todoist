from flet import *
from app.database.operations import listar_tarefas, search_tarefa
from ..animations.high_light import high_light
from ..utils.days_of_week import dia_da_semana_e_cor
from .card_adicionar_tarefa import Card_adicionar_tarefa
import time


class TodoApp(Column):
    def __init__(self, controler):
        super().__init__()
        self.controler = controler
        self.scroll = ScrollMode.ALWAYS
        self.spacing = 10
        self.visible = True
        self.expand = True
        self.on_scroll = self.on_scrol
        self.position = {}
        self.atual = 0
        self.edit = False
        self.adicionar_tarefas()

    def on_scrol(self, e):
        self.atual = int(e.pixels)

    def adicionar_tarefas(self):
        self.controls.clear()
        for tarefa_id in listar_tarefas():
            id, titulo, prioridade, descricao, vencimento, prazo, local, tag = tarefa_id
            if vencimento:
                _, *vencimento = dia_da_semana_e_cor(vencimento)
            tarefa = self.build_tarefa(
                id, titulo, prioridade, descricao, vencimento, prazo, local, tag
            )
            self.controls.append(tarefa)
            self.controls.append(Divider(height=0.3, color=Colors.OUTLINE, opacity=0.4))

    def create_conditional_component(self, condition, component):
        return component if condition else Container(visible=False)

    def create_icon_text_row(
        self, icon, text, condition, cor=Colors.WHITE70, vencida=False
    ):
        return self.create_conditional_component(
            condition,
            Container(
                Row(
                    [
                        Icon(name=icon, size=14, color=cor),
                        Text(text, color=cor, size=13),
                        Icon(name=Icons.AUTORENEW, size=14, color=cor, visible=vencida),
                    ],
                    spacing=2,
                )
            ),
        )

    def build_tarefa(
        self,
        id,
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
                color = Colors.RED
            case 2:
                border_width = 1.7
                color = Colors.ORANGE
            case 3:
                border_width = 1.4
                color = Colors.BLUE
            case 4:
                border_width = 1
                color = Colors.GREY_500

        cor = Colors.WHITE70
        vencida = False
        if vencimento:
            cor = vencimento[1]
            vencimento = vencimento[0]
            if cor == "#ec6553":
                vencida = True

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
                Icons.CALENDAR_TODAY, vencimento, vencimento, cor, vencida
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

        spacin = self.spacing
        size_titulo = 20
        descrisao = 0
        adicional = 0

        if components["descricao"].visible:
            descrisao = 25
        list_componentes = list(components.values())[2:]
        for component in list_componentes:
            if component.visible:
                adicional = 25
                break

        if not adicional:
            size_titulo += 4
        posisao = size_titulo + descrisao + adicional + spacin + 10
        posisao += self.position.get(id - 1, 0)
        self.position[id] = posisao

        components["tag"].opacity = 0.5

        return Container(
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
                        margin=margin.only(right=10),
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
                    Container(expand=True),
                    self.icons_on_hover(Icons.EDIT, self.edit_task),
                    self.icons_on_hover(Icons.DASHBOARD),
                    self.icons_on_hover(Icons.CHAT_BUBBLE_OUTLINE),
                    self.icons_on_hover(Icons.MORE_HORIZ),
                    Container(width=10),
                ],
                spacing=0,
                vertical_alignment=CrossAxisAlignment.START,
            ),
            on_hover=self.show_more_options_task,
            data=id,
        )

    def edit_task(self, e):
        controle = e.control.parent.parent
        # posisao = self.position.get(controle.data - 1, 0)
        # ajuste = posisao - self.atual + 160
        # self.edit = True
        # self.page.views[0].controls[0].controls[2].top = ajuste

        controle.content = Card_adicionar_tarefa(
            self.controler, self.controler.hover_control, controle, self.voltar
        )
        self.controler.hover_control.card_edit()
        controle.content.carregar_tarefa()
        controle.page.update()

    def voltar(self, card, id):
        id, titulo, prioridade, descricao, vencimento, prazo, local, tag = (
            search_tarefa(id)
        )
        if vencimento:
            _, *vencimento = dia_da_semana_e_cor(vencimento)
        tarefa = self.build_tarefa(
            id, titulo, prioridade, descricao, vencimento, prazo, local, tag
        )
        card.content = tarefa

    def icons_on_hover(self, icon, func=None):
        return Container(
            Icon(icon, color=Colors.WHITE60),
            padding=padding.only(right=5),
            on_click=func,
            visible=False,
        )

    def show_more_options_task(self, e):
        if isinstance(e.control.content, Container):
            return
        if e.data == "true":
            visible = True
        else:
            visible = False
        for control in e.control.content.controls[-5:-1]:
            control.visible = visible
        e.control.update()

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
    # Magic methods    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}"