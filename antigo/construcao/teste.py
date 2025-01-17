import flet as ft



def main(page: ft.Page):
    page.window.always_on_top = True
    buton_color = ft.colors.RED

    def toggle_selection(e):
        icon = e.control.content.controls[0]
        if icon.visible:
            icon.visible = False
        else:
            icon.visible = True
        icon.update()

    circle = ft.Container(
        width=30,
        height=30,
        border=ft.border.all(3, buton_color),
        border_radius=20,
        content=ft.Row(
            [
                ft.Icon(
                    name=ft.icons.CHECK,
                    color=buton_color,
                    size=20,
                    visible=False,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_hover=toggle_selection,
        #on_click=toggle_selection,
    )


    page.add(
        ft.Row(
            [
                circle,
                ft.Text("Custom Checkbox", color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(target=main)
