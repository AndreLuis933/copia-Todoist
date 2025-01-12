import flet as ft

class SharedData:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

class ComponentA(ft.UserControl):
    def __init__(self, shared_data):
        super().__init__()
        self.shared_data = shared_data

    def build(self):
        return ft.ElevatedButton(f"A: {self.shared_data.count}", on_click=self.increment)

    def increment(self, e):
        self.shared_data.increment()
        self.update()

class ComponentB(ft.UserControl):
    def __init__(self, shared_data):
        super().__init__()
        self.shared_data = shared_data

    def build(self):
        return ft.Text(f"B: {self.shared_data.count}")

def main(page: ft.Page):
    # Criação da instância única
    shared_data = SharedData()

    # Criação dos componentes, passando a instância compartilhada
    comp_a = ComponentA(shared_data)
    comp_b = ComponentB(shared_data)

    # Adição dos componentes à página
    page.add(comp_a, comp_b)

    # Função para atualizar ComponentB
    def update_b():
        comp_b.update()

    # Configuração do timer para atualizar B periodicamente
    #page.on_interval(1, update_b)

ft.app(target=main)
