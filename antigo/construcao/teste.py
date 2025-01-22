import flet as ft

class CustomDropdown(ft.UserControl):
    def __init__(self, options, width=200, height=30, item_height=30):
        super().__init__()
        self.options = options
        self.width = width
        self.height = height
        self.item_height = item_height
        self.selected_value = ft.Text(value=options[0], color=ft.colors.WHITE, size=15)
        self.is_open = False
        self.dropdown_content = None

    def build(self):
        self.dropdown_content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(option, color=ft.colors.WHITE, size=15),
                    width=self.width,
                    height=self.item_height,
                    on_click=lambda _, o=option: self.select_option(o),
                    bgcolor=ft.colors.GREY_900,
                )
                for option in self.options
            ],
            visible=False,
        )

        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        [self.selected_value, ft.Icon(ft.icons.ARROW_DROP_DOWN, color=ft.colors.WHITE)],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    width=self.width,
                    height=self.height,
                    bgcolor=ft.colors.GREY_900,
                    border_radius=5,
                    on_click=self.toggle_dropdown,
                ),
                self.dropdown_content,
            ],
        )

    def toggle_dropdown(self, e):
        self.is_open = not self.is_open
        self.dropdown_content.visible = self.is_open
        self.update()

    def select_option(self, option):
        self.selected_value.value = option
        self.toggle_dropdown(None)

def main(page: ft.Page):
    page.title = "Custom Dropdown Example"
    page.padding = 20
    page.bgcolor = ft.colors.GREY_800

    options = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
    dropdown = CustomDropdown(options, width=200, height=30, item_height=30)

    page.add(dropdown)

ft.app(target=main)