from flet import *
from ui.views.home_view import HomeView, Teste


class AppController:
    def __init__(self, page: Page):
        self.page = page
        self.loading_indicator = ProgressRing()
        self.initialize_routes()

    def initialize_routes(self):
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

    def route_change(self, route):
        self.page.views.clear()

        self.page.add(self.loading_indicator)

        # Configurações padrão que serão aplicadas em todas as views
        view_settings = {
            "padding": 0,
            "spacing": 0,
            "vertical_alignment": alignment.top_left,
            "horizontal_alignment": alignment.center_left,
        }

        routes = {
            "/": HomeView(self.page),
            "/s": Teste(self.page),
        }

        if route.route in routes:
            content = routes[self.page.route].build()

            # Se content já é uma View, usa suas configurações
            if isinstance(content, View):
                view = content
            else:
                # Cria nova View com as configurações
                view = View(route=self.page.route, controls=[content], **view_settings)

            self.page.views.append(view)

        self.page.remove(self.loading_indicator)
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
