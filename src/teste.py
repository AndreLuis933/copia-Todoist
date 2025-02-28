import flet as ft
from flet import *

def get_childeren(element):
    childen = getattr(element, 'controls', None)
    if childen:
        return childen

    return getattr(element, 'content', None)

def is_row(element):
    return isinstance(element, Row)

def is_column(element):
    return isinstance(element, Column)

def is_container(element):
    return isinstance(element, Container)

def is_stack(element):
    return isinstance(element, Stack)

def have_height(element):
    return getattr(element, 'height', None)

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

def get_height_from_top(container, target_element):
    stack = container.page.controls[0]
    if not is_stack(stack):
        return
    primeira = stack.controls[0]
    if not have_height(primeira):  
        for element in get_childeren(primeira):
            pass



def total(control):
    total_height = getattr(control, 'height', 0)
    if total_height:
        return total_height
    return 0

def calculate_total_height(control, target_name=None):
    
    

    # Verifica se o controle atual é o que estamos buscando
    if control == target_name:
        return 0

    total_height = total(control)
    # Recursivamente percorrer as estruturas de controle

    if hasattr(control, 'controls') and control.controls:
        if isinstance(control, Column):
            for child in control.controls:
                total_height += calculate_total_height(child, target_name)
    elif hasattr(control, 'content'):
        if isinstance(control.content, Control):
            total_height += calculate_total_height(control.content, target_name)
    elif isinstance(control, Text):
        if control.size:
            total_height += control.size / 0.7
        else:
            total_height += 20

    return total_height


def get_parent(control):
    lista = []
    while not isinstance(control, View):
        control = control.parent
        lista.append(control)
    return lista
    

def main(page):
    page.padding = 0
    #page.window.always_on_top = True
    header = ft.Container(height=100, content=ft.Text("Header"))
    content = ft.Container(expand=True, content=ft.Text("Content"), margin=margin.only(top=10),bgcolor='white')
    footer = ft.Container(height=500, content=ft.Text("Footer"),bgcolor='blue')

    column = ft.Column(controls=[header, content, footer], spacing=5)
    sem = ft.Container(height=10, width=10, top=140, bgcolor=ft.Colors.RED)
    
    marcasao = ft.Container(
                    height=10,
                    width=10,
                    top=140,
                    bgcolor=ft.Colors.RED,
                )
    # Adicionar um Stack para verificar visualmente a altura calculada
    page.add(
        ft.Stack(
            [
                column,
                marcasao,
            ]
        )
    )
    #get_height_from_top(column, footer)
    total = calculate_total_height(page,footer)
    marcasao.top = total
    print(total)
    #print(get_parent(footer))
    page.update()


ft.app(target=main)
