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
        svg_content = """
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 30 30" style="enable-background:new 0 0 30 30;" xml:space="preserve">
<g>
	<path d="M14.43339,18.88085c2.15923,0,3.91203-1.7476,3.91203-3.91226c0-2.15805-1.7528-3.90566-3.91723-3.90566
		c-0.74107,0-1.43221,0.21538-2.02332,0.57576c0.18598-0.05526,0.37562-0.09493,0.58084-0.09493
		c1.09756,0,1.98365,0.88609,1.98365,1.98235c0,1.09248-0.88608,1.98376-1.98365,1.98376
		c-1.09627,0-1.98235-0.88608-1.98235-1.98376c0-0.20499,0.03979-0.39486,0.09493-0.58096
		c-0.36027,0.59135-0.57576,1.28236-0.57576,2.02344C10.52254,17.13325,12.27026,18.88085,14.43339,18.88085z"/>
	<path d="M24.55235,1.00006H5.44812C2.99534,1.00006,1,2.99563,1,5.44747v19.10459c0,2.45278,1.99533,4.44788,4.44812,4.44788
		h19.10423c2.45243,0,4.44765-1.9951,4.44765-4.44788V5.44747C29,2.99563,27.00479,1.00006,24.55235,1.00006z M27.32951,24.55206
		c0,1.53175-1.246,2.77774-2.77715,2.77774H5.44812c-1.53151,0-2.77751-1.246-2.77751-2.77774v-8.83719h4.08065
		c0.37644,3.90943,3.67563,6.97482,7.67705,6.97482c4.00709,0,7.3065-3.06539,7.68295-6.97482h5.21824V24.55206z M8.36366,14.96859
		c0-3.34831,2.7161-6.06418,6.06453-6.06418c3.35469,0,6.07079,2.71587,6.07079,6.06418c0,3.35492-2.7161,6.07079-6.07079,6.07079
		C11.07977,21.03938,8.36366,18.32351,8.36366,14.96859z M27.32951,13.75472h-5.28579
		c-0.58568-3.67705-3.77116-6.5006-7.61541-6.5006c-3.83882,0-7.02383,2.82356-7.60951,6.5006H2.67061V5.44747
		c0-1.53128,1.246-2.7768,2.77751-2.7768h19.10423c1.53116,0,2.77715,1.24552,2.77715,2.7768V13.75472z"/>
	<path d="M24.06196,5.11637h-1.75185c-0.48236,0-0.87593,0.39345-0.87593,0.87569v1.75186
		c0,0.48225,0.39356,0.87616,0.87593,0.87616h1.75186c0.47776,0,0.87038-0.39392,0.87038-0.87616V5.99205
		C24.93234,5.50982,24.53972,5.11637,24.06196,5.11637z"/>
</g>
</svg>"""
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
                        Image(src=svg_content,width=20, height=20, color="blue"),
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
            key="main_slidbar",
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                key="icons_texto",
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
