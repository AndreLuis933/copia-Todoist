from abc import ABC, abstractmethod
import flet as ft

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class AscendingSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data)

class DescendingSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data, reverse=True)

class DataList:
    def __init__(self, sort_strategy: SortStrategy):
        self._data = []
        self.sort_strategy = sort_strategy

    def add_item(self, item):
        self._data.append(item)

    def sort(self):
        self._data = self.sort_strategy.sort(self._data)

# Uso
def main(page: ft.Page):
    asc_list = DataList(AscendingSort())
    desc_list = DataList(DescendingSort())
    controle = DataList(DescendingSort())

    for item in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
        asc_list.add_item(item)
        desc_list.add_item(item)
        controle.add_item(item)

    asc_list.sort()
    desc_list.sort()

    page.add(
        ft.Text("Ascendente: " + str(asc_list._data)),
        ft.Text("Descendente: " + str(desc_list._data)),
        ft.Text("Controle: " + str(controle._data)),
        
    )

ft.app(target=main)