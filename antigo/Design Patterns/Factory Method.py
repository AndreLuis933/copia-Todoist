from abc import ABC, abstractmethod
import flet as ft

class Control(ABC):
    @abstractmethod
    def build(self) -> ft.Control:
        pass

class ButtonControl(Control):
    def build(self) -> ft.Control:
        return ft.ElevatedButton("Clique-me")

class TextFieldControl(Control):
    def build(self) -> ft.Control:
        return ft.TextField(hint_text="Digite algo")

class ControlFactory:
    @staticmethod
    def create_control(control_type: str) -> Control:
        if control_type == "button":
            return ButtonControl()
        elif control_type == "textfield":
            return TextFieldControl()
        else:
            raise ValueError("Tipo de controle desconhecido")

# Uso
def main(page: ft.Page):
    factory = ControlFactory()
    button = factory.create_control("button").build()
    textfield = factory.create_control("textfield").build()
    page.add(button, textfield)

ft.app(target=main)