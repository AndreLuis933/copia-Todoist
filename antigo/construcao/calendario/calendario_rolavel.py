import flet as ft
import calendar
from datetime import datetime, timedelta


def main(page: ft.Page):
    page.title = "Calendário Rolável Infinito"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    page.window.always_on_top = True
    page.window.height = 750
    page.window.width = 700
    page.padding = 0

    current_date = datetime.now()
    months_loaded = 0
    is_loading = False

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
                    content=ft.Text(day, size=16, color="#121212"),
                    width=50,
                    height=50,
                    bgcolor="#BB86FC",
                    border_radius=ft.border_radius.all(5),
                    alignment=ft.alignment.center,
                )
                for day in ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
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
                            width=50,
                            height=50,
                            bgcolor="#1F1F1F",
                            border_radius=ft.border_radius.all(5),
                            alignment=ft.alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(ft.Container(width=50, height=50))
            calendar_grid.controls.append(week_row)

        return ft.Container(
            content=calendar_grid,
            margin=ft.margin.only(bottom=20),
            padding=20,
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
        spacing=10,
        padding=20,
        expand=True,
        on_scroll=on_scroll,
    )

    container = ft.Container(
        content=calendar_view,
        height=650,
        width=600,
        border=ft.border.all(1, ft.Colors.BLACK),
        border_radius=10,
    )

    page.add(container)

    load_more_months(3)


ft.app(target=main)
