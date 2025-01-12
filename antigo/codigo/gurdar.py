import flet
from flet import *
from components.slidbar import Slidbar
from animations.animation import create_animate_slidbar
from controller.app_controller import AppController

def print_ui_structure(control, indent=0):
    def get_control_info(ctrl):
        name = type(ctrl).__name__
        details = []
        if hasattr(ctrl, "text") and ctrl.text:
            details.append(f"text='{ctrl.text}'")
        if hasattr(ctrl, "key") and ctrl.key:
            details.append(f"key='{ctrl.key}'")
        if hasattr(ctrl, "content"):
            details.append(f"has_content=True")
        if hasattr(ctrl, "controls"):
            details.append(f"controls_count={len(ctrl.controls)}")
        return f"{name} ({', '.join(details)})"

    print("  " * indent + get_control_info(control))

    if hasattr(control, "controls") and control.controls:
        for child in control.controls:
            print_ui_structure(child, indent + 1)
    elif hasattr(control, "content"):
        if isinstance(control.content, Control):
            print_ui_structure(control.content, indent + 1)
        elif isinstance(control.content, list):
            for child in control.content:
                print_ui_structure(child, indent + 1)


def main(page: Page):
    page.title = "Slidbar"
    page.window.always_on_top = True
    print(page.views)
    page.padding = 0
    page.spacing = 0

    page.vertical_alignment = alignment.top_left
    page.horizontal_alignment = alignment.center_left
    

    def encontrar(e):
        print(page.views)
        pass

    
    slidbar_container = Container(
        width=200,
        height=580,
        bgcolor="black",
        border_radius=10,
        animate=animation.Animation(500, "decelerate"),
        alignment=alignment.center,
        padding=10,
        content=Slidbar(create_animate_slidbar(page)),
    )
    main_layout = Row(
        controls=[
            slidbar_container,
            ElevatedButton(
                "Slidbar",
                bgcolor="white",
                on_click=encontrar,
            ),
        ],
    )
    

    page.add(main_layout)
    
    
if __name__ == "__main__":
    flet.app(target=main)