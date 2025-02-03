from flet import *
from functools import partial
from ..animations.slidbar.fechar_slidbar import create_animate_slidbar
from ..animations.slidbar.high_light_slidbar import HighLight
import flet


class Slidbar(Container):
    def __init__(self):
        super().__init__()
        self.func = create_animate_slidbar(self)
        self.HighLight = HighLight
        self.width = 220
        self.bgcolor = "#222222"
        # self.border_radius = 10
        self.animate = animation.Animation(500, "decelerate")
        self.alignment = alignment.top_left
        self.padding = 10
        self.content = self.build()

    def encontrar(self, e):
        print(self.content)
        pass

    def UserData(self, photo: str, name: str):
        return Row(
            controls=[
                Container(
                    Row(
                        [
                            Container(
                                width=42,
                                height=42,
                                alignment=alignment.center,
                                content=Image(src=photo, border_radius=20),
                            ),
                            Text(
                                value=name,
                                size=14,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,
                            ),
                            Container(
                                Image(
                                    src="down-arrow.png",
                                    width=13,
                                    height=13,
                                    color=Colors.WHITE,
                                ),
                                margin=margin.only(right=8),
                            ),
                        ],
                        spacing=5,
                    ),
                    ink=True,
                    on_click=lambda e: print("home"),
                ),
                Container(
                    Image(src="image.png", width=20, height=20, color=Colors.WHITE),
                    on_click=lambda e: print("home"),
                ),
                Container(
                    Image(src="screen.png", width=25, height=25, color=Colors.WHITE),
                    on_click=partial(self.func),
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=self.width - 20,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=lambda e: self.page.go("/s"),
            content=Row(
                controls=[
                    Container(
                        Icon(
                            name=icon_name,
                            size=20,
                            color="white54",
                        )if isinstance(icon_name, Icons) else Image(src=icon_name, width=18, height=18, color=Colors.WHITE54),
                        padding=padding.only(left=10),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        # weight="bold",
                        size=14,
                        opacity=1,
                        animate_opacity=200,
                    ),
                    Container(expand=True),
                    Container(
                        Text(
                            value="",
                            color=Colors.WHITE54,
                            opacity=0.6,
                        ),
                        padding=padding.only(right=10),
                    ),
                ]
            ),
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                horizontal_alignment="center",
                controls=[
                    self.UserData("perfil.jpg", "Andre"),
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon('search-interface-symbol.png', "Search"),
                    self.ContainedIcon('inbox.png', "Dashboard"),
                    self.ContainedIcon('calendar.png', "Revenue"),
                    self.ContainedIcon(Icons.NOTIFICATIONS, "Notifications"),
                    self.ContainedIcon('menu.png', "Analytics"),
                    Divider(height=10, color="transparent"),
                    self.ContainedIcon(Icons.LOGOUT_ROUNDED, "Logout"),
                ],
                spacing=0,
            ),
        )
