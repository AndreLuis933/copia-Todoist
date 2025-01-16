import flet as ft
import calendar
from datetime import datetime, timedelta

def main(page: ft.Page):
    page.title = "Calendário Rolável"
    page.padding = 50
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    page.window.always_on_top = True
    page.window.height = 650
    page.window.width = 600
    page.scroll = "auto"

    current_date = datetime.now()
    start_year = current_date.year
    start_month = current_date.month

    def create_month_calendar(year, month):
        calendar.setfirstweekday(6)
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]
        
        calendar_grid = ft.Column(spacing=5)

        # Cabeçalho do calendário
        header = ft.Row(
            [ft.Text(f"{month_name} {year}", size=24, weight=ft.FontWeight.BOLD, color="#BB86FC")],
            alignment=ft.MainAxisAlignment.CENTER
        )
        calendar_grid.controls.append(header)

        # Dias da semana
        days_of_week = ft.Row(
            [ft.Container(
                content=ft.Text(day, size=16, color="#121212"),
                width=50,
                height=50,
                bgcolor="#BB86FC",
                border_radius=ft.border_radius.all(5),
                alignment=ft.alignment.center
             ) 
             for day in ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]],
            alignment=ft.MainAxisAlignment.CENTER
        )
        calendar_grid.controls.append(days_of_week)

        # Dias do mês
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
            )
        )

    def create_calendar_listview(num_months=24):
        calendar_list = ft.ListView(spacing=10, padding=20)
        
        for i in range(num_months):
            date = current_date + timedelta(days=30.44 * i)  # Aproximação para um mês
            year, month = date.year, date.month
            month_calendar = create_month_calendar(year, month)
            calendar_list.controls.append(month_calendar)
        
        return calendar_list

    calendar_view = create_calendar_listview()

    page.add(calendar_view)

ft.app(target=main)
