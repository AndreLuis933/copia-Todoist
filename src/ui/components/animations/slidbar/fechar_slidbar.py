import time
from flet import *


class AnimateSlidbar:
    def __init__(self, slidbar):
        self.slidbar = slidbar
        self.slidbar_is_open = True
        self.my_projects_is_open = True
        self.favoritos_is_open = True

    def open_close_slidbar(self, e=None):
        total = self.slidbar.content.controls[0].controls[0].controls
        total.append(self.slidbar.content.controls[0].controls[-1])
        total.append(self.slidbar.content.controls[2])
        total.extend(self.slidbar.content.controls[1].controls)

        if self.slidbar_is_open:
            # Fechar a barra lateral
            self.toggle_opacity_slidbar(total, False)
            self.slidbar.bgcolor = Colors.TRANSPARENT
            time.sleep(0.2)
            self.slidbar.width = 50
        else:
            # Abrir a barra lateral
            self.slidbar.width = 220
            self.slidbar.bgcolor = "#222222"
            time.sleep(0.2)
            self.toggle_opacity_slidbar(total, True)

        self.toggle_opacity_my_projects(
            self.slidbar.content.controls[1].controls[10].content.controls, self.my_projects_is_open
        )
        self.toggle_opacity_my_projects(
            self.slidbar.content.controls[1].controls[7].content.controls, self.favoritos_is_open
        )

        self.slidbar_is_open = not self.slidbar_is_open
        if self.slidbar.page:
            self.slidbar.update()

    def close_projects(self, text):
        if "Meus projetos" in text:
            contole = 9
            is_open = self.my_projects_is_open
        else:
            contole = 6
            is_open = self.favoritos_is_open
        icon = self.slidbar.content.controls[1].controls[contole].content.controls[3].content
        projets = self.slidbar.content.controls[1].controls[contole + 1].content.controls
        if is_open:
            self.toggle_opacity_my_projects(projets, False)
            icon.src = r"icons\right_arrow.png"
        else:
            icon.src = r"icons\down_arrow.png"
            self.toggle_opacity_my_projects(projets, True)

        if "Meus projetos" in text:
            self.my_projects_is_open = not self.my_projects_is_open
        else:
            self.favoritos_is_open = not self.favoritos_is_open

        self.slidbar.update()

    def toggle_opacity_my_projects(self, controls, show):
        for item in controls:
            if isinstance(item, Container) and not item.content is None:
                item.visible = show

    def toggle_opacity_slidbar(self, controls, show):
        opacity = 1 if show else 0

        for item in controls:
            if isinstance(item, Container) and not item.content is None:
                if isinstance(item.content, Image):
                    if "screen" not in item.content.src:
                        item.opacity = opacity
                else:
                    item.opacity = opacity

            #item.update()

        #time.sleep(0.2)
        for item in controls:
            if isinstance(item, Container) and not item.content is None:
                if isinstance(item.content, Image):
                    if "screen" not in item.content.src:
                        item.visible = show
                else:
                    item.visible = show

