import flet as ft
from flet import *
from datetime import datetime, timedelta
import calendar


class Compartilhado:
    def __init__(self):
        self.button_hovered = False
        self.button = None
        self.card_container = None

    def toggle_card(self, e):
        self.button.visible = not self.button.visible
        self.card_container.visible = not self.card_container.visible
        # Reinicia o estado do hover
        self.button_hovered = False
        self.update_button_appearance()
        self.button.page.update()

    def mudar_cor(self, e):
        self.button_hovered = e.data == "true"
        self.update_button_appearance()
        self.button.page.update()

    def update_button_appearance(self):
        if self.button_hovered:
            self.button.content.controls[1].color = Colors.RED
            self.button.content.controls[0].controls[1].name = Icons.ADD_CIRCLE
            self.button.content.controls[0].controls[0].visible = True
        else:
            self.button.content.controls[1].color = Colors.WHITE
            self.button.content.controls[0].controls[1].name = Icons.ADD
            self.button.content.controls[0].controls[0].visible = False


class Button_adicionar_tarefa(Container):
    def __init__(self, compartilhado):
        super().__init__()
        self.compartilhado = compartilhado
        self.compartilhado.button = self
        self.visible = True
        self.button_height = 24
        self.on_click = self.compartilhado.toggle_card
        self.on_hover = self.compartilhado.mudar_cor
        self.padding = ft.padding.symmetric(horizontal=16, vertical=8)
        self.content = self.build()

    def build(self):
        return Row(
            tight=True,
            controls=[
                Stack(
                    [
                        Container(
                            visible=False,
                            bgcolor=ft.Colors.WHITE,
                            height=self.button_height / 2,
                            width=self.button_height / 2,
                            alignment=ft.alignment.center,
                        ),
                        ft.Icon(
                            name=ft.Icons.ADD,
                            color=ft.Colors.RED,
                            size=self.button_height,
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
                ft.Text(
                    "Adicionar tarefa",
                    color=ft.Colors.WHITE,
                    size=14,
                ),
            ],
            spacing=8,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )


class Card_adicionar_tarefa(Container):
    def __init__(self, compartilhado, tarefa_vencimento):
        super().__init__()
        self.visible = False
        self.compartilhado = compartilhado
        self.tarefa_vencimento = tarefa_vencimento
        self.compartilhado.card_container = self
        self.padding = ft.padding.all(16)
        self.border_radius = ft.border_radius.all(10)
        self.border = ft.border.all(0.3, Colors.OUTLINE)
        self.content = self.build()

    def on_vencimento_click(self, e):
        self.tarefa_vencimento.show_card(e)

    def build(self):
        return Column(
            controls=[
                ft.TextField(label="Nome da tarefa"),
                ft.TextField(label="Descrição", multiline=True),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(
                                        name=Icons.CALENDAR_TODAY,
                                        size=18,
                                        color=Colors.ON_SURFACE_VARIANT,
                                    ),
                                    ft.Text(
                                        "Vencimento",
                                        size=14,
                                        color=Colors.ON_SURFACE,
                                    ),
                                ],
                                spacing=4,
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            padding=ft.padding.symmetric(horizontal=12, vertical=6),
                            border_radius=ft.border_radius.all(5),
                            ink=True,
                            on_click=self.on_vencimento_click,
                            border=ft.border.all(0.3, Colors.OUTLINE),
                        ),
                        ft.ElevatedButton(
                            text="Prioridade",
                            icon=Icons.FLAG,
                        ),
                        ft.ElevatedButton(
                            text="Lembretes",
                            icon=Icons.NOTIFICATIONS,
                        ),
                        ft.IconButton(icon=Icons.MORE_VERT),
                    ],
                    spacing=8,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Cancelar",
                            on_click=self.compartilhado.toggle_card,
                            bgcolor=Colors.BLACK,
                            color=Colors.WHITE,
                        ),
                        ft.ElevatedButton(
                            text="Adicionar tarefa",
                            bgcolor=Colors.RED,
                            color=Colors.WHITE,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            spacing=12,
        )


class Calendario(Container):
    def __init__(self):
        super().__init__()
        self.current_date = datetime.now()
        self.months_loaded = 0
        self.is_loading = False
        self.tamanho = 20
        self.height = 205
        self.width = 250
        self.border = ft.border.all(1, ft.Colors.BLACK)
        self.border_radius = 10
        self.content = ListView(
            expand=True,
            on_scroll=self.on_scroll,
        )

    def create_month_calendar(self, year, month):
        calendar.setfirstweekday(6)
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]

        calendar_grid = ft.Column(spacing=5)

        header = ft.Row(
            [
                ft.Text(
                    f"{month_name} {year}",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#BB86FC",
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        calendar_grid.controls.append(header)

        days_of_week = ft.Row(
            [
                ft.Container(
                    content=ft.Text(day, size=14, color="#121212"),
                    width=self.tamanho,
                    height=self.tamanho,
                    bgcolor="#BB86FC",
                    border_radius=ft.border_radius.all(5),
                    alignment=ft.alignment.center,
                )
                for day in ["D", "S", "T", "Q", "Q", "S", "S"]
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        calendar_grid.controls.append(days_of_week)

        for week in cal:
            week_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
            for day in week:
                if day != 0:
                    week_row.controls.append(
                        ft.Container(
                            content=ft.Text(str(day), size=16, color="#E0E0E0"),
                            width=self.tamanho,
                            height=self.tamanho,
                            bgcolor="#1F1F1F",
                            border_radius=ft.border_radius.all(5),
                            alignment=ft.alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(
                        ft.Container(width=self.tamanho, height=self.tamanho)
                    )
            calendar_grid.controls.append(week_row)

        return ft.Container(
            content=calendar_grid,
            margin=ft.margin.only(bottom=20),
            # padding=20,
            bgcolor="#1E1E1E",
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.BLACK54,
                offset=ft.Offset(0, 0),
            ),
        )

    def load_more_months(self, count):
        new_months = []
        for _ in range(count):
            date = self.current_date + timedelta(days=30.44 * self.months_loaded)
            year, month = date.year, date.month
            month_calendar = self.create_month_calendar(year, month)
            new_months.append(month_calendar)
            self.months_loaded += 1
        self.content.controls.extend(new_months)

    def on_scroll(self, e: ft.OnScrollEvent):
        self.is_loading
        if not self.is_loading and e.pixels >= e.max_scroll_extent - 100:
            self.is_loading = True
            self.load_more_months(1)
            self.update()
            self.is_loading = False


class Tarefa_vencimento(Container):
    def __init__(self, calendario):
        super().__init__()
        self.calendario = calendario
        self.current_date = self.calendario.current_date
        self.padding = 15
        self.border_radius = 10
        self.shadow = BoxShadow(blur_radius=5)
        self.visible = False
        self.width = 250
        self.height = 700
        self.content = self.build()

    def show_card(self, e):
        self.visible = True
        self.update()

    def hide_card(self, e):
        self.visible = False
        self.update()

    def opcoes_rapidas(self, texto, icone, cor, complemento):
        return Container(
            bgcolor=Colors.GREY_900,
            on_click=lambda _: print(texto),
            padding=padding.all(10),
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        controls=[
                            Icon(icone, color=cor),
                            Text(
                                texto,
                                size=14,
                                weight="bold",
                                expand=True,
                                overflow=TextOverflow.ELLIPSIS,
                                max_lines=1,
                            ),
                        ],
                        expand=True,
                        spacing=10,
                    ),
                    Text(
                        complemento,
                        size=14,
                        weight="bold",
                        color=Colors.GREY_500,
                    ),
                ],
            ),
        )

    def build(self):
        return Column(
            [
                TextField(
                    hint_text="Digite um vencimento",
                ),
                Divider(),
                self.opcoes_rapidas("Hoje", Icons.TODAY, Colors.GREEN_400, "sab"),
                self.opcoes_rapidas(
                    "Amanha", Icons.WB_SUNNY_OUTLINED, Colors.AMBER_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proxima semana", Icons.NEXT_WEEK, Colors.PURPLE_400, "sab"
                ),
                self.opcoes_rapidas(
                    "Proximo fim de semana", Icons.CHAIR, Colors.BLUE_400, "sab"
                ),
                ft.Divider(),
                # Calendário
                Text(f"{self.current_date.strftime('%b %Y')}", size=16, weight="bold"),
                self.calendario,
                Divider(),
                ElevatedButton("Fechar", on_click=self.hide_card),
            ]
        )
