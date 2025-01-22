from typing import List, Callable
import flet as ft

class Subject:
    def __init__(self):
        self._observers: List[Callable] = []

    def attach(self, observer: Callable):
        self._observers.append(observer)

    def detach(self, observer: Callable):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer()

class DataModel(Subject):
    def __init__(self):
        super().__init__()
        self._data = []

    def add_item(self, item):
        self._data.append(item)
        self.notify()

    @property
    def data(self):
        return self._data

class ListView(ft.UserControl):
    def __init__(self, model: DataModel):
        super().__init__()
        self.model = model
        self.model.attach(self.update_view)

    def build(self):
        self.list_view = ft.ListView()
        return self.list_view

    def update_view(self):
        self.list_view.controls = [ft.Text(item) for item in self.model.data]
        self.update()

# Uso
def main(page: ft.Page):
    model = DataModel()
    list_view = ListView(model)
    add_button = ft.ElevatedButton("Adicionar Item", on_click=lambda _: model.add_item("Novo Item"))
    page.add(list_view, add_button)
    
ft.app(target=main)