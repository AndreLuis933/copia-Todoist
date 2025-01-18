from abc import ABC, abstractmethod
import flet as ft

class UIComponent(ABC):
    @abstractmethod
    def render(self) -> ft.Control:
        pass

class Button(UIComponent):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> ft.Control:
        return ft.ElevatedButton(self.text)

class TextField(UIComponent):
    def __init__(self, hint: str):
        self.hint = hint

    def render(self) -> ft.Control:
        return ft.TextField(hint_text=self.hint)

class Container(UIComponent):
    def __init__(self):
        self.children = []

    def add(self, component: UIComponent):
        self.children.append(component)

    def render(self) -> ft.Control:
        return ft.Column([child.render() for child in self.children])

# Uso
def main(page: ft.Page):
    form = Container()
    form.add(TextField("Nome"))
    form.add(TextField("Email"))
    form.add(Button("Enviar"))

    page.add(form.render())
    
    
ft.app(target=main)