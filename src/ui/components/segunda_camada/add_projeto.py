from flet import *
from ..animations.high_light import high_light


class AddProjeto(Container):
    def __init__(self, segunda_camada):
        super().__init__()
        self.visible = False
        self.controler = segunda_camada
        self.width = 480
        self.height = 565
        self.left = 160
        self.top = 40
        self.padding = padding.only(left=15, right=15, bottom=10, top=15)
        self.bgcolor = "#1E1E1E"
        self.colors_dict = {
            "#E91E63": "Cereja",
            "#FB0202": "Vermelho",
            "#FF9800": "Laranja",
            "#FFC107": "Amarelo",
            "#C0CA33": "Verde oliva",
            "#CDDC39": "Verde limão",
            "#4CAF50": "Verde",
            "#009688": "Verde Menta",
            "#00796B": "Azul petróleo",
            "#03A9F4": "Azul celeste",
            "#ADD8E6": "Azul Claro",
            "#0000FF": "Azul",
            "#6A0DAD": "Uva",
            "#8A2BE2": "Violeta",
            "#E6E6FA": "Lavanda",
            "#FF00FF": "Magenta",
            "#FF8C69": "Salmão",
            "#2F2F2F": "Carvão",
            "#808080": "Cinza",
            "#D2B48C": "Taupe",
        }
        self.border_radius = 15
        self.chose_color = "#2F2F2F"
        self.visualizar = "Lista"
        self.content = self.build()

    def toggle_opacity(self):
        for control in self.controler.primeira_camada.controls:
            control.opacity = 0.35
            control.update()

    def title(self, nome, padding_top):
        return Container(
            Text(nome, size=14, weight="bold"),
            padding=padding.only(top=padding_top, bottom=5),
        )

    def update_color(self):
        self.content.controls[5].content.controls[0].bgcolor = self.chose_color
        self.content.controls[5].content.controls[1].value = self.colors_dict[
            self.chose_color
        ]
        self.update()

    def update_visualizar_defout(self):
        for control in self.content.controls[10].content.controls:
            control.bgcolor = "transparent"
            control.content.controls[0].color = Colors.WHITE54
            control.content.controls[1].color = Colors.WHITE54

        for control in self.content.controls[10].content.controls:
            if self.visualizar in control.content.controls[1].value:
                control.bgcolor = "#202020"
                control.content.controls[0].color = Colors.WHITE
                control.content.controls[1].color = Colors.WHITE
                break

    def update_visualizar(self, e):
        for control in self.content.controls[10].content.controls:
            control.bgcolor = "transparent"
            control.content.controls[0].color = Colors.WHITE54
            control.content.controls[1].color = Colors.WHITE54

        e.control.bgcolor = "#202020"
        e.control.content.controls[0].color = Colors.WHITE
        e.control.content.controls[1].color = Colors.WHITE
        self.visualizar = e.control.content.controls[1].value
        self.update()

    def check_hover(self, e):
        if not self.visualizar in e.control.content.controls[1].value:
            high_light(e, "transparent", "#383838")

    def tabs_custon(self, name, icon, start=False):
        color = Colors.WHITE if start else Colors.WHITE54
        return Container(
            Column(
                [
                    Image(src=icon, height=20, width=20, color=color),
                    Text(name, size=13, color=color),
                ],
                spacing=5,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor="#202020" if start else "transparent",
            on_hover=self.check_hover,
            width=(self.width - 30 - 6) / 3,
            height=55,
            border_radius=8,
            alignment=alignment.center,
            on_click=lambda e: self.update_visualizar(e),
        )

    def update_button_appearance_envio(self):
        botao = self.content.controls[-1].content.controls[-1]
        if self.ativor_envio:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True

    def ativar_envio(self, e):
        self.ativor_envio = len(e.data.strip()) > 0
        self.update_button_appearance_envio()
        self.update()

    def save(self, e):
        name_field = self.content.controls[3].content
        space_work_field = self.content.controls[7].content.controls[1]
        favorite_field = self.content.controls[8].content.controls[0]

        name = name_field.value.strip()
        space_work = space_work_field.value.strip()
        favorite = favorite_field.value

        self.controler.save.save_projetc(
            [
                name,
                self.chose_color,
                space_work,
                favorite,
                self.visualizar,
            ]
        )

        name_field.value = None
        favorite_field.value = False
        self.chose_color = "#2F2F2F"
        self.update_color()

        self.visualizar = "Lista"
        self.update_visualizar_defout()

        self.ativor_envio = False
        self.update_button_appearance_envio()
        
        self.controler.primeira_camada.slidbar.add_project()

        self.controler.default()

    def build(self):
        return Column(
            [
                Container(
                    Row(
                        [
                            Container(
                                Text(
                                    "Adicionar projeto",
                                    size=18,
                                    weight="w500",
                                    max_lines=1,
                                )
                            ),
                            Container(
                                Icon(
                                    name=Icons.HELP_OUTLINE,
                                    color=Colors.WHITE54,
                                    weight="w100",
                                    size=25,
                                ),
                                on_click=lambda _: self.toggle_opacity(),
                            ),
                            Container(expand=True),
                            Container(
                                Icon(
                                    name=Icons.CLOSE,
                                    color=Colors.WHITE70,
                                    weight="w100",
                                    size=25,
                                ),
                                on_click=lambda _: self.controler.default(),
                            ),
                        ]
                    ),
                    padding=padding.only(bottom=15),
                ),
                Divider(height=0.1, color=Colors.OUTLINE, opacity=0.1),
                self.title("Nome", 15),
                Container(
                    TextField(
                        border=1,
                        on_change=lambda e: self.ativar_envio(e),
                        autofocus=True,
                        border_color="#777777",
                        border_width=0.3,
                        focused_border_color="#d8d8d8",
                        focused_border_width=0.5,
                        cursor_color=Colors.WHITE,
                        cursor_width=1,
                        cursor_height=20,
                        content_padding=padding.only(left=10, right=10),
                        height=55,
                        max_length=120,
                        counter_text="{value_length}/{max_length}",
                        counter_style=TextStyle(
                            color=Colors.WHITE70, size=13, weight="w750"
                        ),
                    ),
                ),
                self.title("Cor", 10),
                Container(
                    Row(
                        [
                            Container(
                                bgcolor=self.chose_color,
                                width=12,
                                height=12,
                                border_radius=20,
                            ),
                            Text(self.colors_dict[self.chose_color]),
                            Container(expand=True),
                            Container(
                                Image(
                                    src=r"icons\down_arrow.png",
                                    width=13,
                                    height=13,
                                    color=Colors.WHITE,
                                    visible=True,
                                ),
                            ),
                        ]
                    ),
                    padding=padding.only(top=5, bottom=10, left=10, right=10),
                    on_click=self.controler.show_color_dropdown,
                    border=border.all(0.7, Colors.GREY_800),
                ),
                self.title("Espaço de trabalho", 15),
                Container(
                    Row(
                        [
                            Container(
                                Image(
                                    src="perfil.jpg",
                                    width=20,
                                    height=20,
                                    border_radius=5,
                                    fit="cover",
                                )
                            ),
                            Text(
                                "Meus projetos",
                                color=Colors.WHITE,
                                size=14,
                                weight="w400",
                            ),
                        ]
                    ),
                    padding=padding.only(top=5, bottom=5, left=5, right=10),
                    border=border.all(0.7, Colors.GREY_800),
                ),
                Container(
                    Row(
                        [
                            Switch(
                                value=False,
                                active_color="#de4c4a",
                                thumb_color=Colors.WHITE,
                                inactive_track_color="#555555",
                                height=25,
                                thumb_icon=Colors.GREEN,
                            ),
                            Text("Adicionar aos favoritos"),
                        ],
                        spacing=5,
                    ),
                    padding=padding.only(top=15, bottom=10),
                ),
                self.title("Visualizar", 22),
                Container(
                    Row(
                        [
                            self.tabs_custon("Lista", r"icons\list.png", True),
                            self.tabs_custon("Painel", r"icons\list_rotate.png"),
                            self.tabs_custon("Calendario", r"icons\calendar.png"),
                        ],
                        spacing=0,
                    ),
                    bgcolor="#333333",
                    border_radius=8,
                    padding=padding.only(top=3, bottom=3, left=3, right=3),
                ),
                Container(
                    Row(
                        [
                            Text(
                                "O layout é sincronizado entre equipes em projetos compartilhados.",
                                max_lines=1,
                                size=12,
                            ),
                            Container(
                                Text(
                                    "Saiba mais",
                                    max_lines=1,
                                    size=12,
                                    style=TextStyle(
                                        decoration=TextDecoration.UNDERLINE
                                    ),
                                    weight="w500",
                                ),
                                on_click=lambda _: None,
                            ),
                        ],
                        spacing=5,
                    ),
                    padding=padding.only(top=10, bottom=15),
                ),
                Divider(height=0.1, color=Colors.OUTLINE, opacity=0.1),
                Container(
                    Row(
                        [
                            ElevatedButton(
                                text="Cancelar",
                                on_click=self.controler.default,
                                bgcolor=Colors.GREY_800,
                                color=Colors.WHITE70,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=8),
                                ),
                            ),
                            ElevatedButton(
                                text="Adicionar",
                                on_click=self.save,
                                disabled=True,
                                bgcolor=Colors.RED_900,
                                color=Colors.WHITE,
                                opacity=0.3,
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=8),
                                ),
                            ),
                        ],
                        alignment=MainAxisAlignment.END,
                    ),
                    padding=padding.only(top=15),
                ),
            ],
            spacing=0,
        )
