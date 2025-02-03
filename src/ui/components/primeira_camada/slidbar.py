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

    def UserData(self, initials: str, name: str, descripion: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        alignment=alignment.center,
                        content=Image(src="unnamed.jpg", border_radius=20),
                    ),
                    Text(
                        value=name,
                        size=14,
                        weight="bold",
                        opacity=1,
                        animate_opacity=200,
                    ),
                    Container(
                        Icon(
                            name=Icons.NOTIFICATIONS_NONE,
                        )
                    ),
                    Container(
                        Image(src='home.svg',width=20, height=20, color="blue"),
                        on_click=lambda e: print('home'),
                    ),
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        on_click=lambda _: self.page.go("/s"),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
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
                    self.UserData("LI", "Andre", "Software Engineer"),
                    Container(
                        width=24,
                        height=24,
                        bgcolor="bluegrey800",
                        border_radius=8,
                        on_click=partial(self.func),
                    ),
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon(Icons.SEARCH, "Search"),
                    self.ContainedIcon(Icons.DASHBOARD_ROUNDED, "Dashboard"),
                    self.ContainedIcon(Icons.BAR_CHART, "Revenue"),
                    self.ContainedIcon(Icons.NOTIFICATIONS, "Notifications"),
                    self.ContainedIcon(Icons.PIE_CHART_ROUNDED, "Analytics"),
                    self.ContainedIcon(Icons.FAVORITE_ROUNDED, "Likes"),
                    self.ContainedIcon(Icons.WALLET_ROUNDED, "Wallet"),
                    Divider(height=5, color="wite24"),
                    self.ContainedIcon(Icons.LOGOUT_ROUNDED, "Logout"),
                    ElevatedButton(
                        "Encontrar",
                        on_click=self.encontrar,
                    ),
                ],
            ),
        )
