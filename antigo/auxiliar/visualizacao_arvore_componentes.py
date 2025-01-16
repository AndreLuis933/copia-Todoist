from flet import *
import flet

def print_ui_structure(control, indent=0):
    def get_control_name(ctrl):
        name = type(ctrl).__name__
        if hasattr(ctrl, 'text') and ctrl.text:
            name += f" ('{ctrl.text}')"
        elif hasattr(ctrl, 'label') and ctrl.label:
            name += f" ('{ctrl.label}')"
        elif hasattr(ctrl, 'title') and ctrl.title:
            name += f" ('{ctrl.title}')"
        elif hasattr(ctrl, 'value') and ctrl.value:
            name += f" (value: {ctrl.value})"
        return name

    print("  " * indent + get_control_name(control))
    
    if hasattr(control, 'controls') and control.controls:
        for child in control.controls:
            print_ui_structure(child, indent + 1)
    elif hasattr(control, 'content'):
        if isinstance(control.content, Control):
            print_ui_structure(control.content, indent + 1)
        elif isinstance(control.content, list):
            for child in control.content:
                print_ui_structure(child, indent + 1)
    
    # Lidar com casos especiais
    if isinstance(control, (Tabs, NavigationRail)):
        for tab in control.tabs:
            print_ui_structure(tab, indent + 1)
    elif isinstance(control, DataTable):
        print("  " * (indent + 1) + f"Columns: {len(control.columns)}")
        print("  " * (indent + 1) + f"Rows: {len(control.rows)}")

def main(page: Page):
    main_container = Container(
        content=Column([
            Text("Título Principal", size=20),
            Row([
                ElevatedButton("Botão 1"),
                ElevatedButton("Botão 2")
            ]),
            Container(
                content=Text("Texto no Container"),
                bgcolor=colors.BLUE_100,
                padding=10
            )
        ]),
        padding=20,
        bgcolor=colors.GREEN_100
    )

    page.add(main_container)

    # Imprimir a estrutura da UI após adicionar à página
    print("Estrutura da UI:")
    print_ui_structure(page)

flet.app(target=main)