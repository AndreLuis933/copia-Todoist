import config

import flet as ft
from ui.controller.app_controller import AppController
from ui.components.utils.locale_config import set_default_locale
from app.database.setup import ENGINE, Base, DB_PATH
import os
from flet import *
from utils.positioning import get_element_position


def database_exists():
    return os.path.exists(DB_PATH)

def create_tables():
    Base.metadata.create_all(ENGINE)
    print("Tabelas criadas.")


set_default_locale()

def total(control):
    total_height = getattr(control, 'height', 0)
    if total_height:
        return total_height
    return 0

def calculate_total_height(control, target_name=None):
    
    total_height = total(control)

    # Verifica se o controle atual é o que estamos buscando
    if control == 0:
        print('achou')
        return total_height

    # Recursivamente percorrer as estruturas de controle

    if hasattr(control, 'controls') and control.controls:
        if isinstance(control, Column):
            for child in control.controls:
                total_height += calculate_total_height(child, target_name)
    elif hasattr(control, 'content'):
        if isinstance(control.content, Control):
            total_height += calculate_total_height(control.content, target_name)

    return total_height

def total_controls_in_page(page):
    total = 1
    while True:
        controle = page.get_control(f"_{total}")
        if not controle:
            break
        total += 1
    return total
    


def main(page: ft.Page):
    page.title = "Todo App"
    page.window.always_on_top = True
    #page.window.min_width = 500
    page.window.height = 750
    page.window.width = 840
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#1e1e1e'
    #page.window.icon = "icon.png"

    controller = AppController(page)
    #page.go("/")
    controller.route_change("/")
    #print(total_controls_in_page(page))
    #print(calculate_total_height(page.views[0].controls[0].controls[1].controls[1], target_name=ControlerPrimeiraCamada().card_container))
    #element =page.views[0].controls[0].controls[1].controls[1].controls[1]
    #posicion = get_element_position(element)
    #page.views[0].controls[0].controls[2].top = posicion[0]
    #page.views[0].controls[0].controls[2].left =posicion[1]
    #print(element)
    #print(posicion)
    
    page.update()
        

if __name__ == "__main__":
    if not database_exists():
        create_tables()
    ft.app(target=main)
