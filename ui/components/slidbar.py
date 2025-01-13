from flet import *
from functools import partial
from ui.animations.animation import create_animate_slidbar


class Slidbar(Container):
    def __init__(self):
        super().__init__()
        self.func = create_animate_slidbar(self)
        self.width = 200
        self.bgcolor = "black"
        self.border_radius = 10
        self.animate = animation.Animation(500, "decelerate")
        self.alignment = alignment.top_left
        self.padding = 10
        self.content = self.build()
        
    def encontrar(self, e):
        print(self.content)
        pass

    def HighLight(self, e):
        if e.data == "true":
            e.control.bgcolor = "white10"
            e.control.update()

            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].color = "white"
            e.control.content.update()

        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.content.update()

    def UserData(self, initials: str, name: str, descripion: str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                        ),
                    ),
                    Column(
                        key="titulo_texto",
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,
                            ),
                            Text(
                                value=descripion,
                                size=9,
                                weight="w400",
                                color="white54",
                                opacity=1,
                                animate_opacity=200,
                            ),
                        ],
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
            key="main_slidbar",
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                key="icons_texto",
                horizontal_alignment="center",
                controls=[
                    self.UserData("LI", "Line Indent", "Software Engineer"),
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
