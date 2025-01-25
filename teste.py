import flet as ft
from flet import *

class SmoothScrollList(ListView):
    def __init__(self, item_count):
        super().__init__()
        self.item_count = item_count
        self.controls = self.build()
        self.expand = True
        self.auto_scroll = False

    def build(self):
        items = [
            ft.Container(
                content=ft.Text(f"Item {i}"),
                padding=10,
                bgcolor=ft.colors.GREY,
                border_radius=5,
                margin=ft.margin.only(bottom=10),
            )
            for i in range(self.item_count)
        ]
        return items

def main(page: ft.Page):
    page.title = "Smooth Scroll Experience"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 800
    page.window.always_on_top = True

    smooth_list = SmoothScrollList(100)
    ListView()

    def smooth_scroll(e: ft.OnScrollEvent):
        if e.pixels is not None:
            smooth_list.scroll_to(
                offset=e.pixels,
                duration=50,  # Duração curta para responsividade
                curve=ft.AnimationCurve.EASE_OUT,
                #animate=True,
            )
        page.update()

    smooth_list.on_scroll = smooth_scroll
    #smooth_list.on_scroll_interval = 16  # Aproximadamente 60 FPS

    page.add(smooth_list)

ft.app(target=main)