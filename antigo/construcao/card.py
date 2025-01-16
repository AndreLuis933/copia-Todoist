import flet as ft
from datetime import datetime, timedelta
import calendar
from flet import *


def main(page: ft.Page):
    page.window.always_on_top = True
    page.window.height = 1000
    page.window.width = 1000
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"

    current_date = datetime.now()
    months_loaded = 0
    is_loading = False
    tamanho = 20

    def create_month_calendar(year, month):
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
                    width=tamanho,
                    height=tamanho,
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
                            width=tamanho,
                            height=tamanho,
                            bgcolor="#1F1F1F",
                            border_radius=ft.border_radius.all(5),
                            alignment=ft.alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(
                        ft.Container(width=tamanho, height=tamanho)
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

    def load_more_months(count):
        nonlocal months_loaded
        new_months = []
        for _ in range(count):
            date = current_date + timedelta(days=30.44 * months_loaded)
            year, month = date.year, date.month
            month_calendar = create_month_calendar(year, month)
            new_months.append(month_calendar)
            months_loaded += 1
        calendar_view.controls.extend(new_months)
        page.update()

    def on_scroll(e: ft.OnScrollEvent):
        nonlocal is_loading
        if not is_loading and e.pixels >= e.max_scroll_extent - 100:
            is_loading = True
            page.add(ft.ProgressRing())
            page.update()
            load_more_months(1)
            page.controls.pop()
            is_loading = False
            page.update()

    calendar_view = ft.ListView(
        expand=True,
        on_scroll=on_scroll,
    )

    calendario_scroll = ft.Container(
        content=calendar_view,
        height=205,
        width=250,
        border=ft.border.all(1, ft.Colors.BLACK),
        border_radius=10,
    )

    def show_card(e):
        card.visible = True
        page.update()

    def hide_card(e):
        card.visible = False
        page.update()

    def opcoes_rapidas(texto, icone, cor, complemento):
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

    vencimento_button = ft.ElevatedButton(
        text="Vencimento",
        on_click=show_card,
    )

    card = Container(
        content=Column(
            [
                TextField(
                    hint_text="Digite um vencimento",
                ),
                Divider(),
                opcoes_rapidas("Hoje", Icons.TODAY, Colors.GREEN_400, "sab"),
                opcoes_rapidas(
                    "Amanha", Icons.WB_SUNNY_OUTLINED, Colors.AMBER_400, "sab"
                ),
                opcoes_rapidas(
                    "Proxima semana", Icons.NEXT_WEEK, Colors.PURPLE_400, "sab"
                ),
                opcoes_rapidas(
                    "Proximo fim de semana", Icons.CHAIR, Colors.BLUE_400, "sab"
                ),
                ft.Divider(),
                # Calendário
                Text(f"{current_date.strftime('%b %Y')}", size=16, weight="bold"),
                calendario_scroll,
                Divider(),
                ElevatedButton("Fechar", on_click=hide_card),
            ]
        ),
        padding=15,
        border_radius=10,
        # bgcolor="white",
        shadow=BoxShadow(blur_radius=5),
        visible=False,
        width=250,
        height=700,
    )

    content = ft.Stack(
        [
            ft.GestureDetector(
                on_tap=hide_card,
                content=ft.Container(expand=True, bgcolor=Colors.TRANSPARENT),
            ),
            Column(
                [
                    vencimento_button,
                    card,
                ]
            ),
        ],
        expand=True,
    )

    page.add(content)

    load_more_months(3)


ft.app(target=main)

    def show_card(e):
        tarefa_vencimento.visible = True
        page.update()

    def opcoes_rapidas(texto, icone, cor, complemento):
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

    vencimento_button = ft.ElevatedButton(
        text="Vencimento",
        on_click=show_card,
    )

    tarefa_vencimento = Container(
        content=Column(
            [
                TextField(
                    hint_text="Digite um vencimento",
                ),
                Divider(),
                opcoes_rapidas("Hoje", Icons.TODAY, Colors.GREEN_400, "sab"),
                opcoes_rapidas(
                    "Amanha", Icons.WB_SUNNY_OUTLINED, Colors.AMBER_400, "sab"
                ),
                opcoes_rapidas(
                    "Proxima semana", Icons.NEXT_WEEK, Colors.PURPLE_400, "sab"
                ),
                opcoes_rapidas(
                    "Proximo fim de semana", Icons.CHAIR, Colors.BLUE_400, "sab"
                ),
                ft.Divider(),
                # Calendário
                Text(f"{current_date.strftime('%b %Y')}", size=16, weight="bold"),
                calendario,
                Divider(),
                ElevatedButton("Fechar", on_click=hide_card),
            ]
        ),
        padding=15,
        border_radius=10,
        # bgcolor="white",
        shadow=BoxShadow(blur_radius=5),
        visible=False,
        width=250,
        height=700,
    )
